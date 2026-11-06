"""Permission-Slip Tokenized Human Approval System.

Cryptographically signed token-based human approval engine for TM AI Agent Toolkit.
"""

from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Dict, Any, Optional, List
import uuid
import time
import hmac
import hashlib

class ApprovalTicketStatus(str, Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    EXPIRED = "EXPIRED"

@dataclass
class ApprovalTicket:
    action: str
    reason: str
    target_resource: str
    expected_impact: str
    risk_level: str  # "LOW", "MEDIUM", "HIGH", "CRITICAL"
    payload: Dict[str, Any] = field(default_factory=dict)
    ticket_id: str = field(default_factory=lambda: f"TICK-{uuid.uuid4().hex[:8].upper()}")
    status: ApprovalTicketStatus = ApprovalTicketStatus.PENDING
    approver: Optional[str] = None
    created_at: float = field(default_factory=time.time)
    expires_at: float = field(default_factory=lambda: time.time() + 3600)  # 1 hour default
    decision_reason: Optional[str] = None
    signature: Optional[str] = None

    def sign(self, secret_key: str) -> str:
        data = f"{self.ticket_id}:{self.action}:{self.target_resource}:{self.status.value}"
        sig = hmac.new(secret_key.encode(), data.encode(), hashlib.sha256).hexdigest()
        self.signature = sig
        return sig

    def verify_signature(self, secret_key: str) -> bool:
        if not self.signature:
            return False
        data = f"{self.ticket_id}:{self.action}:{self.target_resource}:{self.status.value}"
        expected = hmac.new(secret_key.encode(), data.encode(), hashlib.sha256).hexdigest()
        return hmac.compare_digest(self.signature, expected)

class ApprovalManager:
    """Manages active approval tickets and verification gates."""

    def __init__(self, secret_key: str = "molavi-default-local-secret"):
        self.secret_key = secret_key
        self._tickets: Dict[str, ApprovalTicket] = {}

    def create_ticket(self, action: str, reason: str, target: str, impact: str, risk: str = "HIGH", payload: Optional[Dict[str, Any]] = None) -> ApprovalTicket:
        t = ApprovalTicket(
            action=action,
            reason=reason,
            target_resource=target,
            expected_impact=impact,
            risk_level=risk,
            payload=payload or {}
        )
        t.sign(self.secret_key)
        self._tickets[t.ticket_id] = t
        return t

    def get_ticket(self, ticket_id: str) -> Optional[ApprovalTicket]:
        return self._tickets.get(ticket_id)

    def approve(self, ticket_id: str, approver: str, reason: str = "Approved by human operator") -> bool:
        t = self._tickets.get(ticket_id)
        if not t:
            return False
        if time.time() > t.expires_at:
            t.status = ApprovalTicketStatus.EXPIRED
            return False
        t.status = ApprovalTicketStatus.APPROVED
        t.approver = approver
        t.decision_reason = reason
        t.sign(self.secret_key)
        return True

    def reject(self, ticket_id: str, approver: str, reason: str = "Rejected by human operator") -> bool:
        t = self._tickets.get(ticket_id)
        if not t:
            return False
        t.status = ApprovalTicketStatus.REJECTED
        t.approver = approver
        t.decision_reason = reason
        t.sign(self.secret_key)
        return True

    def list_pending(self) -> List[ApprovalTicket]:
        now = time.time()
        for t in self._tickets.values():
            if t.status == ApprovalTicketStatus.PENDING and now > t.expires_at:
                t.status = ApprovalTicketStatus.EXPIRED
        return [t for t in self._tickets.values() if t.status == ApprovalTicketStatus.PENDING]

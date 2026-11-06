#!/usr/bin/env python3
"""Example: Permission-Slip Human-in-the-Loop Approval Ticket Lifecycle."""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from molavi_agentic_os.security import ApprovalManager, ApprovalTicketStatus

def demonstrate_permission_flow():
    mgr = ApprovalManager(secret_key="my-production-key")

    print("Agent is attempting an L2 sensitive action: sending an outreach email...")
    ticket = mgr.create_ticket(
        action="send_email",
        reason="Prospective client follow-up on partnership proposal",
        target="ceo@targetcompany.com",
        impact="Sends company pitch directly to C-level executive",
        risk="HIGH",
        payload={"subject": "Strategic AI Visibility Proposal", "recipient": "ceo@targetcompany.com"}
    )

    print(f"Approval Ticket Created: {ticket.ticket_id}")
    print(f"Status: {ticket.status.value}")
    print(f"Signature Verified: {ticket.verify_signature(mgr.secret_key)}")

    # Operator approves ticket
    print("\nHuman Operator reviewing ticket...")
    mgr.approve(ticket.ticket_id, approver="taqi@molavi.pro", reason="Verified email text and target address")

    print(f"Updated Ticket Status: {ticket.status.value}")
    print(f"Approver: {ticket.approver}")
    print(f"Signature Valid After Approval: {ticket.verify_signature(mgr.secret_key)}")

if __name__ == "__main__":
    demonstrate_permission_flow()

"""Permission levels and access control matrix."""

from enum import Enum
from typing import Dict, Any

class PermissionLevel(str, Enum):
    L0_READ_ONLY = "L0_READ_ONLY"
    L1_DRAFT_RECOMMEND = "L1_DRAFT_RECOMMEND"
    L2_HUMAN_APPROVAL = "L2_HUMAN_APPROVAL"
    L3_PRE_AUTHORIZED = "L3_PRE_AUTHORIZED"

# Action classification table
SENSITIVE_ACTIONS = {
    "send_email": PermissionLevel.L2_HUMAN_APPROVAL,
    "publish_content": PermissionLevel.L2_HUMAN_APPROVAL,
    "execute_trade": PermissionLevel.L2_HUMAN_APPROVAL,
    "delete_data": PermissionLevel.L2_HUMAN_APPROVAL,
    "shell_exec": PermissionLevel.L2_HUMAN_APPROVAL,
    "database_mutate": PermissionLevel.L2_HUMAN_APPROVAL,
    "read_data": PermissionLevel.L0_READ_ONLY,
    "draft_text": PermissionLevel.L1_DRAFT_RECOMMEND,
    "analyze_metrics": PermissionLevel.L0_READ_ONLY,
}

def check_permission(agent_level: PermissionLevel, requested_action: str) -> bool:
    """Returns True if agent level is sufficient, False if explicit approval needed."""
    required_level = SENSITIVE_ACTIONS.get(requested_action, PermissionLevel.L1_DRAFT_RECOMMEND)
    hierarchy = [
        PermissionLevel.L0_READ_ONLY,
        PermissionLevel.L1_DRAFT_RECOMMEND,
        PermissionLevel.L2_HUMAN_APPROVAL,
        PermissionLevel.L3_PRE_AUTHORIZED,
    ]
    return hierarchy.index(agent_level) >= hierarchy.index(required_level)

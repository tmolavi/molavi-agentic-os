"""Tests for TM Open Source Governance Validator."""

import os
import pytest
from scripts.check_governance import check_repository

def test_repository_governance_compliance():
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    is_compliant = check_repository(repo_root)
    assert is_compliant is True

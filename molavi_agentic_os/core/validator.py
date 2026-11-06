"""Bot-Ready Validator & Scoring Engine for Molavi Agentic OS.

Scores agents and components on an objective 100-point scale:
- Metadata & Purpose clarity (20 pts)
- Strict Input/Output Schema completeness (20 pts)
- Execution Boundaries & Permission Gates (20 pts)
- Security & Tool Allowlists (20 pts)
- Reproducible Test Cases & Examples (20 pts)
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any
from .agent import AgentDefinition
from .skill import SkillDefinition
from .team import TeamDefinition

@dataclass
class ValidationResult:
    target_id: str
    target_type: str
    is_valid: bool
    score: int  # 0 to 100
    checks_passed: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)
    errors: List[str] = field(default_factory=list)

class BotReadyValidator:
    """Validates agents, skills, teams and workflows for production readiness."""

    @classmethod
    def validate_agent(cls, agent: AgentDefinition) -> ValidationResult:
        score = 0
        checks = []
        warnings = []
        errors = []

        # 1. Metadata check (20 pts)
        if agent.metadata.id and agent.metadata.name and len(agent.metadata.purpose) > 15:
            score += 20
            checks.append("Metadata and purpose clearly defined (+20)")
        else:
            errors.append("Agent ID, Name, or Purpose is missing or too brief")

        # 2. Input/Output schemas (20 pts)
        if agent.input_schema and agent.output_schema:
            score += 20
            checks.append("Deterministic input and output schemas configured (+20)")
        elif agent.input_schema or agent.output_schema:
            score += 10
            warnings.append("Partial input or output schema provided (+10)")
        else:
            warnings.append("Missing structured input/output schemas (0/20)")

        # 3. Execution Boundaries (20 pts)
        if len(agent.execution_boundaries) >= 2:
            score += 20
            checks.append(f"Explicit execution boundaries defined ({len(agent.execution_boundaries)} rules) (+20)")
        elif len(agent.execution_boundaries) == 1:
            score += 10
            warnings.append("Only 1 execution boundary specified (+10)")
        else:
            errors.append("No execution boundaries specified (high risk of unbounded actions)")

        # 4. Permission and System Instructions (20 pts)
        if len(agent.system_instructions) >= 50 and agent.permission_level:
            score += 20
            checks.append(f"System instructions robust with permission level {agent.permission_level.value} (+20)")
        else:
            errors.append("System instructions too sparse (<50 chars)")

        # 5. Test cases & Examples (20 pts)
        if len(agent.test_cases) >= 1 or len(agent.example_usage) > 20:
            score += 20
            checks.append("Verification test cases or concrete usage example provided (+20)")
        else:
            warnings.append("No automated test cases or usage examples provided")

        is_valid = len(errors) == 0 and score >= 70
        return ValidationResult(
            target_id=agent.metadata.id,
            target_type="Agent",
            is_valid=is_valid,
            score=score,
            checks_passed=checks,
            warnings=warnings,
            errors=errors,
        )

    @classmethod
    def validate_skill(cls, skill: SkillDefinition) -> ValidationResult:
        score = 0
        checks = []
        warnings = []
        errors = []

        if skill.metadata.id and skill.metadata.name and skill.metadata.description:
            score += 25
            checks.append("Metadata defined (+25)")
        else:
            errors.append("Skill metadata incomplete")

        if len(skill.trigger_conditions) >= 1:
            score += 25
            checks.append("Trigger conditions specified (+25)")
        else:
            warnings.append("No trigger conditions specified")

        if len(skill.execution_instructions) >= 30:
            score += 25
            checks.append("Execution instructions present (+25)")
        else:
            errors.append("Execution instructions too brief")

        if len(skill.security_considerations) >= 1:
            score += 25
            checks.append("Security considerations detailed (+25)")
        else:
            warnings.append("No security considerations noted")

        is_valid = len(errors) == 0 and score >= 70
        return ValidationResult(
            target_id=skill.metadata.id,
            target_type="Skill",
            is_valid=is_valid,
            score=score,
            checks_passed=checks,
            warnings=warnings,
            errors=errors,
        )

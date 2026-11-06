# Security Policy & Permission Model

Molavi Agentic OS is built on a **Security-First & Principle of Least Privilege** philosophy.

## 1. Permission Hierarchy

Every agent and tool executes under a deterministic permission classification:

| Level | Code | Description | Permitted Capabilities |
|---|---|---|---|
| **L0** | `L0_READ_ONLY` | Read-only analysis | Web browsing, document reading, metric calculation, log parsing |
| **L1** | `L1_DRAFT_RECOMMEND` | Drafting & local proposing | Writing drafts, proposing code diffs, compiling briefs (no external side effects) |
| **L2** | `L2_HUMAN_APPROVAL` | Human-in-the-Loop Required | **DEFAULT for sensitive actions:** Sending emails, executing trades, web server modifications, data deletion, shell execution |
| **L3** | `L3_PRE_AUTHORIZED` | Pre-authorized automation | Restricted to sandboxed, pre-approved staging workflows with verified audit trails |

## 2. Permission-Slip Ticket Architecture

Sensitive operations (such as sending external emails, publishing articles to production CMS, or executing financial transactions) cannot execute autonomously. When an L2 operation is reached:
1. Execution halts and an HMAC-signed `ApprovalTicket` is generated with an explicit reason, target resource, risk level, and expiration timestamp.
2. The human operator reviews and cryptographically approves or rejects the ticket via CLI:
   ```bash
   molavi-agentic-os approval approve --ticket-id TICK-ABCD1234
   ```
3. Only verified, signed tickets allow the action worker to proceed.

## 3. Foreman Verification Gate ("No Guessing")

Agents are prohibited from declaring tasks "COMPLETED" without verifiable evidence artifacts (source URLs, code diffs, test logs). Unverifiable guesses are flagged and rejected by `ForemanVerificationGate`.

## 4. Reporting Vulnerabilities

To report a vulnerability or prompt-injection escape, please email security@molavi.pro. Security advisories are addressed within 48 hours.

# Skills and verification

## What this repository demonstrates

A PagerDuty-style decision CLI that validates the incident age and deadline, prioritizes acknowledgment status, and recommends wait or escalate based on the deadline.

## Reproduce the result

The sample recommends escalation at age eight with a five-minute deadline. The acknowledged scenario suppresses escalation. Reproduce the primary fixture with `python3 agent.py --age 8 --deadline 5`.

Run `make verify` locally. Ruff and Bandit medium/high checks passed for the checked Python code.

## Scope

The decision uses CLI inputs. The lab does not contact PagerDuty or send a page.

Check acknowledgment state before elapsed time. An acknowledged incident takes precedence in this local decision model.

[agent.py](../agent.py) · [examples/Demo 1.stdout.txt](../examples/Demo%201.stdout.txt) · [Architecture](../docs/ARCHITECTURE.md) · [Case study](../docs/CASE_STUDY.md) · [Runbook](../docs/RUNBOOK.md) · [CI template](../docs/github-actions/ci.yml)

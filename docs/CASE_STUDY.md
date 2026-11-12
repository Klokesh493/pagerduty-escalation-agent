# Pagerduty Escalation Agent walkthrough

## Business problem

Offline decision helper for incident acknowledgment and escalation.

## Reproduce the workflow

Run `python3 agent.py --age 8 --deadline 5` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
escalate
```

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.

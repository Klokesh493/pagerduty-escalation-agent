# Pagerduty Escalation Agent architecture

Offline decision helper for incident acknowledgment and escalation.

```mermaid
flowchart LR
    N0["CLI arguments"]
    N1["agent.py"]
    N2["Compare elapsed minutes to the acknowledgment deadline before recommending escalation."]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.

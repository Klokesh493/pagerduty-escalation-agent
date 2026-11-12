PYTHON ?= python3

.PHONY: verify
verify:
	$(PYTHON) agent.py --age 8 --deadline 5

.PHONY: replay
replay:
	$(PYTHON) tools/replay_examples.py --report reports/replay.md

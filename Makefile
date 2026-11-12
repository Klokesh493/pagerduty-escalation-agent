PYTHON ?= python3

.PHONY: verify
verify:
	$(PYTHON) agent.py --age 8 --deadline 5

UV ?= uv
PY ?= $(UV) run -q python
RUFF = $(UV) run -q -m ruff
PYTEST = $(UV) run -q -m pytest

PATHS = src tests

.PHONY: ci pre

pre:
	$(RUFF) format $(PATHS)
	$(RUFF) check --fix $(PATHS)
	$(PYTEST) -q

ci: # format -> lint -> test for CLI
	$(RUFF) format --check $(PATHS)
	$(RUFF) check $(PATHS)
	$(PYTEST) -q
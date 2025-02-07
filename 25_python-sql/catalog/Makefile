psql-connect:
	psql -U postgres -h localhost -d test -W

console:
	@python-console

test:
	uv run pytest

install:
	uv sync

run:
	uv run python3 src/main.py

.PHONY: test

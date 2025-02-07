.PHONY: psql-connect

psql-connect:
	psql -U postgres -h localhost -d test -W

run:
	uv run python3 src/sample.py

console:
	@uv run flask shell

install:
	uv sync

lint:
	uv run ruff check

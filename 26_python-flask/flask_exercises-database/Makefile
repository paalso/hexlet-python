export PYTHONPATH=src

psql-connect:
	psql -U postgres -h localhost -d test -W

console:
	@uv run flask shell

start:
	uv run flask run -h 0.0.0.0 -p 8080

debug:
	uv run flask --debug run -h 0.0.0.0 -p 8080

run:
	uv run gunicorn --workers=4 --bind=127.0.0.1:8000 src.app:app

test:	
	uv run pytest -vv tests

routes:
	uv run flask routes

install:
	uv sync

build:
	./build.sh

lint:
	uv run ruff check

lint-fix:
	uv run ruff check --fix

check: test lint

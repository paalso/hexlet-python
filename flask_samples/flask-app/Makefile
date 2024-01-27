start:
	poetry run flask --app flask_app/example run --port 8000

debug:
	poetry run flask --app flask_app/example --debug run --port 8000

install:
	poetry install

test:
	@poetry run pytest

test-cov:
	poetry run pytest --cov

test-coverage:
	poetry run pytest --cov=page_loader --cov-report xml

lint:
	@poetry run flake8 flask_app
	@poetry run flake8 tests

selfcheck:
	poetry check

check:
	make lint
	make test

build:
	poetry build

.PHONY: install test test-cov test-coverage lint selfcheck check build run install-dist
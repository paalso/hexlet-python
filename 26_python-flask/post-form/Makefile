export PYTHONPATH=src

console:
	@poetry run flask shell

test:
	poetry run pytest -vv tests

install:
	poetry install

debug:
	poetry run flask --app hexlet_flask/app --debug run --port 8000

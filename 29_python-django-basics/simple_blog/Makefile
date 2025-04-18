start:
	uv run python3 manage.py runserver 0.0.0.0:8080

test:
	uv run python3 manage.py test tests/

console:
	uv run python3 manage.py shell_plus --ipython

install:
	uv sync

# db aliases
sqlite:
	sqlite3 db.sqlite3

migrate:
	uv run python3 manage.py migrate

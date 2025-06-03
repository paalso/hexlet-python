# Port for development server
PORT = 8080

MANAGE := uv run python manage.py

# Run development server
start:
	uv run python3 manage.py runserver 0.0.0.0:$(PORT)

.PHONY: test
test:
	uv run pytest

.PHONY: setup
setup: db-clean install migrate

.PHONY: install
install:
	@uv sync

.PHONY: db-clean
db-clean:
	@rm db.sqlite3 || true

.PHONY: makemigrations
makemigrations:
	@$(MANAGE) makemigrations

.PHONY: migrate
migrate:
	@$(MANAGE) migrate

.PHONY: shell
shell:
	@$(MANAGE) shell_plus --ipython

sqlite:
	sqlite3 db.sqlite3

showmigrations:
	@$(MANAGE) showmigrations

.PHONY: lint
lint:
	uv run ruff check python_django_orm_blog

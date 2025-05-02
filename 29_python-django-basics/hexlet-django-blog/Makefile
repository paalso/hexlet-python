# Port for development server
PORT = 8000

# Install project dependencies
install:
	uv sync

# Create and apply database migrations
migrate:
	uv run python3 manage.py makemigrations
	uv run python3 manage.py migrate

# Run development server
start:
	uv run python3 manage.py runserver 0.0.0.0:$(PORT)

# Launch Django shell
shell:
	uv run python3 manage.py shell

# Launch Django shell with IPython and shell_plus
console:
	uv run python3 manage.py shell_plus --ipython

# Run test suite
test:
	uv run python3 manage.py test

# Connect to the SQLite database manually
sqlite:
	sqlite3 db.sqlite3

# Show all migrations and their status
showmigrations:
	uv run python3 manage.py showmigrations

# Show raw SQL for a specific migration (example usage: make sqlmigrate app_name=articles migration_num=0001)
sqlmigrate:
	uv run python3 manage.py sqlmigrate $(app_name) $(migration_num)

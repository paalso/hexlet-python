#!/usr/bin/env bash

INIT_SQL_FILE=${1:-init.sql}  # Используем переданный аргумент или по умолчанию init.sql

export $(grep -v '^#' .env | xargs)

if [ -z "$DB_USER" ] || [ -z "$DB_PASSWORD" ] || [ -z "$DB_HOST" ] || [ -z "$DB_NAME" ]; then
  echo "Error: One or more required DB credentials are missing. Check your .env file."
  echo "Required variables: DB_USER, DB_PASSWORD, DB_HOST, DB_NAME"
  exit 1
fi

if [ -z "$DATABASE_URL" ]; then
  echo "Warning: DATABASE_URL not specified. Generating DATABASE_URL using DB credentials."
  export DATABASE_URL="postgresql://${DB_USER}:${DB_PASSWORD}@${DB_HOST}/${DB_NAME}"
fi

echo "DATABASE_URL: $DATABASE_URL"

if [ ! -f "$INIT_SQL_FILE" ]; then
  echo "Error: $INIT_SQL_FILE not found. Make sure the file exists in the current directory."
  exit 1
fi

# Запуск psql с указанным файлом
psql -a -d "$DATABASE_URL" -f "$INIT_SQL_FILE"

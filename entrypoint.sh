#!/bin/sh

# Wait for PostgreSQL to be available
until pg_isready -h "$PG_HOST" -p "$PG_PORT" -U "$POSTGRES_USER"; do
  echo "Waiting for PostgreSQL to start..."
  sleep 2
done

# Check if the database exists, if not, create it
psql -h "$PG_HOST" -p "$PG_PORT" -U "$POSTGRES_USER" -tc "SELECT 1 FROM pg_database WHERE datname = '$POSTGRES_DBNAME'" | grep -q 1 || psql -h "$PG_HOST" -p "$PG_PORT" -U "$POSTGRES_USER" -c "CREATE DATABASE $POSTGRES_DBNAME"

# Run the original entrypoint command
exec "$@"

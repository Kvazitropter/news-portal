install:
	uv sync
	cp .env.example .env

dev:
	uv run manage.py runserver

migrate:
	uv run manage.py makemigrations
	uv run manage.py migrate

console:
	uv run manage.py shell
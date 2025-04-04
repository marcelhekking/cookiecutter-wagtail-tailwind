DATABASE_NAME ?= {{cookiecutter.project_slug}}

.PHONY: all clean install requirements


all: clean install frontend compilemessages exampledata

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	find . -name '*.egg-info' | xargs rm -rf

rebuild:
	dropdb --if-exists $(DATABASE_NAME)
	createdb $(DATABASE_NAME)
	uv run manage.py migrate
	uv run manage.py initadmin

install:
	uv sync

makemigrations:
	uv run manage.py makemigrations

migrate:
	uv run manage.py migrate

runserver:
	uv run manage.py runserver

test:
	uv run pytest tests/ -vvv

watch:
	yarn watchify

build:
	sudo docker build -t {{cookiecutter.project_slug}}-web:latest -f Dockerfile .

up:
	fish -c 'envsource .env_var; and docker compose -p {{cookiecutter.project_slug}} -f docker-compose.yml up -d'

down:
	fish -c 'envsource .env_var; and docker compose -p {{cookiecutter.project_slug}} -f docker-compose.yml down'

sh:
	docker exec -it {{cookiecutter.project_slug}}-web-1 sh

shell:
	docker exec -it {{cookiecutter.project_slug}}-web-1 python manage.py shell

public:
	mkdir -p ~/www/omni/public/mediafiles
	mkdir -p ~/www/omni/public/staticfiles

1024:
	# 1024 is the group id of the docker container
	sudo chown -R :1024 ~/www/omni/public/mediafiles
	sudo chmod -R 777 ~/www/omni/public/mediafiles
	sudo chmod g+s ~/www/omni/public/mediafiles
	sudo chown -R :1024 ~/www/omni/public/staticfiles
	sudo chmod -R 777 ~/www/omni/public/staticfiles
	sudo chmod g+s ~/www/omni/public/staticfiles

#
# Format / Lint targets
#
format: format_backend format_sort format_frontend

format_backend: ruff sort

format_frontend: prettier

format_sort: sort

sort: sort_fix

sort_check:
	uv run ruff check src tests --target-version=py311 --exclude=migrations --select I

sort_fix:
	uv run ruff check src tests --target-version=py311 --exclude=migrations --select I --fix

ruff: ruff_fix

ruff_check:
	uv run ruff check src tests --target-version=py39 --exclude=migrations

ruff_fix:
	uv run ruff check src tests --target-version=py39 --exclude=migrations --fix



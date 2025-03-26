# {{cookiecutter.project_name}}

## Introduction

This repo builds a website based on Django and Wagtail. The production version runs in two Docker containers. One container provides a Gunicorn webservice serving Django and the other container provides a Postgress database service. Nginx on the host machine can then be used as a proxy-server. There is another cookiecutter template available that sets up Digital Ocean droplets to run these containers (<https://github.com/marcelhekking/cookiecutter-infra-do/>)

## Installation

### Local installation and development

Clone the Git repo into a local folder:

```bash
git clone git@gitlab.com:marcelhekking/{{cookiecutter.project_slug}}.git
```

#### Running the container in production mode locally

With Docker, you can start a container in production mode.

##### Changing the group of public static and media folders

The web Docker performs actions under GI 1024 (e.g., running `collectstatic`). In the Docker files, a physical volume on the host is linked with folders inside Docker. To avoid permission errors:

- Create a public folder at the project level (next to `src`)
- Create `staticfiles` and `mediafiles` folders and run the following `make` command (<https://www.gnu.org/software/make/>):

```bash
make public
```

then grant access for docker:

```bash
make 1024
```

##### Starting the containers in production mode

Go to the root of the project (`{{cookiecutter.project_slug}}`) and first (only to be done once) build the container with:

```bash
sudo docker build -t {{cookiecutter.project_slug}}-web:latest -f Dockerfile .
```

Then start the container with:

```bash
make up
```

and shut it down with:

```bash
make down
```

#### Running the Django development server locally

Install the frontend:

```bash
yarn install
```

install all dependencies specified in the `pyproject.toml`:

```bash
uv sync
```

Create a database:

```bash
createdb {{cookiecutter.project_slug}}
```

Migrate the database and install a superuser. This is the admin as specified in `base.py`.

```bash
make rebuild
```

Start the Django development server

```bash
make runserver
```

### Installing Pre-commit

Pre-commit is a Python package to check code via git hooks before it ends up in a Git repo. Before committing, you need to install pre-commit. In the correct Python virtual environment, go to the root of the project (`{{cookiecutter.project_slug}}`) and run:

```bash
pre-commit install
```

To test, you can check existing files with pre-commit:

```bash
pre-commit run --all-files
```

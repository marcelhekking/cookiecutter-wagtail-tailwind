# {{cookiecutter.project_name}}

## Installation

### Local installation and development

Clone the Git repo into a local folder:

```bash
git clone git@gitlab.com:marcelhekking/{{cookiecutter.project_slug}}.git
```

With Docker, you can start a container for development. Make sure Docker and Docker Compose are installed (<https://docs.docker.com/compose/install/>).

Go to the root of the project (`{{cookiecutter.project_slug}}`) and build the dev container with:

```bash
docker compose -f docker-compose.yml build
```

Then start the container with:

```bash
docker compose -f docker-compose.yml up
```

### Changing the group of public static and media folders

The web Docker performs actions under GI 1024 (e.g., running `collectstatic`). In the Docker files, a physical volume on the host is linked with folders inside Docker. To avoid permission errors:

- Create a public folder at the project level (next to `src`)
- Create `staticfiles` and `mediafiles` folders and run the following for both folders:

```bash
mkdir -p public/staticfiles && mkdir -p public/mediafiles
```

and execute the following make command (<https://www.gnu.org/software/make/>):

```bash
make 1024
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

## Creating a minified bundle of JS and CSS files

For modifying and effectively creating CSS and JS files, `watchify` is used. Changes to CSS and JS are observed and converted into a minified bundle. This minified bundle is deployed to production.

### Requirements

The following Node.js applications must be installed:

- browserify
- watchify
- uglify-js
- browserify-css

All dependencies can be installed with the `yarn install` command in the root of the project:

```bash
cd ~/../{{cookiecutter.project_slug}}$
yarn install
```

Start watchify to create a minified bundle 'on-the-fly':

```bash
cd ~/../{{cookiecutter.project_slug}}$
yarn run watchify
```

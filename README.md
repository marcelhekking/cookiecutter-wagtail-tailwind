# Cookiecutter template for creating a Wagtail project with Tailwind CSS.

## Introduction

This repo is a cookiecutter template with which one can create a Wagtail site that can be automatically deployed to a Digial Ocean droplet. See [this](https://github.com/marcelhekking/cookiecutter-infra-do) cookiecutter on how to create Digital Ocean droplets using Pulumi.

## How to install this template

First install [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and then run:

```bash
cookiecutter https://github.com/marcelhekking/cookiecutter-wagtail-tailwind
```

You'll be asked some questions about the project. After installation read the README.md file of the just created project on how to further set things up to run the site locally or via Docker.

## Making CI/CD via Github actions possible for a created site

- After the cookiecutter created the site, go into to the project's folder and make a uv lock file first by running

    ```bash
    uv sync
    ```

- make a Git repo out of this site and make it available on your Github account.

- Add two secret variables to the repo:
  - PRIVATE_KEY_DROPLET (the private SSH key of an SSH pair as created on the droplet with `ansible-playbook ansible/ssh.yml`) (see [this](https://github.com/marcelhekking/cookiecutter-infra-do) cookiecutter project)
  - PULUMI_ACCESS_TOKEN (a token to access `{{cookiecutter.pulumi_environment}}`)

- Ensure you have a Pulumi cloud account with an installed environment named {{cookiecutter.pulumi_environment}}, containing the following key/value pairs:
  - DATABASE="postgres"
  - DEBUG="0"
  - DOMAIN_NAME="{{cookiecutter.domain_name}}"
  - DROPLET_IP="DROPLET IP ADDRESS"
  - MEDIAFILES_HOST="/home/public/mediafiles"
  - NAMESPACE="GITHUB USER NAME"
  - PERSONAL_ACCESS_TOKEN="GITHUB PERSONAL ACCESS TOKEN"
  - POSTGRES_DB="DB NAME"
  - POSTGRES_PASSWORD="DB PASSWORD"
  - POSTGRES_USER="postgres"
  - SECRET_KEY="DJANGO SECRET"
  - SQL_DATABASE="DB NAME"
  - SQL_HOST="db"
  - SQL_PASSWORD="DB PASSWORD"
  - SQL_PORT="5432"
  - SQL_USER="postgres"
  - STATICFILES_HOST="/home/public/staticfiles"

  If you want email enabled:
  - EMAIL_HOST_USER (user to log in at email provider)
  - EMAIL_HOST_PASSWORD (password to log in at email provider)
  - EMAIL_RECIPIENT_LIST (list if email addresses that should be notified)
  - DEFAULT_FROM_EMAIL (email address of sender)
# {{cookiecutter.project_name}}

## Installeren

### Lokaal installeren en ontwikkelen

Clone de Git repo in een lokale folder:

```bash
git clone git@gitlab.com:marcelhekking/{{cookiecutter.project_slug}}.git
```

Met docker kan er een container gestart worden voor ontwikkeling. Zorg er voor dat docker en docker-compose geïnstalleerd zijn (<https://docs.docker.com/compose/install/>)

Ga naar the root van het project (`{{cookiecutter.project_slug}}`) en 'build' de dev container met:

```bash
docker compose -f docker-compose.yml build
```

Start daarna de container op met:

```bash
docker compose -f docker-compose.yml  up
```

### Group wijzigen van public static en media folders

Web docker doet acties under GI 1024 (bijvoorbeeld `collectstatic` draaien). In de Docker files wordt er een fysiek volume op de host gekoppeld met folders binne docker. Om geen permissie error te krijgen:

- maak public folder aan op project niveau (dus naast `src`)
- maake `staticfiles` en `mediafiles` folder aan en voor voor beide folders het volgende uit:

```bash
mkdir -p public/staticfiles && mkdir -p public/mediafiles
```

en voer het volgende make commando uit:

```bash
make 1024
```

### Pre-commit installereren

Pre-commit is een Python package om via git hooks code te checken alvorens het in een Git repo terecht komt. Voordat je een commit doet moet je pre-commit installeren. In de juiste Python virtuele omgeving, ga naar the root van het project (`{{cookiecutter.project_slug}}`) en voer uit:

```bash
pre-commit install
```

Om te testen kun je bestaande bestanden checken met pre-commit:

```bash
pre-commit run --all-files
```

## Een minified bundel maken van JS en CSS bestanden

Voor het aanpassen en effectief maken van CSS en JS files wordt er gebruikt gemaakt van `watchify`. Veranderingen aan CSS en JS worden waargenomen en omgezet naar een minified bundle. Deze minified bundle wordt uitgerold naar productie.

### Voorwaarden

De volgende Node.js applicaties moeten worden geïnstalleerd:

- browserify
- watchify
- uglify-js
- browserify-css

Alle dependencies zijn te installeren met het `yarn install` commando in de root van het project:

```bash
cd ~/../{{cookiecutter.project_slug}}$
yarn install
```

Start watchify om 'on-the-fly' een minified bundle te maken maken:

```bash
cd ~/../{{cookiecutter.project_slug}}$
yarn run watchify
```

## Dependencies



## Google pingen

Log in of de web container via Portainers en voer dan uit:

```Bash
python manage.py ping_google sitemap.xml
```

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)
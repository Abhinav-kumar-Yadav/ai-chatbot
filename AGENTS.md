# Repository Guidelines

## Overview of Project
- This project is simpal Ai chatbot which use `ollama's` different free models to response and also able to search the web by using `Firecrawl` module 

## Project Structure

The Django project is under `my-project/aiwebsearching/`. `manage.py` is its command entry point, the inner `aiwebsearching/` package holds project configuration, and `myapp/` contains the application. Keep new application behavior in `myapp/` unless it belongs to project-wide configuration. The `.env`, database, and virtual environment are local-only; never read or modify `.env`.

## Architecture Tree

```text
web-searching/
|-- .gitignore
|-- AGENTS.md
|-- requirements.txt
|-- myenv/                              # Local Python virtual environment
`-- my-project/
    `-- aiwebsearching/
        |-- .env                        # Local secrets; do not read or modify
        |-- .gitignore
        |-- db.sqlite3                  # Local development database
        |-- manage.py
        |-- aiwebsearching/             # Django project configuration
        |   |-- __init__.py
        |   |-- asgi.py
        |   |-- settings.py
        |   |-- urls.py                 # Project URL routing
        |   `-- wsgi.py
        `-- myapp/                      # Application code
            |-- __init__.py
            |-- admin.py
            |-- apps.py
            |-- models.py
            |-- serialization.py
            |-- tests.py
            |-- urls.py                 # App URL routing
            |-- views.py
            `-- migrations/
                |-- __init__.py
                |-- 0001_initial.py      # Initial Users table
                `-- 0002_delete_userserialcounter_remove_users_sr_no.py
```

## Development Commands

Run commands from the repository root, using the virtual environment's executable paths:

```powershell
.\myenv\Scripts\python.exe -m pip install -r requirements.txt
.\myenv\Scripts\python.exe my-project\aiwebsearching\manage.py check
.\myenv\Scripts\python.exe my-project\aiwebsearching\manage.py migrate
.\myenv\Scripts\python.exe my-project\aiwebsearching\manage.py runserver
.\myenv\Scripts\python.exe my-project\aiwebsearching\manage.py test
```

These install dependencies, check project configuration, apply database migrations, start the local development server, and run Django tests, respectively.

## Style and Naming

Follow standard Python conventions: four spaces for indentation, `snake_case` for functions and variables, `PascalCase` for classes, and descriptive lowercase module names. Use Django's established patterns for views, models, URL names, and migrations. No formatter or linter is currently configured; keep changes focused and consistent with nearby code.

## Testing

Tests use Django's built-in test runner. Add tests in the relevant app's `tests.py` or a `tests/` package, with test classes derived from `django.test.TestCase` and methods named `test_*`. Run the test command above after changing application behavior or models; add migrations when model definitions change.

## Commits and Pull Requests

The repository has no commit history yet, so no established commit format is available. Use short imperative commit subjects, such as `Add search results view`. Pull requests should describe the change, note relevant checks, link related issues when applicable, and include screenshots for visible UI changes.

## Configuration and Secrets

- Keep credentials and machine-specific settings out of source control. Install dependencies from `requirements.txt`; do not add the virtual environment or generated database files to commits.
- Never read, modify,open,delete `.env` file
- Never commit it in git 

## Codex Project Guidance

This `AGENTS.md` is the canonical project instruction file for Codex. As the project grows, keep durable decisions, verified commands, and conventions current here. Confirm details against the repository before documenting them, and remove guidance that becomes outdated. Add nested `AGENTS.md` files only when a subdirectory needs distinct instructions.

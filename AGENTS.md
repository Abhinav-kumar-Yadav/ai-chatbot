# Repository Guidelines

## Project Structure

The repository root contains `requirements.txt` and the Python virtual environment `myenv/`. The Django project lives in `my-project/aiwebsearching/`: `manage.py` is the management entry point, `aiwebsearching/` contains project settings and URL configuration, and `myapp/` contains application code, migrations, and tests. Keep new application behavior in `myapp/` unless it belongs to project-wide configuration. Do not commit the local database or virtual environment.

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

Keep credentials and machine-specific settings out of source control. Install dependencies from `requirements.txt`; do not add the virtual environment or generated database files to commits.

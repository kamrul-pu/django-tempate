# Django Template

A Django REST Framework starter template with JWT auth, and a built-in
`Organization` (multi-vendor) layer so multiple tenants can share one
deployment.

## Stack

- Django + Django REST Framework
- JWT auth via `djangorestframework-simplejwt`
- PostgreSQL (prod) / SQLite (local dev, automatic when `DEBUG=True`)
- Docker / docker-compose

## Getting started

### With Docker (recommended)

```bash
cp dot-env-example.txt .env   # edit as needed
docker-compose up --build
```

This waits for the database, runs migrations, and starts the dev server on
`http://localhost:8000`.

### Without Docker

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements/dev.txt
cp dot-env-example.txt .env
cd app
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Multi-tenant (multi-vendor) design

Every tenant-scoped model should inherit one of the base classes in
`app/common/models.py`:

- `BaseModelWithUID` — uid/status/timestamps only, no tenant scoping.
- `BaseModelWithOrg` — adds an `organization` FK. Use for models that need
  org-scoping but no name/slug/description.
- `NameSlugDescriptionBaseModel` — name/slug/description, **not** tenant
  scoped (shared/global entities).
- `NameSlugDescriptionBaseModelWithOrg` — name/slug/description **and**
  tenant scoping. This is the one most vendor-specific business models
  (catalog items, etc.) should use.

`core.User` carries an `organization` FK, and `core.Organization` is the
tenant model itself.

**Important:** the base classes only define the `organization` field —
they do not filter querysets by it. Every view/queryset touching a
tenant-scoped model must filter by `request.user.organization` itself (see
`core/views/user.py`); this template does not do it for you.

### Converting to a single-tenant (single vendor) app

Since every tenant-scoped model already carries an explicit `organization`
FK, going single-vendor is a matter of removing that layer rather than
rewriting models:

1. Drop the `organization` field from `core.User` (switch it to inherit
   `BaseModelWithUID` instead of `BaseModelWithOrg`) and remove the
   `Organization` model if you don't need it.
2. Swap `NameSlugDescriptionBaseModelWithOrg` for `NameSlugDescriptionBaseModel`
   on any app models that used it, and `BaseModelWithOrg` for
   `BaseModelWithUID`.
3. Remove the org-scoping filters you added to views/querysets.
4. Regenerate migrations.

## Environment variables

See `dot-env-example.txt` for the full list (`SECRET_KEY`, `DEBUG`,
`ALLOWED_HOSTS`, `CORS_ALLOWED_ORIGINS`, `DATABASE_URL`, etc.).

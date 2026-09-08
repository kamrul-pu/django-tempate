# ── Stage 1: Build dependencies ───────────────────────────────────────────────
FROM python:3.14-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /build

# Install build-time OS deps
RUN apt-get update && apt-get install -y --no-install-recommends \
        libpq-dev \
        gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps into a prefix dir (not system)
COPY ./requirements/dev.txt .
RUN pip install --upgrade pip \
    && pip install --prefix=/install --no-cache-dir -r dev.txt


# ── Stage 2: Runtime ──────────────────────────────────────────────────────────
FROM python:3.14-slim AS runtime

LABEL maintainer="django-template"

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/install/bin:$PATH" \
    PYTHONPATH="/install/lib/python3.14/site-packages"

WORKDIR /app

# Install only runtime OS deps (no gcc, no build tools)
RUN apt-get update && apt-get install -y --no-install-recommends \
        libpq5 \
    && rm -rf /var/lib/apt/lists/*

# Copy installed packages from builder
COPY --from=builder /install /install

# Copy application source
COPY ./app .

# Create a non-root user and set permissions
RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user \
    && mkdir -p /vol/web/media /vol/web/static \
    && chown -R django-user:django-user /vol /app \
    && chmod -R 755 /vol

USER django-user

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
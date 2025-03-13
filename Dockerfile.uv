FROM python:3.12-slim-bookworm

LABEL org.opencontainers.image.source=https://github.com/pvital/simple-flask
LABEL org.opencontainers.image.description="Simple Flask container"
LABEL org.opencontainers.image.licenses=MIT

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the project into the container
ADD . /app

# Sync the project into a new environment, using the frozen lockfile
WORKDIR /app
RUN uv sync --frozen

EXPOSE 5000
# Run the application
CMD ["uv", "run", "flask", "--app", "app", "run", "--host=0.0.0.0"]
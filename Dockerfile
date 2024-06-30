FROM python:3.11-slim

ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /home

RUN adduser --disabled-password --gecos '' pwuser

COPY requirements.txt /home/requirements.txt
COPY .env.example /home/.env

RUN apt-get update && \
    apt-get install -y --no-install-recommends libzbar0 && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /home/requirements.txt

ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright

RUN mkdir /ms-playwright /ms-playwright-agent && \
    cd /ms-playwright-agent && \
    pip install playwright && \
    python -m playwright install && \
    python -m playwright install-deps chromium && \
    python -m playwright install-deps firefox && \
    rm -rf /ms-playwright-agent && \
    rm -rf /ms-playwright/webkit-* && \
    chmod -R 777 /ms-playwright

COPY . /home/

ENV PYTEST_CACHE_DIR=/home/.pytest_cache

RUN mkdir -p /home/.pytest_cache && chmod -R 777 /home/.pytest_cache

USER pwuser

ENTRYPOINT ["python3", "-B", "-m", "pytest"]

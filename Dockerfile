# syntax=docker/dockerfile:1.6

FROM python:3.10.13-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    DJANGO_SETTINGS_MODULE=my_django_vue.settings \
    CHROME_BIN=/usr/bin/chromium \
    CHROME_DRIVER_PATH=/usr/bin/chromedriver

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
        chromium \
        chromium-driver \
        netcat-openbsd \
        ca-certificates \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . /app

RUN chmod +x wait-for-it.sh

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM python:3.8.13-bullseye

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./my_app /app
WORKDIR /app

# Shared prometheus metrics folder. This is configured in uwsgi.ini
RUN mkdir /app/metrics

RUN python manage.py migrate

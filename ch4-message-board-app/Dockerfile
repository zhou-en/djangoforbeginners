# Pull base image
FROM python:3.6-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV LOGGING_DIR=/var/log/ch4-message-board-app
RUN mkdir /var/log/ch4-message-board-app
RUN touch /var/log/ch4-message-board-app/app.log
RUN chmod 777 /var/log/ch4-message-board-app/app.log
RUN apt-get update -y
RUN apt-get install -y cron
# Set work directory
WORKDIR /code

# Install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /code/Pipfile

RUN pipenv install --deploy --system --skip-lock --dev

# Copy project
COPY . /code/

RUN set -xe \
    && python manage.py crontab add

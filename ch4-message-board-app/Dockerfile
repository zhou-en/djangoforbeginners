# Pull base image
FROM python:3.6-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /log
RUN touch /log/app.log
RUN chmod -R 777 /log
VOLUME /log


RUN apt-get update -y
RUN apt-get install cron rsyslog -y


#ADD crontab /etc/cron.d/crontab
#RUN chmod 0600 /etc/cron.d/crontab

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

# ENTRYPOINT ["/bin/sh", "-c", "service start cron"]

CMD [ "sh", "-c", "python /code/manage.py migrate --noinput && service cron start && python /code/manage.py runserver 0.0.0.0:8000"]
# ENTRYPOINT exec /code/start.sh

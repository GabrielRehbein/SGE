FROM python:3.11-slim

WORKDIR /sge

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update && apt -y install cron && apt -y install nano

COPY . .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY sge/cron /etc/cron.d/cron
RUN chmod 0644 /etc/cron.d/cron
RUN crontab /etc/cron.d/cron

EXPOSE 8000

CMD python manage.py migrate && python manage.py initadmin && python manage.py runserver 0.0.0.0:8000

FROM python:3.11-slim

WORKDIR /django-app
COPY . /django-app

RUN pip install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]
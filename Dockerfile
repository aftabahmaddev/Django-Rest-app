FROM python:3.6
ENV PYTHONUNBUFFERED 1
WORKDIR /restapi
COPY requirements.txt /restapi/

RUN pip install -r requirements.txt
COPY . /restapi

CMD python manage.py runserver 0.0.0.0:8000
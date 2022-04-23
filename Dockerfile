FROM python:3.9.7-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /smartdoor_host

RUN pip install --upgrade pip 
COPY requirements.txt /smartdoor_host/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /smartdoor_host/

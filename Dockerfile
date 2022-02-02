FROM python:3.9
WORKDIR /code
ENV FLASK_APP run.py
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

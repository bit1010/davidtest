FROM python:3

WORKDIR /app

COPY . .
RUN pip3 install -r requirements.txt

CMD gunicorn 'main:app' --bind=0.0.0.0:80

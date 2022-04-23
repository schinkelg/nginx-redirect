FROM python:3.6

COPY . .

RUN python nginx-redirect.py < example.txt

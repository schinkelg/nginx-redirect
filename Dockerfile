FROM python:3.12-slim

COPY . .

RUN python nginx-redirect.py < example.txt

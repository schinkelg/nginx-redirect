FROM python:3.12-slim

COPY nginx-redirect.py .
COPY example.txt .

RUN python nginx-redirect.py < example.txt

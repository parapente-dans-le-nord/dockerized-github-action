FROM python:3.8-slim

WORKDIR /app

COPY entrypoint.sh .
COPY myscript.py .

ENTRYPOINT ["/app/entrypoint.sh"]

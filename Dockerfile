FROM python:3.8-slim

WORKDIR /app
COPY myscript.py .

ENTRYPOINT ["python", "/app/myscript.py"]

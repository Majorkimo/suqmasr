FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

COPY . .

# /data wird von Coolify als persistentes Volume gemountet
RUN mkdir -p /data/uploads

ENV UPLOAD_FOLDER=/data/uploads
ENV DB_PATH=/data/marketplace.db

EXPOSE 5055

CMD ["gunicorn", "--bind", "0.0.0.0:5055", "--workers", "2", "--timeout", "120", "app:app"]

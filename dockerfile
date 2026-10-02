# Multi-stage build for lightweight container packaging
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EX-POSE 8501 8000

# Default command can be overridden by docker-compose or Kubernetes manifests
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

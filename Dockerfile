# -----------------------------
# Base image (light but compatible)
# -----------------------------
FROM python:3.10-slim

# -----------------------------
# System dependencies (REQUIRED)
# -----------------------------
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
# Working directory
# -----------------------------
WORKDIR /app

# -----------------------------
# Copy requirements first (cache)
# -----------------------------
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# -----------------------------
# Copy application code
# -----------------------------
COPY . .

# -----------------------------
# DO NOT SET PORT
# DO NOT OVERRIDE CMD
# Render already runs uvicorn automatically
# -----------------------------

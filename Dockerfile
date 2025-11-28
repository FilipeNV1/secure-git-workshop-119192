# Use official Python image
FROM python:3.11-slim

WORKDIR /app

COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./

# Default command (can be overridden)
CMD ["python3", "get_wheater.py", "Lisbon"]

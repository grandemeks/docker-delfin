# Use slim Python image as base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements file
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire application (including app.py, .env, etc.)
COPY . .

# Expose the port the app runs on
EXPOSE 8080

# Start the app
CMD ["python", "app.py"]



# Use slim Python image as base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy flask app into the container
COPY app.py .

#Instal required Python packages directly
RUN pip install Flask psycopg2-binary

# Expose the port the app runs on
EXPOSE 8080


# Start the app
CMD ["python", "app.py"]

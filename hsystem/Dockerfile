# Use the official Python base image
FROM python:3.11.0a1-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

#upgrade pip
RUN pip install --upgrade pip

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Install SQLite
RUN apt-get update && apt-get install -y sqlite3

# Create a directory for the SQLite database
RUN mkdir /app/db

# Set the command to create and migrate the database
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
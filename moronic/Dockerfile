# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/requirements.txt

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to /app
COPY . /app

# Set environment variables
ENV FLASK_APP=App.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port 5000 for the Flask app
EXPOSE 5000

# Run create_tables.py to create the database tables
# RUN python create_tables.py
# RUN apk add --no-cache iputils
RUN apt-get update && apt-get install -y iputils-ping
# RUN python create_tables.py

# Run the application
CMD ["flask", "run"]

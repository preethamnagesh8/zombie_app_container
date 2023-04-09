# Base image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the requirements
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Run migrations
RUN python manage.py migrate

# Expose the application port
EXPOSE 8000

# Start the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app/quera-cashing-project

# Install dependencies
COPY requirements.txt /app/quera-cashing-project/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the current directory contents into the container at /app/quera-cashing-project
COPY . /app/quera-cashing-project/

# Expose the port that Django will run on
EXPOSE 8000

# Run the command to start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Use an official Python runtime as a parent image
FROM python:3.11.4-slim-buster


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Set the working directory in the container
WORKDIR /quera-cashing-project

# Install dependencies
COPY requirements.txt /app/quera-cashing-project/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the current directory contents into the container at /app/quera-cashing-project
COPY . /app/quera-cashing-project/

# Expose the port that Django will run on
EXPOSE 8000

# Run the command to start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


#
## pull official base image
#FROM python:3.11.4-slim-buster
#
## set work directory
#WORKDIR /quera-cashing-project
#
#
## set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
## install system dependencies
#RUN apt-get update
#
#RUN pip install --upgrade pip
#COPY ./requirements.txt .
#RUN pip install -r requirements.txt
#
#COPY . .
#
#EXPOSE 8000
#
## Run the command to start the Django development server
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# Use the official Python 3.8 slim image as the base image
FROM python:3.8-slim

# Set the working directory in the container to /app
WORKDIR /

RUN apt-get update

# Create the virtual environment
RUN python -m venv /opt/venv

# Set up the path to the venv
ENV PATH='/opt/venv/bin:$PATH'

# Copy the project files to the container
COPY . .

# Install the dependencies specified in the requirements file
RUN pip install -r requirements.txt

# Command to run the application when the container starts
EXPOSE 5000
CMD ["python", "main.py"]

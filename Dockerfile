# Use the official Debian based Python 3.8 image as the base image
FROM python:3.8-buster

# Set the working directory in the container to /app
WORKDIR /app

# Update the package manager and install necessary packages
RUN apt-get update && apt-get install -y \
    coreutils \
    && rm -rf /var/lib/apt/lists/*

# Create the virtual environment
RUN python -m venv /opt/venv

# Set up the path to the venv
ENV PATH='/opt/venv/bin:$PATH'

# Copy the project files to the container
COPY . .

# Install the dependencies specified in the requirements file
RUN pip install -r requirements.txt

# Expose the port on which the application will run
EXPOSE 5000

# Command to run the application when the container starts
CMD ["python", "main.py"]

# Define the steps to create a base image and run a container in working directory 
FROM python:3.9-slim-buster

WORKDIR /app
# Copy requirement.txt inside this image from the local directory
COPY requirements.txt .
# Installing packages inside requirement.txt in order for the application to run
RUN pip3 install --no-cache-dir -r requirements.txt
# Copy everything else inside the local directory
COPY . .
# Set the environment variables for flask app
ENV FLASK_RUN_HOST=0.0.0.0
# Expose the port on which the flask app will run
EXPOSE 5000
# Start the flask app when the container is run
CMD ["flask", "run"]
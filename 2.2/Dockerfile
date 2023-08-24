# Base image
FROM python:3.9-slim

# Set workdir
WORKDIR /app

# Copy app files
COPY . /app

# Install scanner app as python package
# Install dependencied
RUN apt update
RUN apt install nmap -y
RUN pip install --no-cache-dir /app/
RUN rm -rf /app

# Run application
ENTRYPOINT ["scanner"]
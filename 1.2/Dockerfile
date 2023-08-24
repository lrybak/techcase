# Base image
FROM python:3.9-slim

# Set workdir
WORKDIR /app

# Copy app files
COPY . /app

# Install getweather app as pip packaged app
RUN pip install --no-cache-dir /app/
RUN rm -rf /app

# Run application
CMD ["getweather"]
# Base image
FROM python:3.9-slim

ENV WORKDIR=/app
ENV VENV=${WORKDIR}/venv
ENV USER=user
ENV UID=1001

# Create user
RUN useradd -u ${UID} -U ${USER}

# Create a virtual environment
RUN python3 -m venv ${VENV}

# Activate the virtual environment
ENV PATH="$VENV/bin:$PATH"

# Set workdir
WORKDIR ${WORKDIR}

# Copy app files
COPY . ${WORKDIR}

# Install scanner app as python package
# Install dependencies
RUN apt update
RUN apt install nmap -y
RUN pip install --upgrade pip
RUN pip install --no-cache-dir ${WORKDIR}

USER ${USER}

# Run application
ENTRYPOINT ["scanner"]
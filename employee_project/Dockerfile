# Base image
FROM python:3.11-slim

# Environment settings
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set working directory
WORKDIR /code

# System dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev gcc curl netcat && \
    rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY employee_project/requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r employee_project/requirements.txt

# Copy project files
COPY . /code/

# Copy and set entrypoint script
COPY ./employee_project/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expose Render-compatible port
EXPOSE 10000

# Run entrypoint which will call gunicorn
ENTRYPOINT ["/entrypoint.sh"]

FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install system dependencies
# Install system dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    netcat-openbsd \
    curl \
    ca-certificates \
    gnupg && \
    rm -rf /var/lib/apt/lists/*


# Install Python dependencies
COPY ./employee_project/requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project files
COPY . /code/

# Add entrypoint
# Add entrypoint
COPY ./employee_project/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Expose port and start server
EXPOSE 10000
ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "employee_project.wsgi:application", "--bind", "0.0.0.0:10000"]


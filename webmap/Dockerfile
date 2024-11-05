FROM python:3.10-bullseye

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libproj-dev \
    libpq-dev \
    libgeos-dev \
   # libpq-dev \
    gdal-bin \
    libgdal-dev \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables for GDAL
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal
ENV PATH="/usr/bin:${PATH}"

# Update pip
RUN pip install --upgrade pip

# Install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Copy the entry point script
COPY docker-entrypoint.sh /app/docker-entrypoint.sh

# Make the entry point script executable
RUN chmod +x /app/docker-entrypoint.sh

# Expose the port uWSGI will run on
EXPOSE 8000

# Set the entry point
ENTRYPOINT ["/app/docker-entrypoint.sh"]

# Run uWSGI
CMD ["uwsgi", "--ini", "/app/uwsgi.ini"]
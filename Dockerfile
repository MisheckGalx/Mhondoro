# Use official Python image as base
FROM python:3.11

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    FLASK_APP=run.py \
    FLASK_ENV=production

# Set working directory inside the container
WORKDIR /app

# Copy project files
COPY . /app/

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose Flask port
EXPOSE 5000

# Run Gunicorn server
CMD ["gunicorn", "-b", "0.0.0.0:5000", "run:app"]

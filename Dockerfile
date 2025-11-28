# Use an official lightweight Python image
FROM python:3.10-slim

# Create directory for the app
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the full project into the container
COPY . .

# Expose whatever port your Flask/FastAPI app uses
EXPOSE 5000

# Run the app
CMD ["python", "src/app.py"]

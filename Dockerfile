# Dockerfile
FROM python:3.10-slim

# Set working directory
#WORKDIR /app

# Install Streamlit
COPY app/requirements.txt .
RUN pip install -r requirements.txt

# Copy the app code
COPY app/ .

# Expose Streamlit default port
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Command to run the app
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]

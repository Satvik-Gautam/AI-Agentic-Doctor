# Use the official lightweight image 
FROM python:3.10-slim

# copy application code here 

COPY . /app/

# Set Working directory

WORKDIR /app

#Install required dependence

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libportaudio2 \
    portaudio19-dev \
    gcc \
    libc-dev \
    make \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

# Expose the required port
EXPOSE 7860

# Start the code INSIDE the docker container
CMD ["sh", "-c", "python app.py"]
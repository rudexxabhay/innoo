FROM nikolaik/python-nodejs:python3.10-nodejs19
FROM node:14


COPY . /app/
WORKDIR /app/
COPY package*.json ./


RUN npm install
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
    

RUN pip3 install --no-cache-dir -U -r requirements.txt


COPY . . 


CMD bash start

# Use an official node image as a base image
FROM node:14

# Set the working directory
WORKDIR /app


RUN npm install

# Copy package.json and package-lock.json
COPY package*.json ./


# Copy the rest of the application code
COPY . .

# Specify the command to run your application
CMD bash start

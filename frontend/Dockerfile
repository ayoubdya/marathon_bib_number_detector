# Use the official Node.js image from the Docker Hub
FROM node:18-alpine

# Set the working directory
WORKDIR /app

# Copy the package.json and package-lock.json to the container
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the rest of the application code to the container
COPY . .

# Build the React application
RUN npm run build

# Install a lightweight web server to serve the React application
RUN npm install -g serve

# Expose the port that the web server runs on
EXPOSE 3000

# Serve the built React application
CMD ["serve", "-s", "build"]
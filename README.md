# AI Task

This project is a FastAPI application designed to provide a RESTful API service. It includes a `Dockerfile` for easy setup and deployment using Docker.

## Requirements

To run this project, you will need:

- Docker installed on your machine. You can download Docker [here](https://www.docker.com/products/docker-desktop).

# Docker Setup
To run the application using Docker, follow these steps:

git clone https://github.com/your-username/your-repository.git

cd your-repository

docker build -t fastapi-app .

docker run -d --name myfastapiapp -p 8000:8000 fastapi-app

After running the above command, the API should be accessible at http://localhost:8000

# API Endpoints

http://localhost:8000/api/rephrase
http://localhost:8000/api/generate

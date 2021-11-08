#!/bin/bash
# Application environment variables
export JWT_SECRET=secret

echo ====================== Starting Containers ======================
docker rm test-mongo-container
docker rm test-rabbitmq-container
docker run --name test-mongo-container -p 27017:27107 -d mongo:latest
docker run --name test-rabbitmq-container -p 5673:5672 -p 15672:15672 -d rabbitmq:3
echo ====================== Starting Tests ======================
#Flask environment variables
export DEPLOY=test
export FLASK_ENV=development
python -m pytest -s
echo ====================== Stopping Containers ======================
docker stop test-mongo-container
docker stop test-rabbitmq-container
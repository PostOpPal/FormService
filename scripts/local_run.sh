#!/bin/bash
#Application variables 
export JWT_SECRET=secret

echo ====================== Starting Containers ======================
docker rm --volumes local-mongo-container
docker rm --volumes local-rabbitmq-container
docker run --name local-mongo-container -p 27017:27017 -d mongo:latest
docker run --name local-rabbitmq-container -p 5672:5672 -p 15672:15672 -d rabbitmq:3
echo ====================== Starting App ======================
#These variables are just for configuring flask
#export DEPLOY=local
#export FLASK_ENV=development
#export FLASK_APP=app.py
uvicorn app:app --reload
echo ====================== Stopping Containers ======================
docker stop local-mongo-container
docker stop local-rabbitmq-container
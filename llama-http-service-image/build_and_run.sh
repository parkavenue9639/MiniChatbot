#!/bin/bash

# 设置变量
IMAGE_NAME="llama-http-service"
CONTAINER_NAME="llama-api"
MODEL_PATH="/Users/luchong/PycharmProjects/MiniChatbot/LM_models"

# 检查镜像是否存在
if [[ "$(docker images -q $IMAGE_NAME 2> /dev/null)" == "" ]]; then
    echo "Docker image '$IMAGE_NAME' not found. Building..."
    docker build -t $IMAGE_NAME .
else
    echo "Docker image '$IMAGE_NAME' already exists. Skipping build."
fi

# 检查是否已有同名容器在运行或存在
if [[ "$(docker ps -aq -f name=^/${CONTAINER_NAME}$)" ]]; then
    echo "Container '$CONTAINER_NAME' already exists. Removing..."
    docker rm -f $CONTAINER_NAME
fi

# 启动容器
echo "Starting container '$CONTAINER_NAME'..."
docker run -d --name $CONTAINER_NAME -p 8001:8000 -v "$MODEL_PATH":/app/model $IMAGE_NAME

# 输出访问信息
echo "Container '$CONTAINER_NAME' started. Access the API at: http://localhost:8001"
#!/bin/bash

# 项目路径设置（可选，根据实际情况修改）
PROJECT_ROOT="$(cd "$(dirname "$0")"; pwd)"
BACKEND_DIR="$PROJECT_ROOT/backend"
FRONTEND_DIR="$PROJECT_ROOT/frontend"
MICROSERVICE_DIR="$PROJECT_ROOT/llama-http-service-image"

# 启动 Docker 微服务
echo "🐳 启动 Docker 微服务 llama-api..."
cd "$MICROSERVICE_DIR"
./build_and_run.sh
cd "$PROJECT_ROOT"

# 启动 Django 后端
echo "🚀 启动 Django 后端服务..."
cd "$BACKEND_DIR"
# source venv/bin/activate  # 如有虚拟环境
python manage.py runserver &
BACKEND_PID=$!

# 启动 Vue 前端
echo "🚀 启动 Vue 前端服务..."
cd "$FRONTEND_DIR"
npm install  # 如依赖已安装，可注释
npm run dev &
FRONTEND_PID=$!

# 返回项目根目录
cd "$PROJECT_ROOT"

# 等待服务运行
echo "✅ 所有服务已启动："
echo "  - Django: http://127.0.0.1:8000"
echo "  - Vue:  http://localhost:5173"
echo "  - 微服务 llama-api: http://localhost:8001"
echo "按 Ctrl+C 停止服务..."
wait $BACKEND_PID $FRONTEND_PID
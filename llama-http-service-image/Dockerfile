# 使用 llama-cpp-python 官方镜像作为基础镜像（已含编译库）
FROM ghcr.io/abetlen/llama-cpp-python:latest

# 安装 FastAPI 和 Uvicorn（已有 pip3）
RUN pip3 install --no-cache-dir fastapi uvicorn

# 创建一个新的目录来放你的 FastAPI 服务，避免污染 /app 根目录
WORKDIR /app/http_service

# 拷贝 FastAPI 应用代码
COPY app.py .

# 设置共享库环境变量（可选但推荐，确保 llama_cpp 能找到 libllama.so）
ENV LLAMA_CPP_LIB=/app/build/libllama.so

# 启动服务（监听 0.0.0.0，端口8000）
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
# MiniChatbot project

这是一个基于 Vue3 + Django 的简易聊天机器人项目，旨在实现一个问答机器人的完整工作流程。当前版本关注核心问答功能，暂不包括多用户管理、权限控制等复杂特性。

This is a simple chatbot project based on Vue3 + Django, designed to implement the full workflow of a Q&A chatbot. The current version focuses on core question-answering functionality and excludes complex features such as multi-user support or permission control.

# 项目结构 | Project Architecture
前端 | Frontend: Vue3  
后端 | Backend: Django   
模型服务 | Model Deployment: llama.cpp + FastAPI + Docker

# 使用说明 | Usage Instructions
## 依赖安装 | Dependencies
上述所有的框架环境
Ensure the following frameworks and tools are installed and configured properly in your environment:
Node.js & npm/yarn (for Vue3)  
Python (Django, FastAPI .etc)  
Docker  

## 启动项目 | Running the Project
运行start.sh脚本即可  
该脚本将会自动启动前后端及模型服务。
This script will automatically start the frontend, backend, and model services.

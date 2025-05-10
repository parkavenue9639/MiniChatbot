# 导入必要的库
from fastapi import FastAPI  # 导入FastAPI框架，用于创建API服务
from pydantic import BaseModel  # 导入Pydantic的BaseModel，用于数据验证和序列化
from llama_cpp import Llama  # 导入Llama类，用于加载和运行LLaMA模型

# 创建FastAPI应用实例
app = FastAPI()

# 定义模型路径常量
# 使用TinyLlama模型，这是LLaMA的较小版本，适合资源有限的环境
# 使用GGUF格式，这是一种优化的模型格式，适合高效推理
mini_model = "/app/model/tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf"

# 初始化Llama模型
# model_path: 指定模型文件的路径
# n_ctx: 设置上下文窗口大小为2048个token，决定了模型能记住的对话历史长度
llama_model = Llama(model_path=mini_model, n_ctx=2048)

# 定义请求体数据模型
class ChatInput(BaseModel):
    prompt: str  # 用户输入的提示文本，必填字段
    n_predict: int = 50  # 预测的最大token数量，默认值为50

# 定义根路由处理函数
@app.get("/")
async def root():
    """
    根路由处理函数，返回欢迎信息
    返回: 包含欢迎信息的JSON对象
    """
    return {"message": "Welcome to the Llama API"}

# 定义预测路由处理函数
@app.post("/predict/")
async def predict(input: ChatInput):
    """
    处理文本生成请求的端点
    参数:
        input: 包含prompt和n_predict的ChatInput对象
    返回:
        包含模型生成的文本响应的JSON对象
    """
    # 调用LLaMA模型进行推理
    # 使用用户提供的prompt作为输入
    # max_tokens参数限制生成的最大token数量
    output = llama_model(input.prompt, max_tokens=input.n_predict)
    
    # 从输出中提取生成的文本并返回
    # output["choices"][0]["text"]包含了模型生成的实际文本内容
    return {"response": output["choices"][0]["text"]}
# DeepSeek Calculator Agent

一个基于DeepSeek API的智能计算器代理，支持自然语言数学计算。

## 功能特点

- 🧮 支持基本数学运算：加减乘除、幂运算、开方
- 🤖 自然语言交互，理解中文数学问题
- 🔧 完整的工具调用系统
- 📊 详细的思考、行动、观察过程展示
- 🔄 两种API调用方式：OpenAI SDK 和 原生 requests

## 支持的运算

- 加法 (add)
- 减法 (subtract) 
- 乘法 (multiply)
- 除法 (divide)
- 幂运算 (power)
- 平方根 (sqrt)

## 安装

1. 克隆项目
```bash
git clone https://github.com/your-username/deepseek-calculator-agent.git
cd deepseek-calculator-agent
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置环境变量
复制 `.env.example` 到 `.env` 并填入你的 DeepSeek API 密钥：
```bash
cp .env.example .env
```

编辑 `.env` 文件：
```
DEEPSEEK_API_KEY=your_deepseek_api_key_here
DEEPSEEK_BASE_URL=https://api.deepseek.com/v1
DEEPSEEK_MODEL=deepseek-chat
```

## 使用方法

### OpenAI SDK 版本
```bash
python calculator_agent_openai.py
```

### Requests 版本
```bash
python calculator_agent_requests.py
```

## 示例对话

```
你: 计算 25 + 17
============================================================
🧠 用户输入: 计算 25 + 17
💭 思考: 分析用户问题，准备调用DeepSeek API...
📤 行动: 发送请求到 deepseek-chat
📥 观察: 收到API响应
💭 思考: AI决定使用工具来解决问题
🔧 行动 1: 调用工具 'add' 参数: {'a': 25, 'b': 17}
📊 观察 1: 工具执行结果 = 42
💭 思考: 工具执行完成，请求AI整理最终答案...
📤 行动: 发送工具结果给AI进行总结
📥 观察: 收到AI的最终回复
✅ 结果: 25 + 17 = 42
============================================================
```

## 项目结构

```
deepseek-calculator-agent/
├── calculator_tools.py          # 计算器工具定义
├── calculator_agent_openai.py   # OpenAI SDK版本
├── calculator_agent_requests.py # Requests版本
├── requirements.txt             # 依赖包
├── .env.example                # 环境变量示例
├── .gitignore                  # Git忽略文件
└── README.md                   # 项目说明
```

## 命令

- `quit` - 退出程序
- `reset` - 重置对话历史

## 技术栈

- Python 3.7+
- OpenAI SDK
- Requests
- DeepSeek API
- python-dotenv

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！
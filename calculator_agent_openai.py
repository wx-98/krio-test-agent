"""
使用OpenAI SDK调用DeepSeek API的计算器Agent
"""
import os
import json
from typing import List, Dict, Any
from openai import OpenAI
from dotenv import load_dotenv
from calculator_tools import CALCULATOR_TOOLS, execute_tool

# 加载环境变量
load_dotenv()

class CalculatorAgentOpenAI:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            base_url=os.getenv("DEEPSEEK_BASE_URL")
        )
        self.model = os.getenv("DEEPSEEK_MODEL")
        self.messages = []
    
    def add_message(self, role: str, content: str):
        """添加消息到对话历史"""
        self.messages.append({"role": role, "content": content})
    
    def chat(self, user_input: str) -> str:
        """与计算器agent对话"""
        print(f"\n{'='*60}")
        print(f"🧠 用户输入: {user_input}")
        
        # 添加用户消息
        self.add_message("user", user_input)
        
        try:
            print(f"💭 思考: 分析用户问题，准备调用DeepSeek API...")
            print(f"📤 行动: 发送请求到 {self.model}")
            
            # 调用DeepSeek API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                tools=CALCULATOR_TOOLS,
                tool_choice="auto"
            )
            
            message = response.choices[0].message
            print(f"📥 观察: 收到API响应")
            
            # 如果有工具调用
            if message.tool_calls:
                print(f"💭 思考: AI决定使用工具来解决问题")
                if message.content:
                    print(f"💬 AI回应: {message.content}")
                
                # 添加带有工具调用的助手消息
                self.messages.append({
                    "role": "assistant",
                    "content": message.content,
                    "tool_calls": [
                        {
                            "id": tool_call.id,
                            "type": "function",
                            "function": {
                                "name": tool_call.function.name,
                                "arguments": tool_call.function.arguments
                            }
                        } for tool_call in message.tool_calls
                    ]
                })
                
                # 执行工具调用
                for i, tool_call in enumerate(message.tool_calls, 1):
                    function_name = tool_call.function.name
                    function_args = json.loads(tool_call.function.arguments)
                    
                    print(f"🔧 行动 {i}: 调用工具 '{function_name}' 参数: {function_args}")
                    
                    # 执行工具
                    result = execute_tool(function_name, function_args)
                    print(f"📊 观察 {i}: 工具执行结果 = {result}")
                    
                    # 添加工具结果
                    self.messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": str(result)
                    })
                
                print(f"💭 思考: 工具执行完成，请求AI整理最终答案...")
                print(f"📤 行动: 发送工具结果给AI进行总结")
                
                # 再次调用API获取最终回复
                final_response = self.client.chat.completions.create(
                    model=self.model,
                    messages=self.messages
                )
                
                final_message = final_response.choices[0].message.content
                print(f"📥 观察: 收到AI的最终回复")
                print(f"✅ 结果: {final_message}")
                
                self.add_message("assistant", final_message)
                return final_message
            else:
                # 没有工具调用，直接返回回复
                print(f"💭 思考: AI直接回答，无需使用工具")
                print(f"✅ 结果: {message.content}")
                
                self.add_message("assistant", message.content)
                return message.content
                
        except Exception as e:
            error_msg = f"调用API时出错: {str(e)}"
            print(f"❌ 错误: {error_msg}")
            return error_msg
    
    def reset_conversation(self):
        """重置对话历史"""
        self.messages = []

def main():
    """主函数 - 交互式计算器"""
    agent = CalculatorAgentOpenAI()
    
    print("🧮 DeepSeek计算器Agent (OpenAI SDK版本)")
    print("输入数学问题，我会帮你计算！输入 'quit' 退出，'reset' 重置对话")
    print("-" * 50)
    
    while True:
        try:
            user_input = input("\n你: ").strip()
            
            if user_input.lower() == 'quit':
                print("再见！")
                break
            elif user_input.lower() == 'reset':
                agent.reset_conversation()
                print("对话已重置")
                continue
            elif not user_input:
                continue
            
            response = agent.chat(user_input)
            print(f"{'='*60}")
            
        except KeyboardInterrupt:
            print("\n\n再见！")
            break
        except Exception as e:
            print(f"发生错误: {str(e)}")

if __name__ == "__main__":
    main()
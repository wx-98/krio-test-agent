"""
计算器工具定义
"""
import json
from typing import Dict, Any, List

def add(a: float, b: float) -> float:
    """加法运算"""
    return a + b

def subtract(a: float, b: float) -> float:
    """减法运算"""
    return a - b

def multiply(a: float, b: float) -> float:
    """乘法运算"""
    return a * b

def divide(a: float, b: float) -> float:
    """除法运算"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

def power(a: float, b: float) -> float:
    """幂运算"""
    return a ** b

def sqrt(a: float) -> float:
    """平方根运算"""
    if a < 0:
        raise ValueError("负数不能开平方根")
    return a ** 0.5

# 工具函数映射
TOOL_FUNCTIONS = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "power": power,
    "sqrt": sqrt
}

# OpenAI格式的工具定义
CALCULATOR_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "add",
            "description": "执行两个数的加法运算",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "第一个数"
                    },
                    "b": {
                        "type": "number", 
                        "description": "第二个数"
                    }
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "subtract",
            "description": "执行两个数的减法运算",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "被减数"
                    },
                    "b": {
                        "type": "number",
                        "description": "减数"
                    }
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function", 
        "function": {
            "name": "multiply",
            "description": "执行两个数的乘法运算",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "第一个数"
                    },
                    "b": {
                        "type": "number",
                        "description": "第二个数"
                    }
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "divide", 
            "description": "执行两个数的除法运算",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "被除数"
                    },
                    "b": {
                        "type": "number",
                        "description": "除数"
                    }
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "power",
            "description": "执行幂运算",
            "parameters": {
                "type": "object", 
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "底数"
                    },
                    "b": {
                        "type": "number",
                        "description": "指数"
                    }
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "sqrt",
            "description": "计算平方根",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "number",
                        "description": "要开平方根的数"
                    }
                },
                "required": ["a"]
            }
        }
    }
]

def execute_tool(tool_name: str, arguments: Dict[str, Any]) -> Any:
    """执行工具函数"""
    if tool_name not in TOOL_FUNCTIONS:
        raise ValueError(f"未知的工具: {tool_name}")
    
    func = TOOL_FUNCTIONS[tool_name]
    try:
        return func(**arguments)
    except Exception as e:
        return f"执行错误: {str(e)}"
import json
from groq import Groq
from tools import fahrenheit_para_celsius, celsius_para_fahrenheit
from dotenv import load_dotenv

load_dotenv()

client = Groq()

tools = [
    {
        "type": "function",
        "function": {
            "name": "celsius_para_fahrenheit",
            "description": "Converte uma temperatura de celsius para fahrenheit",
            "parameters": {
                "type": "object",
                "properties": {
                    "temperatura_original": {"type": "number", "description": "Temperatura Original"}
                },
                "required": ["temperatura_original"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "fahrenheit_para_celsius",
            "description": "Converte uma temperatura de fahrenheit para celsius",
            "parameters": {
                "type": "object",
                "properties": {
                    "temperatura_original": {"type": "number", "description": "Temperatura Original"}
                },
                "required": ["temperatura_original"]
            }
        }
    }
]

def perguntar(pergunta: str):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "Você é um assistente que decide qual função usar."},
            {"role": "user", "content": pergunta}
        ],
        tools=tools,
        tool_choice="auto",
        temperature=0
    )

    message = response.choices[0].message

    if message.tool_calls:
        tool_call = message.tool_calls[0]
        tool_name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)

        print(f"Tool chamada: {tool_name}")
        print(f"Argumentos: {args}")

        if tool_name == "celsius_para_fahrenheit":
            return celsius_para_fahrenheit(**args)
        
        if tool_name == "fahrenheit_para_celsius":
            return fahrenheit_para_celsius(**args)

    return message.content


print(perguntar("Converter 30 graus Celsius para Fahrenheit"))
print(perguntar("Quanto é 80F em Celsius?"))
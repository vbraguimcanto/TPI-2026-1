import json
from groq import Groq
from tools import somar, multiplicar
from dotenv import load_dotenv

load_dotenv()

client = Groq()

tools = [
    {
        "type": "function",
        "function": {
            "name": "somar",
            "description": "Soma dois números (a + b)",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "integer", "description": "Primeiro valor"},
                    "b": {"type": "integer", "description": "Segundo valor"}
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "multiplicar",
            "description": "Multiplica dois números (a * b)",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {"type": "integer", "description": "Primeiro valor"},
                    "b": {"type": "integer", "description": "Segundo valor"}
                },
                "required": ["a", "b"]
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

        if tool_name == "somar":
            return somar(**args)

        if tool_name == "multiplicar":
            return multiplicar(**args)

    return message.content


print(perguntar("Quanto é 7 mais 3?"))
print(perguntar("Quanto é 6 vezes 4?"))
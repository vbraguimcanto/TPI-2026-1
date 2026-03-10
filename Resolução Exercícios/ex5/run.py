import json
from groq import Groq
from tools import consultar_estoque
from dotenv import load_dotenv

load_dotenv()

client = Groq()

tools = [
    {
        "type": "function",
        "function": {
            "name": "consultar_estoque",
            "description": "Busca a quantidade disponível no estoque de acordo com o nome do produto",
            "parameters": {
                "type": "object",
                "properties": {
                    "nome_produto": {"type": "string", "description": "Nome do Produto"}
                },
                "required": ["nome_produto"]
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

        if tool_name == "consultar_estoque":
            return consultar_estoque(**args)
        

    return message.content


print(perguntar("Tem notebook em estoque?"))
print(perguntar("Quantos mouses temos?"))
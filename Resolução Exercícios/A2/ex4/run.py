import json
from groq import Groq
from tools import buscar_produto
from dotenv import load_dotenv

load_dotenv()

client = Groq()

tools = [
    {
        "type": "function",
        "function": {
            "name": "buscar_produto",
            "description": "Busca as informações do produto pelo nome",
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

        if tool_name == "buscar_produto":
            return buscar_produto(**args)
        

    return message.content


print(perguntar("Qual o preço do notebook?"))
print(perguntar("Quanto custa um mouse?"))
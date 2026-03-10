import json
from groq import Groq
from tools import buscar_clima
from dotenv import load_dotenv

load_dotenv()

client = Groq()

tools = [
    {
        "type": "function",
        "function": {
            "name": "buscar_clima",
            "description": "Busca o clima da cidade de acordo com o nome dela (PASSE O NOME DA CIDADE SEM ACENTUAÇÃO, SOMENTE COM ESPAÇOS)",
            "parameters": {
                "type": "object",
                "properties": {
                    "cidade": {"type": "string", "description": "Nome da cidade"}
                },
                "required": ["cidade"]
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

        if tool_name == "buscar_clima":
            return buscar_clima(**args)
        

    return message.content


print(perguntar("Como está o clima em Bauru?"))
print(perguntar("Qual a temperatura em Curitiba?"))
print(perguntar("Como está o tempo em São Paulo?"))
import json
from groq import Groq
from tools import listar_eventos, criar_evento
from dotenv import load_dotenv

load_dotenv()

client = Groq()

tools = [
    {
        "type": "function",
        "function": {
            "name": "criar_evento",
            "description": "Cria um novo evento",
            "parameters": {
                "type": "object",
                "properties": {
                    "data": {"type": "string", "description": "Data do evento"},
                    "titulo": {"type": "string", "description": "Título do evento"}
                },
                "required": ["data", "titulo"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "listar_eventos",
            "description": "Lista todos os eventos existentes",
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
        args = json.loads(tool_call.function.arguments) or {}

        print(f"Tool chamada: {tool_name}")
        print(f"Argumentos: {args}")

        if tool_name == "listar_eventos":
            return listar_eventos(**args)
        
        if tool_name == "criar_evento":
            return criar_evento(**args)
        

    return message.content


print(perguntar("Criar evento reunião amanhã"))
print(perguntar("Mostrar meus eventos"))
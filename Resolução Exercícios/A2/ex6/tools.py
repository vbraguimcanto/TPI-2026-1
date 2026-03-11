import os

ARQUIVO = os.path.join(os.path.dirname(__file__), "eventos.txt")

def criar_evento(titulo, data):
    with open(ARQUIVO, "a", encoding="utf-8") as f:
        f.write(f"{data} - {titulo}\n")
    return {"mensagem": f"Evento '{titulo}' criado para {data}."}

def listar_eventos():
    if not os.path.exists(ARQUIVO):
        return {"eventos": []}
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        eventos = [linha.strip() for linha in f.readlines() if linha.strip()]
    return {"eventos": eventos}
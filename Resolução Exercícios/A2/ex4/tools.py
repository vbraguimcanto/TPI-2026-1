produtos = {
    "notebook": 4500,
    "mouse": 80,
    "teclado": 150
}

def buscar_produto(nome_produto):
    nome = nome_produto.lower()
    if nome in produtos:
        return {"produto": nome, "preco": produtos[nome]}
    return {"erro": f"Produto '{nome_produto}' não encontrado."}

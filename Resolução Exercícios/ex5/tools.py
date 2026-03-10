estoque = {
    "notebook": 5,
    "mouse": 20,
    "teclado": 8
}
def consultar_estoque(nome_produto):
    nome = nome_produto.lower()
    if nome in estoque:
        return {"produto": nome, "quantidade": estoque[nome]}
    return {"erro": f"Produto '{nome_produto}' não encontrado."}

clima = {
    "sao paulo": "24°C e nublado",
    "bauru": "30°C e ensolarado",
    "curitiba": "18°C e chuvoso"
}
def buscar_clima(cidade):
    city = cidade.lower()
    if city in clima:
        return {"cidade": city, "clima": clima[city]}
    return {"erro": f"Cidade '{city}' não encontrada."}

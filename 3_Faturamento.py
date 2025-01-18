import json


faturamento = {
    "dias": [
        {"dia": 1, "valor": 100.0},
        {"dia": 2, "valor": 200.0},
        {"dia": 3, "valor": 0.0},
        {"dia": 4, "valor": 300.0},

    ]
}

def calcular_faturamento(dados):
    valores = [dia["valor"] for dia in dados if dia["valor"] > 0]
    menor = min(valores)
    maior = max(valores)
    media = sum(valores) / len(valores)
    dias_acima_media = sum(1 for valor in valores if valor > media)

    return menor, maior, dias_acima_media

menor, maior, dias_acima_media = calcular_faturamento(faturamento["dias"])
print(f"Menor valor: R${menor:.2f}")
print(f"Maior valor: R${maior:.2f}")
print(f"Dias acima da média: {dias_acima_media}")

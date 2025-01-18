data_path = "desafio/dados.json"
import json

with open(data_path, "r") as file:
    dados = json.load(file)

valores = [d["valor"] for d in dados if d["valor"] > 0]

menor_valor = min(valores)
maior_valor = max(valores)
média = sum(valores) / len(valores)
dias_acima_da_média = len([v for v in valores if v > média])

print(f"Menor valor de faturamento: {menor_valor}")
print(f"Maior valor de faturamento: {maior_valor}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_média}")

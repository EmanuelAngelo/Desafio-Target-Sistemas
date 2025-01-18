def inverter_string(string):
    invertida = ""
    for caractere in string:
        invertida = caractere + invertida
    return invertida

entrada = input("Digite uma string: ")
print(f"String invertida: {inverter_string(entrada)}")

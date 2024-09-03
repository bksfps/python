#EX 5
def inverterString(String):
    stringInvertida = ""
    for i in range(len(String) - 1, -1, -1):
        stringInvertida += String[i]
    return stringInvertida

palavra = input("Digite uma String: ")
resultado = inverterString(palavra)
print(f"String invertida: {resultado}")

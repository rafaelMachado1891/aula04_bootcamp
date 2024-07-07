# Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, 
# calcule o preço total da lista de compras.

lista: list = ['maçã', 'banana', 'cereja']
dicionario: dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65, "picanha": 100.00}



resultado = sum(dicionario[valores] for valores in lista)

print(f"O total das suas compras é: {resultado}")
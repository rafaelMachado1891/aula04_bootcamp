# exemplo de criacao de uma funcao 

lista_de_numeros: list = [45, 77, 36, 1747, -155]

def ordenar_lista_de_numeros(numeros: list) -> list:
    nova_lista = numeros.copy()

    for i in range(len(nova_lista)):
        for j in range(i+1, len(nova_lista)):
            if nova_lista[i] > nova_lista[j]:
                nova_lista[i], nova_lista[j] = nova_lista[j], nova_lista [i]

    return nova_lista

lista_ordenada = ordenar_lista_de_numeros(lista_de_numeros)
print(lista_ordenada)
nome_valido: bool = False
salario_valido: bool = False
bonus_valido: bool = False

while nome_valido is not True:

    try: 

        nome: str = input("Digite o seu nome: ")

        if  nome.isdigit():
            print('você digitou um valor invalido: ')
            
        elif len(nome) == 0:
            print('você não digitou nada: ')
            
        elif nome.isspace():
            print('você digitou somente espaco')

        else:            
            print('Nome valido: ', nome)
            nome_valido = True
            
    except ValueError  as e:
            print(e)
    

while salario_valido is not True: 
    try:
        salario: float = float(input("Digite o seu salário: "))
        if salario <= 0:
            print('insira uma valor valido para o salário')

        else: 
            salario_valido = True
    except: 
        ValueError
        print('Você inseriu o seu salario errado, digite um valor valido')

        
while bonus_valido is not True:
    try: 
        bonus_valor: float = float(input("Qual foi o percentual do seu bonus? "))

        if bonus_valor < 0:
         print('Insira um valor positivo para o bonus')

        else:
         bonus_valido = True

    except:
        ValueError
        print('insira um valor decimal para o bônus')
        NameError
        print('você inseriu um valor invalido para o bonus, digite uma valor no formato decimal separado por "." ')
        exit()

bonus: float = 1000 + salario * bonus_valor
 

print("O valor total do seu bonus é: ", bonus)
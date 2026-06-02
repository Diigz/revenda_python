#------------------VARIAVEIS-----------------------#
plataforma = ["Mercado Livre","Shopee","Amazon Brasil","Aliexpress","Tiktok Shop"]
i = 0
repetir = 1

def pular_linha():
    print("")

#------------------APRESENTAÇÃO E INPUT-----------------------#
print("Bem vindo a calculadora de revenda!")


while repetir != 0:
    while True:
        try:
            pular_linha()
            produto = (input("Digite o nome do produto: "))
            valor = float(input("Digite o valor do produto: "))
            pular_linha()
            break
        except ValueError:
            print("Digite com a formatação correta!")
            pular_linha()


#------------------LÓGICA-----------------------#

    print("As plataformas disponíves são:")
    for i, plataformas in enumerate(plataforma, start=1):
        print(f"{i}.{plataformas}")

    pular_linha()
    escolha = int(input("Qual a sua escolha: "))
    match escolha:
        case 1:
            print(f"No Mercado livre, a sugestão é que o seu produto {produto} seja vendido por, no mínimo, R${(valor/(1-0.14)):.2f}")
            pular_linha()
        case 2:
            print(f"Na Shopee, a sugestão é que o seu produto {produto} seja vendido por, no mínimo, R${((valor/(1 - 0.2))+4):.2f}")
            pular_linha()
        case 3:
            print(f"Na Amazon Brasil, a sugestão é que o seu produto {produto} seja vendido por, no mínimo, R${(valor/(1 - 0.15)):.2f}")
            pular_linha()
        case 4:
            print(f"Na Aliexpress, a sugestão é que o seu produto {produto} seja vendido por, no mínimo, R${(valor/(1 - 0.08)):.2f}")
            pular_linha()
        case 5:
            print(f"Na Tiktok Shopee, a sugestão é que o seu produto {produto} seja vendido por, no mínimo, R${(valor/(1 - 0.08)):.2f}")
            pular_linha()

#------------------REPETIÇÃO-----------------------#
    print("Deseja testar outro produto?")
    while True:
        try:
            confirmacao_repetir = input("Digite Y ou N: ").upper()
            if confirmacao_repetir == "Y":
                repetir = 1
                break
            elif confirmacao_repetir == "N":
                repetir = 0
                break
            else:
                print("Insira um valor válido.")
                pular_linha()

        except ValueError:
            print(" ")


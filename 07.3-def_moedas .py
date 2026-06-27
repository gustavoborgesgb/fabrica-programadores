#definindo as funcoes de conversao de moedas
def dolar_real(valor_dolar):
    taxa = 5.06
    valor_real = valor_dolar * taxa
    return valor_real

def real_dolar(valor_real):
    taxa = 5.06
    valor_dolar = valor_real / taxa
    return valor_dolar

#criando o menu interativo 
def menu():
    while True:
        print("\n=== converso de moedas ===")
        print("1 - dolar para real")
        print("2 - real para dolar")
        print("0 - sair ")

        opcao = int(input("escolha uma opçao:")) #le a opcao do usuario

        if opcao == 1:
            valor = float(input("digite o valor em dolar $"))
            resultado = dolar_real(valor)
            print(f"$ {valor} = R$ {resultado:.2f}")


        elif opcao == 2:
            valor = float(input("digite o valor em real R$  "))
            resultado = real_dolar(valor)
            print(f"R$ {valor} = $ {resultado:.2f}")


        elif opcao == 0:
            print("obrigado por usar o conversos de moedas!")
            break

        else:
            print("opcao invalido. tente novamente. ")
        
#executa o programa 
menu()

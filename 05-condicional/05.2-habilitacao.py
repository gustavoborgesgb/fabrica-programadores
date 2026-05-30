#criando as variaveis 
nome = input("qual e o seu nome? ")
idade = int(input("qual sua idade? "))

#verificando condicao de motorista
if idade >= 18:
    possui_carteira  = input("possui carteira de motorista? \n(1-sim / 2-nao)")

    if possui_carteira == "1":
        print("pode dirigir")
    else:
        print("nao pode dirigir")
else:
    print("menor de idade")        
        
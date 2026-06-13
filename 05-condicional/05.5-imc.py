# Programa para calcular o Índice de Massa Corporal (IMC)
# Criação das variáveis e Solicitando os dados ao usuário
peso = float(input("digite o seu peso: "))
altura = float(input("digite sua altura: "))

 #  Realizando cálculo do imc= altura²  
imc = peso / (altura * altura)

if imc >= 30:
    print("cuidado com a saude ")
else:
    print("tudo ok")


# verificaçao do programa 
print("seu imc e:", imc)
if imc <=18.5:
    print("abaixo do peso ")
elif imc <=24.9:
    print("peso normal")
elif imc <=29.9:
    print("sobrepeso")
elif imc <=34.9:
    print("obesidade grau 1")
elif imc <=39.9:
    print("obesidade grau 2")
else:
    print("obsidade de grau 3(morbida)")







     
  
    
    

    
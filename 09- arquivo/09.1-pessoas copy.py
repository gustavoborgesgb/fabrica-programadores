#solicitando os dados do usuario
nome = input("digite o nome:  ")
email = input("digiteo e-mail: ")

#acessando o arquivo e gravando  os dados do usuario
with open("09.2-pessoas.txt","a",encoding="utf-8" ) as arquivo:
    arquivo.write(nome + " | " + email + "\n")



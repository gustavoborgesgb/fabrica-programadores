#solicitando os dados do usuario
nome = input("digite o nome:  ")
email = input("digiteo e-mail: ")

#acessando o arquivo e gravando  os dados do usuario
arquivo = open("09.2-gusta gb.txt", "a")
arquivo.write(nome + " | " + email + "\n")
arquivo.close()

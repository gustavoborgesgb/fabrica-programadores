#SOLISITANDO INFORMAÇOES DE ACESSO AO USUARIO
email = input("digite o e-mail de acesso: ")
senha = input("digite a senha de acesso: ")

#VERIFICANDO SE O EMAIL ESTA CADASTRADO 
if email == "teste@teste.com.br":
    print("email correto")
else:
    print("usuario nao cadastrado ")
#verificando se a senha esta correta a liberado acesso ao sistema
if senha == "123456":
    print("bem vindo ao sistema da fabrica")
else:
    print("senha incorreta")            
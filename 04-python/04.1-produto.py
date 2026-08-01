# Criando as variaveis e solicitando os valores ao usuario 
nome_produto = input("digite o nome do produto: ")
preco = float (input("digite o preco do produto: "))
desconto = float (input("digite o percentual de desconto: "))

# calculando o desconto e o preco final 
valor_desconto = preco * desconto / 100
preco_final = preco - valor_desconto

# apresentando o preco final ao usuario 
print(f"produto: {nome_produto} - preco final: R$ {preco_final} ")
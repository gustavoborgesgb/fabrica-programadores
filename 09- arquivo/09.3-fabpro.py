# Criando as variáveis e solicitando os dados ao usuário
nome_aluno = input("Digite o nome do aluno: ")
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

# Calculando a média das notas do aluno
media = (nota_1 + nota_2 + nota_3) / 3

print(f"A média do aluno(a) {nome_aluno} é {media}")

# Criando as condições
if media >= 7:
    print("Situação: Aprovado")
elif media > 4:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")
 # Entrada das notas
nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))

# Cálculo da média
media = (nota1 + nota2 + nota3) / 3

# Verificação da situação
if media >= 7:
    situacao = "Aprovado"
elif media > 4:
    situacao = "Em Recuperação"
else:
    situacao = "Reprovado"

# Saída
print("Média:", media)
print("Situação:", situacao)
1 # criaçao da constante com o valor do dolar 
DOLAR = 5.50

valor_em_dolar = float(input("digite o valo em dolare: "))
valor_em_real =valor_em_dolar * DOLAR

print(f"o valor convertido em reais e R$ {valor_em_real:.2f}")
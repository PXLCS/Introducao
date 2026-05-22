# Sistema de Cálculo de Descontos
# Entrada de Dados
print("Sistema de Cáculo de Desconto")

desconto = input("Digite o número do produto: ")

preco = float(input("Digite o preço do produto: "))

#Cáculo do Desconto no Preço
#Processamento de Dados

desconto = preco * 0.10

preco_final = preco - desconto

#Saída de Dados

print("Produto: ", preco)
print("Desconto: ", desconto)
print("Preço Final: ", preco_final)


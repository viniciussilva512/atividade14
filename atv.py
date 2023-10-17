# Exercício Python 14: Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um
# aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite o salário do funcionario: R$"))

if salario > 1250.00: 
    aumento = salario * 0.10 
else: 
    aumento = salario * 0.15 
    
    novo_salario = salario + aumento 
    
    print(f"O aumento salarial é de R${aumento:.2f}")
    print(f"O novo salário é de R${novo_salario:.2f}")
# n1 = int(input("Digite um numero para verificar se ele é maior ou igual a 10. "))

# if n1 < 10 :
#     print("é menor que 10")
# elif n1 > 10:
#     print("é maior que 10")
# else :
#     print("é igual a 10.")

numeroHorasTrabalhadas = float(input("Informe a duração do total dos programas: "))

valorPagoHora = float(input("Me informe o quanto cobra por hora: "))

salarioBruto = numeroHorasTrabalhadas * valorPagoHora

salarioLiquido = 0

if salarioBruto < 1000 :
    salarioLiquido = salarioBruto - (salarioBruto * 0.05)
    print('Seu salário bruto é de R${}, mas por receber menos de R$1000, seu salário recebe um desconto de 5%, totalizando R${}'.format(salarioBruto, salarioLiquido))
elif salarioBruto > 999 and salarioBruto < 1999 :
    salarioLiquido = salarioBruto - (salarioBruto * 0.1)
    print('Seu salário bruto é de R${}, mas por receber mais de R$1000.00 e menos de R$2000.00, seu salário recebe um desconto de 10%, totalizando R${}'.format(salarioBruto, salarioLiquido))
else :
    salarioLiquido = salarioBruto - (salarioBruto * 0.15)
    print('Seu salário bruto é de {}, mas por receber mais de R$2000.00, seu salário recebe um desconto de 15%, totalizando R${}'.format(salarioBruto, salarioLiquido))
    

nome = input('Insira seu Nome ')
peso = float(input("Informe o seu peso: "))
altura = float(input("Informe sua altura: "))

imc = peso / (altura ** 2)

if imc < 18.5 :
    print('{} você está abaixo do peso e o seu IMC é: {:.2f}'.format(nome, imc))
elif imc >= 18.5 and imc <= 24.9 :
    print('{} seu peso é classificado como normal e o seu IMC é :{:.2f}'.format(nome, imc))
elif imc >= 25.0 and imc <= 29.9 : 
    print('{} você é considerado levemente acima do peso e o seu IMC é :{:.2f}'.format(nome, imc))
elif imc >= 30.0 and imc <= 34.9 :
    print('{} seu peso já é considerado com obesidade I: {:.2f}'.format(nome, imc))
elif imc >= 35.0 and imc <= 39.9 :
    print('{} seu peso já é considerado com obesidade II(severa){:.2f}'.format(nome, imc))
else :
    print('{} seu peso já é considerado com obesidade III(mórbida): {:.2f}'.format(nome, imc))
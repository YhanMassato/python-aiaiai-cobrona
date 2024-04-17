#funções
numero1 = int(input('Informe o primeiro numero '))
numero2 = int(input('Informe o segundo numero '))
resultado = 0

def multiplicacao():
    global resultado
    resultado = numero1 * numero2

def soma():
    res = numero1 + numero2
    return(res)

def subtracacao(n1, n2):
    res = n1 - n2
    return(res)

def divisao(n1, n2):
    res = n1 / n2
    return(res)

operacao = input("Escolha uma operação entre '*' , '-' ou '+' ou '/' ")

while operacao != "+" or operacao != "-" or operacao != "/" or operacao != "*":
    print("Por favor, insira uma operação válida")
    operacao = input("Escolha uma operação entre '*' , '-' ou '+' ou '/' ")


if ( operacao == "+" ):
    resultado = soma()
    print(resultado)
elif ( operacao == "/"):
    resultado = divisao(numero1, numero2)
    print(resultado)
elif ( operacao == "-" ):
    resultado = subtracacao(numero1, numero2)
    print(resultado)
elif ( operacao == "*" ):   
    multiplicacao()
    print(resultado)
else:
    print("insira uma operação válida")
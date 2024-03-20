import math
def calc():
    print('calculadorinha besta')
    print('aqui você pode fazer algumas operaçõezinhas basicas, vou aprimora-lo com o tempo!')
    n1 = float(input("digite um numero:"))
    n2 = float(input('outro numero:'))
    operation = (input('''escolha sua operção, saiba que você tem os seguintes codigos para construir sua calculadora
    +, para adição
    -, para subtração
    *, para multiplicação
    /, para divisão 'exata'
    //, para divisão inteira com resultados mais simples
    você também pode usar ** para potenciação e */ para radiciação simples (neste caso, o segundo valor tem que ser nulo '0')
    '''))
    if operation == '+':
        print('{} + {} ='.format(n1, n2))
        print(n1 + n2)
    elif operation == '-':
        print('{}-{}='.format(n1, n2))
        print(n1 - n2)
    elif operation == '*':
        print('{}*{}='.format(n1, n2))
        print(n1 * n2)
    elif operation == '/':
        print('{}/{}='.format(n1, n2))
        print(n1 / n2)
    elif operation == '//':
        print('{}//{}='.format(n1, n2))
        print(n1 // n2)
    elif operation == '**':
        print('{}**{}='.format(n1, n2))
        print(n1 ** n2)
    elif operation == '*/':
        print(('n1/*2'))
        print(math.sqrt(n1))
    else:
        print('reinicie o programa e tente novamente, seu sinal operacional provavelmente está errado')

    again()

def again():
    dnv = input('para calcular novamente, digite s para sim ou n para não')
    if dnv.upper() == 'S':
        calc()
    elif dnv.upper() == 'N':
        print('até uma proxima, meu caro amigo, espero poder ajuda-lo mais e mais vezes!')

    else:
        again()
calc()

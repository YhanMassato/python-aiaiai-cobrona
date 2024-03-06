import math
import random
# curso = 'Python'
# ano = 2004
# valor = 15000.00

# # '''Concatenando com virgula'''

# # print("O curso de ", curso, "possui o valor de", valor, " no ano de ", ano)

# # '''concatennado com identificadores'''

# # print ("O curso de %s, possui o valor de %.2f, no ano de %d" % (curso, valor, ano) )

# # '''Operador -> + '''

# # print("O curso de " + curso + " possui o valor de " + str(valor) + " no ano de" + str(ano))

# message = "O curso de " + curso + " possui o valor de " + str(valor) + " no ano de" + str(ano)
# print (type(message))

# 

# print('Raiz quadrada de 49', math.sqrt(49))
# print('Cosseno de 180 graus', math.cos(180))
# print('Seno de 360 graus', math.sin(360))
# print('Tangente de 180 graus', math.tan(180))
# print('Angulo de 90 graus', math.radians(90))
# print('PI', math.pi)
# print('Hipotenusa de 4 e 9', math.hypot(4, 9))
# print('Arredonda o valor para cima 5.584:', math.ceil(5.584))

# print("random.randrange(100): ",random.randrange(100))
# print("random.randrange(50, 100): ", random.randrange(50, 100)) 
# print("random.choice([40,21,32,12,45]): ",random.choice([40,21,32,12,45]))
# print("random.random(): ", random.random())
# print("random.randint(30,60): ",random.randint(30,60))
# //==//
# n1 = int(input('Insira o numero '))
# n1 += 1
# print ('O sucessor do seu numero é : {}'.format(n1))
# //==//

raio = float(input('Insira o raio de sua circuferência em metros'))

perimetro = math.pi * 2 * raio
area = math.pi * (raio ** 2)

print('A área do seu cirulo é igual a :{}m² e o perimetro da circunferencia é de: {}m.'.format(area, perimetro))

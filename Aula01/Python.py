import math

a = float(input("insira o valor de A"))

if a == 0 :
    print('A não pode ser igual a 0, pois sua equação não existirá solução')
    exit()
b = float(input("Insira o valor de B")) 
c = float(input("Insira o valor de C")) 

delta = (b**2) - (4 * a * c)

if delta < 0:
    print("Sua equação não possui solução no campo dos números reais")
    exit()

elif delta == 0 :
    x = -(b) / 2*a
    print('Sua equação possui um resultado nos campos dos reais e ele equivale a {}' .format(x))

else : 
    delta = math.sqrt(delta)
    x1 = (-(b) + delta) / 2 * a
    x2 = (-(b) - delta) / 2 * a
    
print('Sua equação do segundo grau retornou os valores {} e {}' .format(x1, x2))
    


#bhaskara

a = float(input('Digite o valor de a'))

b = float(input('Digite o valor de b'))

c = float(input('Digite o valor de c'))

if a == 0:
    print('O valor de "a" não pode corresponder a zero, reinicie o código por favor')
else :
    delta = float((b**2) - (4*a*c))
    delta1 = delta ** 0.5
    
    print(delta)
    
    if 0 > delta:
          print('Desculpe, mas sua equação não possui uma solução na área dos inteiros.')
               
    elif delta == 0 :
          x = ((-b) / (2 * a))
          print('Para a equação de segundo grau {}x^2 + {}x + {} = 0, temos apenas uma solução, que é{}' .format(a, b, c, x)) 
    else  :
        print(delta)
        x1 = ((-b) + delta1 ) / (2 * a)
        x2 = ((-b) - delta1 ) / (2 * a)
        print('Para a equação de segundo grau {}x^2 + {}x + {} = 0, temos duas possíveis soluções {} e {}' .format(a, b, c, x1, x2)) 
        
     
        

   

     
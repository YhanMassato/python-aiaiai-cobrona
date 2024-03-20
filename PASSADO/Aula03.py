#Operações aritméticas

#símbolos 
print('  * = adição')
print('  + = soma')
print('  - = subtração')
print('  / = divisão')
print('  ** = exponenciação')
print('  // = divisão inteira, sem prosseguir com a vírgula')
print('  % = mostra o resto de uma divisão')
#estrutura das operações aritméticas 

print('ordem de precedência dos fatores')
print('1° ()')
print('2° **')
print('3° * / // %')
print('4° + -')

#exercícios

nm=input('Bom dia, me diga seu nome')
print('Prazer em te conhecer {:60}!' .format(nm))

#para centralizar se usa o caractere ^
print('Prazer em te conhecer {:^60}!' .format(nm))

#colocar caracteres nos espaços 
print('Prazer em te conhecer {:=^60}!' .format(nm))   

#calculadorazinha
n1 = int(input('Digite um valor'))
n2 = int(input('Digite outro valor'))

s = n1 + n2 
d = n1 / n2 
su = n1 - n2
m = n1 - n2    
di = n1 // n2
e = n1 ** n2

print('A soma dos números {} e {} é {}'.format(n1, n2, s))
print('A subtração é {}' .format(su))
print('A multiplicação é {}' .format(m))
print('A divisão é {}' .format(d))
print('A divisão inteira é {}' .format(di))
print('A potência é {}' .format(e))

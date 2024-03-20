# n1 = int(input('Insira o número que você deseja saber a taboada '))
# rangeT = int(input('Insira a quantidade de multiplos desejada '))

# for n in range(rangeT):
#     result = n1 * n
#     print(f'{n} * {n1} = {result}')

#media

# n = int(input('Quantos valores serão inseridos? '))
# i = 0

# for no in range(n):
#     i += int(input('Insira a nota :'))
    
# print(f'A média dos valores informados é {i/n} ')

## ----------- ##

# n1 = int(input('Insira o número que você deseja saber a taboada '))
# multiplos = int(input('Insira a quantidade de multiplos desejada '))
# i = 0
# while i <= multiplos:
#     result = n1 * i
#     print(f"{n1} * {i} = {result}")
#     i += 1 

## media while

n = int(input('Quantos valores serão inseridos? '))
i = 0
media = 0

while i < n :
    media +=(int(input('Insira a nota ')))
    i +=1

print(f'A média dos valores é de {media/n}')



    

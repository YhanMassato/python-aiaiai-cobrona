#Dissecando uma variável 

x = input('Digite algo')

print('o tipo da variável "{}" é'.format(x) ,type(x))
print('É numérico?', x.isnumeric())
print('É alfabético?', x.isalpha())
print('É alfanumérico?', x.isalnum())
print('É totalmente maiúsculo?', x.isupper())
print('É totalmente minúsculo?', x.islower())
print('É decimal?', x.isdecimal())


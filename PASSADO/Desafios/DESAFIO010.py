#conversor dolar real
re = float(input('Digite a quantidade que você tem em real.'))

cd = float(input('Digite a cotação do dólar hoje'))

qt = re / cd

print('Com R${}, você pode comprar US{:.3}' .format(re, qt))
#Pintor de parede

h = int(input('Digite a altura da parede'))

w = int(input('Digite a largura da parede'))

a = h * w

l = a / 2

print('A sua parede de {} x {}, cuja area corresponde a {}m², precisará de {} litros de tinta para ser pintada.' .format(h, w, a, l))
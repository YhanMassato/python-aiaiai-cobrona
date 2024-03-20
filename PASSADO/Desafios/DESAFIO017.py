#calculador de hipotenusa
import math

co = float(input('Digite o comprimento do lado oposto'))

ca = float(input('Digite o comprimento do lado adjacente'))

h = math.sqrt(((ca ** 2) + (co ** 2)))

print('Para você, que fugiu da escola, a hipotenusa desse desse trinagulo é {}' .format(h))


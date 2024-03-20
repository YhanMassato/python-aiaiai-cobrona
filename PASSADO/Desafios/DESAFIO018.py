#calculadora de trigonometria
import math

an = float(input('Digite aqui seu angulo de merda'))

sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tan = math.tan(math.radians(an))

print('Seno {:.2f}' .format(sen))
print('Cosseno{:.2f}' .format(cos))
print('Tangente{:.2f}' .format(tan))
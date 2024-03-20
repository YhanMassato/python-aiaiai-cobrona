#Carro aluguel
cdu = float(input('Por quantos dias tu usou o carro?'))
kmr = float(input('Por quantos km tu sentou esse teu cu sujo no banco do carro?'))

to = 60 * cdu + kmr * 0.15

print('Tu deve pro carro R${}.' .format(to))
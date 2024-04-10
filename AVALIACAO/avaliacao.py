print("Bem vindo à eleição da cidade de Etequilson")
print("Existem 3 candidatos, poderia me informar o nome deles?")

candidatos = []
votos = []

for i in range(3) :
  candidato = input("Nome:")
  candidato = candidato.upper()
  candidatos.append(candidato)

candidato1 = candidatos[0]
candidato2 = candidatos[1]
candidato3 = candidatos[2]

print("Obrigado, agora me diga a quantidade de votos totais")

votosTotais = input("Número total de votos ")

while votosTotais.isnumeric() != True :   
    votosTotais = input("Número total de votos ")

votosTotais = float(votosTotais)

print(f"Certo, a candidatura possuirá {votosTotais} votos ao todo.")

while votosTotais > 0 :
    voto = input(f"Vote no seu candidato! Os avaliáveis são: {candidato1}, {candidato2} e {candidato3} ")
    voto = voto.upper()
    
    if voto == candidatos[0] or voto == candidatos[1] or voto == candidatos[2]:
        votos.append(voto)
        print("Voto realizado com sucesso")
        votosTotais -= 1
    else :
        print(f"Este não é um candidato válido. Os cadidatos são: {candidato1}, {candidato2} e {candidato3}")
        
print("Votação terminada!")
print("Realizando a contagem de votos...")
votosCandidato1 = votos.count(candidatos[0])
votosCandidato2 = votos.count(candidatos[1])
votosCandidato3 = votos.count(candidatos[2])

print("Aqui está o resultado da votação:")

if votosCandidato1 == votosCandidato2 and votosCandidato1 == votosCandidato3 :
    print(f"Todos empataram com a mesma quantidade de votos... \nQuantidade total de votos: para cada {votosCandidato1}")
      
elif votosCandidato1 > votosCandidato2 and votosCandidato1 > votosCandidato3 :
    if votosCandidato2 > votosCandidato3 :
        print(f"Resultados: \n1º Candidato {candidato1} com {votosCandidato1} \n2º Candidato {candidato2} com {votosCandidato2} \n3º Candidato {candidato3} com {votosCandidato3}")
    else :
        print(f"Resultados: \n1º Candidato {candidato1} com {votosCandidato1} \n2º Candidato {candidato3} com {votosCandidato3} \n3º Candidato {candidato2} com {votosCandidato2}")
        
elif votosCandidato2 > votosCandidato1 and votosCandidato2 > votosCandidato3 :
    if votosCandidato1 > votosCandidato3 :
        print(f"Resultados: \n1º Candidato {candidato2} com {votosCandidato2} \n2º Candidato {candidato1} com {votosCandidato1} \n3º Candidato {candidato3} com {votosCandidato3}")
    else :
        print(f"Resultados: \n1º Candidato {candidato2} com {votosCandidato2} \n2º Candidato {candidato3} com {votosCandidato3} \n3º Candidato {candidato1} com {votosCandidato1}")
        
elif votosCandidato3 > votosCandidato2 and votosCandidato3 > votosCandidato1 :
    if votosCandidato1 > votosCandidato2 :
        print(f"Resultados: \n1º Candidato {candidato3} com {votosCandidato3} \n2º Candidato {candidato1} com {votosCandidato1} \n3º Candidato {candidato2} com {votosCandidato2}")
    else :
        print(f"Resultados:\n 1º Candidato {candidato3} com {votosCandidato3} \n2º Candidato {candidato2} com {votosCandidato2} \n3º Candidato {candidato1} com {votosCandidato1}")

elif votosCandidato1 == votosCandidato2 and votosCandidato1 != votosCandidato3 :
    print(f"O candidato {candidato1} e o candidato {candidato2} empataram")
    print(f"Empate: {votosCandidato1} votos \nCandidato {candidato3} ficou com {votosCandidato3} voto.")

elif votosCandidato1 == votosCandidato3 and votosCandidato1 != votosCandidato2 :
    print(f"O candidato {candidato1} e o candidato {candidato3} empataram")
    print(f"Empate: {votosCandidato1} votos \nCandidato {candidato2} ficou com {votosCandidato2} voto.")

elif votosCandidato3 == votosCandidato2 and votosCandidato3 != votosCandidato1 :
    print(f"O candidato {candidato3} e o candidato {candidato2} empataram")
    print(f"Empate: {votosCandidato3} votos \nCandidato {candidato1} ficou com {votosCandidato1} voto.")



    



    


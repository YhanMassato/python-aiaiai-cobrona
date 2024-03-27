# text = input("Inisira uma palavra que será contado ")
# nChar = len(text)
# print(f"sua frase possui {nChar} caracteres")
# #####_--------------_

# sala = ["joao","joao","Maria","Thay","carol","divisao","Lucas","yhan","guilherme","joao"]

# print(sala.count("joao")

######## _------------_
# qntdPal = int(input("Insira a quantidade de palavras que você deseja digitar"))
# paltotal = []
# for i in range(qntdPal):
#     pal = input("insira a palavra ")
#     paltotal.append(pal)
    
# print(" ".join(paltotal))

###### _---------_
print("Descubra se a palavra é um palindromo (●'◡'●)")
palavra = input("Insira a palavra ")

palavraReversa = palavra[::-1]

palavra = palavra.upper()
palavraReversa = palavraReversa.upper()

if palavraReversa == palavra :
    print("Sua palavra é um palindromo (p≧w≦q)")
else :
    print("Sua palavra não é um palindromo (┬┬﹏┬┬)")
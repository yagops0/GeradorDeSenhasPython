import random as r
import string 

# print(ord('A'))

# print(r.choice(string.ascii_letters))

def gerar_senhas(tamanho : int):
    aux = ""
    senha = []
    for i in range(tamanho):
        aux = r.choice(string.ascii_letters)
        senha.append(aux)
        aux = r.choice(string.digits)
        senha.append(aux)
        aux = r.choice(string.punctuation)
        senha.append(aux)
    return senha



tamanho = int(input("Digite o tamanho da senha que deseja: "))
senha = gerar_senhas(tamanho)

print(senha)



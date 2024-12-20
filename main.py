import random as r
import string 

# print(ord('A'))

# print(r.choice(string.ascii_letters))

def gerar_senhas(tamanho : int):
    senha = []
    # i=0
    for i in range(tamanho):
        senha.append(r.choice(string.ascii_letters))
        senha.append(r.choice(string.digits))
        senha.append(r.choice(string.punctuation))
    return senha

def escolher_caracteres(lista : list, tamanho):
    senhaDefinitiva = []
    for i in range(tamanho):
        senhaDefinitiva.append(r.choice(lista))
    return senhaDefinitiva




tamanho = int(input("Digite o tamanho da senha que deseja: "))
senha = gerar_senhas(tamanho)
senhaDefinitiva = escolher_caracteres(senha, tamanho)
print(senha)
print(len(senha))
print(senhaDefinitiva)
print(len(senhaDefinitiva))



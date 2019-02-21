import random as r

v_lista = []
i = 1

while i <= 20:
    v_lista.append(r.randrange(1,100,3))
    i = i+1

print(f'Essa foi a lista gerada aleatoriamente: {v_lista}')

def maior_valor(v_lista):
    return max(v_lista, key=int)

print(f'Maior valor é: {maior_valor(v_lista)}')
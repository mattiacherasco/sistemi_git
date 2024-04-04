#lambda function: utile per definire funzioni brevi
'''
#funzione normale
def somma(a, b):
    return a+b

#funzione lambda
somma = lambda x, y: x+y
'''
somma = lambda x, y: x+y

lista =[10, 4]
#print(somma(lista[0], lista[1]))
print(somma(*lista))#funziona come sopra, ma la lista ha il numero uguale ai parametri(spacchettare la lista su parametri)

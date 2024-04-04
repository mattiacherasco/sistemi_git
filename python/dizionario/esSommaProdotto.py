def somma(a, b):
    return a+b
def sottrazione(a, b):
    return a-b
def prodotto(a, b):
    return a*b
def divisione(a, b):
    return a/b

    #pass non fa niente, ma almeno non da errori se non ce niente


def main():
    #print(somma) somma è un oggetto quindi si stampa l'indirizzo della funzione
    dizionario={"+":somma, "-": sottrazione, "*": prodotto, "/": divisione}
    operazione=input("scrivi + per somma, * per prodotto, - per sottrazione, / per divisione: ")
    a=float(input("scrivi il primo numero: "))
    b=float(input("scrivi il secondo numero: "))
    print(dizionario[operazione](a,b))

if __name__=="__main__":
    main()




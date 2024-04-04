def main():
    lista = [4, 100, 3, 5, "ciao", print] # lista(simile vettori)

    #ciclo for c-style
    for i in range(0, len(lista)):
        print(f"l'elemento in lista{i}-esimo è {lista[i]}")


    #ciclo for python-style
    for elemento in lista:
       print(f"elemento è {elemento}")

if __name__=="__main__":
    main()
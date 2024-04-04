def trovaSequenza(sequenza, target):
    if target in sequenza:
        index = sequenza.index(target)
        return index
    return None

#def trovaSequenza(sequenza, target):
    #index = sequenza.find(target)
    #return index

def main():
    dizionario={"A":0, "T":0, "G":0, "C":0}
    with open("/home/mattia/scuola/sistemi/quarta/python_git/prova verifica/covid-19_gen1.txt", "r") as file:
        sequenza = file.read().replace('\n', '')
    for valore in sequenza:
        dizionario[valore]+=1
    print(sequenza)
    print(dizionario)
    target="ATGTTTGTTTTT"
    trovato=trovaSequenza(sequenza, target)
    if trovato is None:
        print(f"La sequenza '{target}' non è presente nel genoma.")
    else:
        print(f"La sequenza '{target}' è presente nella posizione iniziale: {trovato}")
        
if __name__=="__main__":
    main()
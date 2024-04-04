def contaNucleotidi(sequenza):
    dizionario = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for nucleotide in sequenza:
        if nucleotide in dizionario:
            dizionario[nucleotide] += 1
    return dizionario

def trovaSequenza(sequenza, target):
    if target in sequenza:
        index = sequenza.index(target)
        return index
    return None

def main():
    with open("covid-19_gen1.txt", "r") as file:
        sequenza = file.read().replace('\n', '')
    print(sequenza)
    dizionario = contaNucleotidi(sequenza)
    print("Occorrenze dei nucleotidi nella sequenza genomica:")
    for nucleotide, count in dizionario.items():
        print(f"{nucleotide}: {count}")

    target = "ATGTTTGTTTTT"
    trovato = trovaSequenza(sequenza, target)
    if trovato is None:
        print(f"La sequenza '{target}' non è presente nel genoma.")
    else:
        print(f"La sequenza '{target}' è presente nella posizione iniziale: {trovato}")
        

if __name__ == "__main__":
    main()

#il dizionario è un insieme di coppie chiave: valore
#il dizionario non ha indici, ma viene indicizzato per chiave

def main():
    dizionario={"nome": "Mario", "cognome": "Rossi"}        #nome=chiave, mario=valore
    print(dizionario["nome"])
    #aggiungo
    dizionario["data nascita"] = "01/01/2000"
    dizionario["eta"]=123
    #sovrascrive
    dizionario["nome"]="Luca"

    #ciclo
    for chiave in dizionario:
        print(f"Chiave:{chiave} - Valore:{dizionario[chiave]}")

    rubrica={38189192:"Mario Rossi", 3313309799: "Mattia Cherasco"}
    print(dizionario)
    print(rubrica)


if __name__=="__main__":
    main()
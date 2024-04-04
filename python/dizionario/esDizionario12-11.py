def cercaContatto(rubrica, chiave):
    if chiave in rubrica:
        return rubrica[chiave]
    else:
        for nome, numero in rubrica.items():
            if numero == chiave:
                return nome
        return "Contatto non trovato"
    
def main():
    #il dizionario è una collezione di coppie chiave: valore
    #il dizionario non ha indici, ma si indicizza per chiave (è univoca)
    dizionario = {"nome": "Mario", "cognome" : "Rossi"} #nome->chiave mario->valore, cognome->chiave rossi->valore
    #lista = ["Mario", "Rossi"] lista analoga al dizionario
    print(dizionario["nome"])
    #assegnamento in cui aggiunge un nuovo elemento al dizionario
    dizionario["data nascita"] = "01/01/1900"
    dizionario["età"] = 123
    #sovrascrive sulla chiave nome
    dizionario["nome"] = "Luca" 
    print(dizionario)

    #ciclo for su dizionario [scorrimento sulle chiavi]
    for chiave in dizionario:
        print(f"Chiave: {chiave} - valore: {dizionario[chiave]}")

    rubrica = {"Marco Giorgis": "3666616216", "Nico": "3499378455"}
    for chiavi in rubrica:
        print(f"Chiave: {chiavi} - valore: {rubrica[chiavi]}")
    print(rubrica)
    ricercato = input("inserire nome o numero di telefono da ricercare: ")
    
    risultato = cercaContatto(rubrica, ricercato)
    print(f"Risultato: {risultato}")

if __name__ == "__main__":
    main()
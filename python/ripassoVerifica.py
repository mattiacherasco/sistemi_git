def main():
    lettere = "abcdefghilmnopqrstuvz ?"
    N = len(lettere)
    lettere2numeri = {}
    numeri2lettere = {}
    for posizione, lettera in enumerate(lettere):
        lettere2numeri[lettera]= posizione
        numeri2lettere[posizione]= lettera
        
    testo_chiaro = "ciao come stai?"
    chiave = "itisdelpozzo fprfrncnc rnfrfrovmc rmfcpdndpcs?"
    testo_criptato = ""
    testo_decodificato = ""

    for lettera_testo, lettera_chiave in zip(testo_chiaro, chiave): #cicla in parallelo sulle due parole fermandosi alla più corta
        numero = (lettere2numeri[lettera_testo] + lettere2numeri[lettera_chiave]) % N
        testo_criptato += numeri2lettere[numero]
    print(f"il testo in chiaro '{testo_chiaro}' diventa: '{testo_criptato}'")

    for lettera_testo, lettera_chiave in zip(testo_criptato, chiave):
        parola = (lettere2numeri[lettera_testo] - lettere2numeri[lettera_chiave]) % N
        testo_decodificato += numeri2lettere[parola]
    print(f"il testo codificato '{testo_criptato}' decofica '{testo_decodificato}'")

    #t = Testo(testo_chiaro, chiave, lettere2numeri, numeri2lettere)
    #t.codifica()

if __name__ == "__main__":
    main()
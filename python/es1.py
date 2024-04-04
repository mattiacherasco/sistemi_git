def main():
    nome = input("come ti chiami? ")
    anni = input("quanti hanni hai? ")
    anno_corrente = int(input("in quale anno siamo? "))

    print(f"il tuo nome è {nome} e hai {anni} anni")
    print(f"sei nato nel {anno_corrente - anni}")

if __name__=="__main__":
    main()
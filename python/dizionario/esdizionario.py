def main():
    file=open("rubrica.txt", "r")
    righe=file.readlines()
    file.close
    rubrica={}
    print(righe)

    for riga in righe:
        campi=riga.split(",")
        print(campi[0])
        print(campi[1].replace("\n",""))
        
        rubrica[int(campi[1].replace("\n",""))]=campi[0]

    print(rubrica)


if __name__=="__main__":
    main()




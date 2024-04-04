def main():
    lista=[]
    k=0
    while True:
        voto=int(input("inserisci il tuo voto (-1 per interrompere)"))
        if(voto<0 and k>=6):
            break
        lista.append(voto)
        k+=1

    print(lista[1:-1])
    print(f"{lista[0:3]} 10 {lista[5:]}")
    print(lista[0:3])

if __name__=="__main__":
    main()
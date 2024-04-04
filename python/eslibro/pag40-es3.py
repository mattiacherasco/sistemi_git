def main():
    
    n1 = float(input("inserisci un numero"))
    n2 = float(input("inserisci l'altro numero"))
    simbolo = int(input("inserisci\n0:sommma\n1:sottrazione\n2:moltiplicazione\n3:divisione"))
    if simbolo == 0:                   
        print(f"{n1+n1}")
    elif simbolo == 1:                   
        print(f"{n1-n1}")
    elif simbolo == 2:                   
        print(f"{n1*n1}")
    elif simbolo == 3:                   
        print(f"{n1/n1}")
    else:
        print("reinserire il numero")

if __name__=="__main__":
    main()
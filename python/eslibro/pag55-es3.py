def main():

    n1 = input("inserisci un numero")
    n2 = input("inserisci il secondo numero")
    print("numero1 =", n1)
    print("numero2 =", n2)

    n1, n2 = n2, n1

    print("Dopo lo scambio:")
    print("numero1 =", n1)
    print("numero2 =", n2)
   

if __name__=="__main__":
    main()

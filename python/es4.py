def main():
    a = 10
    n1 = input("inserisci un numero")
    n2 = input("inserisci il secondo numero")
    if n1 > n2 :                           #<>
        n1, n2 = n2, n1
    else:
        n1, n2=n1, n2
    print(f"{n1} {n2}")

if __name__=="__main__":
    main()
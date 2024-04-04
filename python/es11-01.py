def main():
    num = int(input("Inserisci un numero dispari: "))
    while num % 2 != 1:
        num = int(input("Reinserisci un numero dispari: "))
    for k in range(1, num + 2, 2):
        print(" " * int((num-k)/2) + "*" * k)
    
    for k in range(num-2, 0, -2):
        print(" " * int((num-k)/2) + "*" * k)

if __name__=="__main__":
    main()
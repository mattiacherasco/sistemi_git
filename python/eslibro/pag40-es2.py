def main():
    
    n1 = int(input("inserisci un numero"))
    if n1 % 2 == 0:                   
        print("è divisibile per 2")
    elif n1 % 3 == 0:                           #<>
        print("è divisibile per 3")
    elif n1 % 4 == 0:
        print("è divisibile per 4")
    elif n1 % 5 == 0:               
        print("è divisibile per 5")
    else:
        print("non è divisibile")

if __name__=="__main__":
    main()
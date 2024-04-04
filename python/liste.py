import random

def print_list(l):
    print("la lista è:", end=" ")
    for elemento in l:
        print(elemento, end=" ")
    print("\n")

def main():
    l=[1, 2, 3, 4, "c", 3, 14, "python"]
    r=[10, 12, 14]
    print_list(l)
    print_list(l+r)
    print_list(3*r)
    print_list(l[-1])
    print_list(l[::-1])
    


    lista=[]
    num=1
    while(num>0):
        num=int(input("un numero: (-1 per interrompere): "))
        if(num > 0):
            lista.append(num)
    print_list(lista)

    

    #list comprehension
    #lista con i primi 5 quadrati perfetti
    quadrati = [i*i for i in range(1,6)]
    numeri_interi=[i for i in range(1,11)]
    print(quadrati)
    print(numeri_interi)
    stringhe=["computer", "cellulare", "laptot"]
    stringhe_c=[parola for parola in stringhe if parola[0]=="c"]
    print(stringhe_c)


    voti=[random.randint(2,10) for _ in range(0,10)]
    print(voti)
    voti_insuff=[voto for voto in voti if(voto<6)]

if __name__=="__main__":
    main()
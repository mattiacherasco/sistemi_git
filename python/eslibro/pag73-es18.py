import math

def main():
    lista = [i**2 for i in range(1,int(math.sqrt(200))+1) if(i%2 != 0)]
   # lista = [i**2 for i in range(1,1000) if(i%2 != 0) and(i**2<200)] soluzione meno ottimale

    print(lista)

if __name__=="__main__":
    main()
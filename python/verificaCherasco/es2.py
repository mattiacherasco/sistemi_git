def main():
    x=0
    num=0
    lim=999
    for num in range(0, lim):
        for cont in range(0, len(str(num))):
            numL=int(str(num)[cont])
            x=x+numL**3
        if(x==num):
            print(x)
   
def mainCorretto():
    for numero in range(1, 1000):
        listaCifre=[int(cifra)**3 for cifra in str(numero)]==numero
        print(f"il numero {numero} è narcisita")

if __name__=="__main__":
    main()
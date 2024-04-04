import turtle

def print_list(l):
    print("la lista è:", end=" ")
    for elemento in l:
        print(elemento, end=" ")
    print("\n")

def main():
    cont=0
    lista=[]
    cont=0
    num=1
    while(num>0):
        lista[cont]=(input("inserisci una lettera"))
        cont=cont+1
        num=int(input("inserisci un numero negativo se hai dichiarato tutto"))
        if(num > 0):
            lista.append(num)
    
    finestra = turtle.Screen()
    disegno = turtle.Turtle()
    disegno.begin_fill()
    for i in range(0, cont):     
        disegno.color("red")
        if(lista[i]=='f'):
            disegno.forward(100)
        elif(lista[i]=='r'):
            disegno.right(90)
        elif(lista[i]=='l'): 
            disegno.left(90)

    disegno.end_fill()
    


if __name__=="__main__":
    main()
import turtle

def nord(disegno, lung):
    
    disegno.setheading(90)
    disegno.forward(lung)
    
def sud(disegno, lung):
    disegno.setheading(-90)
    disegno.forward(lung)

def est(disegno, lung):
    disegno.setheading(0)
    disegno.forward(lung)

def ovest(disegno, lung):
    disegno.setheading(180)
    disegno.forward(lung)

def uscita(disegno, lung):
    exit()

    #pass non fa niente, ma almeno non da errori se non ce niente

#chiedere nord sud est ovest all'utente, un movimento è costante di cento verso la direzione definita



def main():
    lung=float(input("inserisci di quanto si muove(lunghezza)"))
    dizionario={"n":nord, "s": sud, "e": est, "o": ovest, "esc": uscita}
    finestra = turtle.Screen()
    disegno = turtle.Turtle()


    while(True):
        operazione=input("scrivi n per nord, s per sud, e per est, o per ovest")
        if operazione in dizionario:
            dizionario[operazione](disegno, lung)
        

if __name__=="__main__":
    main()




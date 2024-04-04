import turtle #esempio di importazione di un modulo built-in

num = int(input("inserisci il numero di lati"))   #<>
lung= int(input("inserisci la lunghezza dei lati"))
finestra = turtle.Screen()
alice = turtle.Turtle()
alice.begin_fill()
for i in range(0, num):     
    alice.color("red")
    alice.forward(lung)
    alice.left(360/num)
alice.end_fill()
finestra.mainloop()
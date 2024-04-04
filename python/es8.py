import turtle #<>

finestra = turtle.Screen()

poligono = turtle.Turtle()
poligono.shape("turtle")
poligono.begin_fill()
poligono.color("black")

lunglati = int(input("Inseriscila lunghezza dei lati del poligono"))
nangoli = int(input("Inserisci il numero di angoli che deve avere il poligono[da 3 a 12 compresi]"))

if (3<nangoli<12):
    for i in range(nangoli):
        poligono.forward(lunglati)
        poligono.left(360/nangoli)
else:
    print("il numero di angoli deve essere da 3 a 12 compresi")

poligono.end_fill()

finestra.mainloop()
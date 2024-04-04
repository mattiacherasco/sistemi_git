import turtle

finestra = turtle.Screen()

stella = turtle.Turtle()
stella.shape("turtle")
stella.begin_fill()
stella.color("yellow")

numero_punte = int(input("Inserisci il numero di punte della stella (deve essere dispari): "))

if numero_punte % 2 == 0:
    print("Il numero di punte deve essere dispari.")
else:

    lunghezza_punte = 100

    angolo_punte = 360 / numero_punte

    for i in range(numero_punte):
        stella.forward(lunghezza_punte)
        stella.right(180 - angolo_punte)

        stella.forward(lunghezza_punte)
        stella.left(180 - (angolo_punte * 2))

stella.end_fill()

finestra.mainloop()
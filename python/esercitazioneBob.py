import random
import turtle

class Punto():
    def _init_(self,x,y):
        self.x=x
        self.y=y
        
def main():
    tarta = turtle.Turtle()
    finestra = turtle.Screen()
    tarta.speed("fast")
    percorso = {0: Punto(0,0)}
    lista = [1,2,3,4]
    lung = 10
    for minuto in range(1,60):
        spost = random.choice(lista)
        if spost == 1:
            percorso[minuto] = Punto(percorso[minuto-1].x, percorso[minuto-1].y+10)
        elif spost == 2:
            percorso[minuto] = Punto(percorso[minuto-1].x,percorso[minuto-1].y-lung)
        elif spost == 3:
            percorso[minuto] = Punto(percorso[minuto-1].x+lung,percorso[minuto-1].y)
        elif spost == 4:
            percorso[minuto] = Punto(percorso[minuto-1].x-lung,percorso[minuto-1].y)
        tarta.goto(percorso[minuto].x, percorso[minuto].y)
    for tempo in percorso:
        if percorso[minuto].x ==  percorso[minuto].x and  percorso[minuto].y  == percorso[minuto].y:
            print(f"bob è passato di nuovo per { percorso[minuto].x},{ percorso[minuto].y}")  
    with open("percorso.csv","w") as file:
        file.write("MINUTO X Y \n")
        for minuto in percorso: #ciclo su dizionario percoso
            file.write(f"{minuto} {percorso[minuto].x} {percorso[minuto].y}\n")
    finestra.mainloop()

if __name__ == "__main__":
    main()
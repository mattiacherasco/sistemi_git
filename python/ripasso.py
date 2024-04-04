import random

class Nemico():
    def __init__(self, posX, posY, nVite):
        self.posX=posX
        self.posY=posY
        self.nVite=nVite
    def stampa(self):
        print(f"nemico in posizione {self.posX},{self.posY} con {self.nVite} vite")       
    
def main():
    nNemici=5
    WIDTH=800
    HEIGHT=400
    listaNemici=[]
    random.seed(1234) #seleziona il seme del generatore di numeri pseudocasuali
    for _ in range(nNemici):
        posX=random.randint(0, WIDTH-1)
        posY=random.randint(0, HEIGHT-1)
        nemico=Nemico(posX, posY, 5)
        listaNemici.append(nemico)    
    personaggio={"posX":100, "posY":200} 
    for nemico in listaNemici:
        nemico.stampa()
        if(nemico.posX==personaggio["posX"] and nemico.posY==personaggio["posY"]):
            print("COLLISIONE")
    
if __name__ =="__main__":
    main()
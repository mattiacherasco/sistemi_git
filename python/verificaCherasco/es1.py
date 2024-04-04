class primoEs:
    def __init__(self, frase):
        self.frase=frase
        self.parola=[]

    def calcoloCrattere(self, x):
        cont=0
        for _ in x:
            cont+=1
        return cont

    def restituireListe(self):
        return self.frase.split(" ")
    
    def restituireLunghezza(self):
        self.parola=self.restituireListe()
        cont=[]
        for x in len(self.parola):
            cont[x]+=1
        return cont    
        
    def trovaSequenza(self, target):
        if target in self.frase:
            return True
        return False
    
    def salvaSuFile(self, nomeFile):
        with open(nomeFile, "w") as file:
            file.write(self.frase)
    
    def calcolaFrequenza(self): # so puo fre anche con get(paola, 0)+1
        dizionario={"ciao":0, "come":0, "stai":0}
        for chiave in dizionario:
            if self.trovaSequenza(self.frase):
                dizionario[chiave]+=1 
        return dizionario
    
def main():
    frase="ciao come stai ciao"
    x=primoEs(frase)
    print(x.trovaSequenza("ciao"))

if __name__=="__main__":
    main()
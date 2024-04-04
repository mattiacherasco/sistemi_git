#cirfario di vernam
#converto in numeri, poi sommo i numeri+la chiave,poi mod 21[%21], poi sottraggo la chiave
#classe che può contenere sia un testo in chiave che codificato
dizionarioa0={0:"a" , 1:"b" ,  2:"c" , 3:"d" , 4:"e" , 5:"f" ,  6:"g" , 7:"h" , 8:"i" , 9:"l" ,  10:"m" , 11:"n" , 12:"o" , 13:"p" ,  14:"q" , 15:"r" ,  16:"s" , 17:"t" ,  18:"u" , 19:"v" , 20:"z"}
dizionario0a={}
for numero in dizionarioa0:
    dizionario0a[dizionarioa0[numero]]=numero

class cifrarioVernam:
    def __init__(self, testo, chiave, cifrato):
        self.testo=testo.lower()
        self.chiave=chiave.lower()
        self.cifrato=cifrato
        
    def dichiara(self):
        pass

    def codifica(self):
        pass
    def decodifica(self):
        pass    
        
def main():
    stringa=input("inserisci una stringa")
    cifrarioVernam.__init__(stringa, )

if __name__=="__main__":
    main()
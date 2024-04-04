class Coda:    
    def __init__(self, lista):
        self.lista=lista
    
    def isEmpty(self):
        if len(self.lista)==0:
            return True
        else:
            return False
        
    def enqueue(self, x):
        self.lista.append(x)
    
    def dequeue(self):
        if self.is_empty():
            print("lista vuota")
            return None
        else:
            return self.lista.pop(0)

def main():
    lista="ciao"
    coda=Coda(lista)
    coda.enqueue(lista)

if __name__=="__main__":
    main()
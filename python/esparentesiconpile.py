def push(pila, elemento):
    pila.append(elemento)

def pop(pila):
    if len(pila) == 0:
        x= None
    else:
        x = pila.pop()
    return x

def main():
    parentesiAperte = ["{", "[", "("]
    parentesiChiuse = ["}", "]", ")"]
    dizionario = {"{":"}", "[":"]", "(":")"}
    stringa = "([)"
    pila = []
    errore = False
    a = 0
    posErrore = None

    for poscarattere, carattere in enumerate(stringa):
        if carattere in parentesiAperte:
            push(pila, carattere)
            a = a +1
        if carattere in parentesiChiuse:
            if a > 0:
                parentesi = pop(pila)
                if parentesi != None:
                    if dizionario[parentesi] != carattere:
                        errore = True
                        posErrore = poscarattere
                    else: 
                        a -= 1
                else:
                    errore = True 
                    posErrore = poscarattere
            else:
                errore = True
                posErrore = poscarattere

    if errore or a>0:        
        print(f"ERRORE in posizione {posErrore}")
    else:
        print("corretto!")

if __name__ == "__main__":
    main()
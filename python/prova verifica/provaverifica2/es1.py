import random

def numRand(lista):
    return random.choice(lista)

def totTempo(giorni):
    return 60*60*24*giorni

def main():
    listaCasual=-1, 1
    spostamento=[numRand(listaCasual) for _ in range(0, totTempo(5))]
    tot=0
    for i in spostamento:
        tot += i
    print(spostamento) 
    print(tot)

        

if __name__ == "__main__":
    main()

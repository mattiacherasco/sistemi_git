import sys

def stringRead(s):
    sTot=""
    s=sys.stdin.read(1)
    if(s!="-1"):
        sTot=sTot+s
        stringRead(s)
    else:
        
        return sTot
    

def getPattern(s):
    s=stringRead(s)
    print(s)

def main():
    sC=""
    sT=""
    print("frase: ")
    stringRead(sC)
    getPattern(sT)
    
if __name__=="__main__":
    main()
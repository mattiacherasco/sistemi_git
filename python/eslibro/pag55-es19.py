from math import sqrt
def mediaAlgebrica(num1, num2):
    return((num1+num2)/2)

def mediaGeometrica(num1, num2):
    return(pow(num1*num2, 1/2))

def main():
    num1 = int(input("inserire un numero: "))
    num2 = int(input("inserire un second numero: "))
    dizionario = {"Media aritmetica" : mediaAlgebrica(num1, num2), "Media geometrica" : mediaGeometrica(num1, num2)}
    print(dizionario)
if __name__ == "__main__":
    main()
def main():
    x=[0, 1, 2, 3, 5, 6, 7, 8]
    lung=len(x)/2
    lista1=x[:lung]
    lista2=x[lung:]

    print(f"{lista1}5{lista2}")
   

if __name__=="__main__":
    main()
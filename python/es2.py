def main():
    a = 10
    print(f"il tipo di  a è {type(a)}")
    if a > 5 :                           #<>
        print("a è maggiore di 5")
    elif (a<=5) and (a>=0):
        print("a  è maggiore di 0 e è minore o uguale di 5")
    else:
        print("a è minore di 0")

if __name__=="__main__":
    main()
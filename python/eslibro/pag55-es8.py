def main():

    s1 = input("inserisci una parola ")
    if len(s1) >= 8:
        print(s1[0:2] + "?" + s1[3:])
    else:
        print("La parola inserita non ha almeno 8 lettere.")
    
   

if __name__=="__main__":
    main()

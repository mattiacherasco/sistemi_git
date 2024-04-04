def main():
    max = 11
    power=[[k*i for i in range(1, max)] for k in range(1,max)]
    
    

    file=open("tabelline.txt", "w")
    for k, tabellina in enumerate(power):
        file.write(f"tabellina del {k+1}: {tabellina}\n")
        #enumerate numera le liste, ritorna indice e elemento
    file.close
if __name__=="__main__":
    main()
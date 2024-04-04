def main():
    sub=int(input("inserisci la subnet mask"))
    print(sub)
    subbin="1"*sub+"0"*(32-sub)
    print(subbin)
    group1=subbin[0:8]
    group2=subbin[8:16]
    group3=subbin[16:24]
    group4=subbin[24:32]
    group1=int(group1,2)
    group2=int(group2,2)
    group3=int(group3,2)
    group4=int(group4,2)
    ip=f"{group1}.{group2}.{group3}.{group4}"
    print(ip)

if __name__=="__main__":
    main()
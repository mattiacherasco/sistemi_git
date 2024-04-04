def completaOttobit(strbin):
    b=strbin[2:]
    return "0"*(8-len(b))+b

def main():
    ip=int(input("inserisci l'indirizzo ip"))
    group=ip.split(".")
    print(group)
    group=[int(group) for group in group]
    print(group)
    group_bin=[bin(group) for group in group]
    print(group_bin)
    print(completaOttobit(group_bin[3]))
    group_strbin=[completaOttobit(strbin) for strbin in group_bin]
    print(group_strbin)
    print(".".join(group_strbin))

if __name__=="__main__":
    main()
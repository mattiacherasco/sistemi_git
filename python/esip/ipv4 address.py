import ipaddress

def main():
    ipv4 = input("inserire un ipv4: ")
    subnetmask = input("inserire una subnet mask: ")
    ip = ipaddress.IPv4Address(ipv4)
    ipv4Pieno = ipv4 + subnetmask
    
    if ip.is_private == True:
        print("ip per indirizzi privati")
    else:
        print("ip non utilizzabili per inidirizzi privati")

    if ip.is_loopback == True:
        print("ip di loopback")
    else:
        print("ip non utilizzabile per il loopback")

    iprete = ipaddress.IPv4Network(ipv4Pieno, strict=False)
    if ipv4Pieno == str(iprete):
        print("ip di rete")
    else:
        print("ip non funzionali in rete")
    print(f"indirizzo di rete: {iprete}")
    hosts = list(iprete.hosts())
    print(f"il primo ip utilizzabile è: {hosts[0]}")
    print(f"l'ultimo ip utilizzabile è {hosts[-1]}")
    
if __name__ == "__main__":
    main()
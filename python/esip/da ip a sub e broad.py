def conversioneDecimale(ip_binario):
    gruppiDecimali = []
    for i in range(0, 32, 8):
        ottetto = ip_binario[i:i+8]
        gruppiDecimali.append(str(int(ottetto, 2)))
    return ".".join(gruppiDecimali)

def main():
    ip_address = input("inserire un ip di un dispositivo: ")
    cidr = int(input("inseire la notazione CIDR: "))
    subnet_mask = "1" * cidr + "0" * (32 - cidr)
    wild_card = "0" * cidr + "1" * (32 - cidr)
    subnet_maskDecimale = '.'.join(str(int(subnet_mask[i:i+8], 2)) for i in range(0, 32, 8))
    wild_cardDecimale = '.'.join(str(int(wild_card[i:i+8], 2)) for i in range(0, 32, 8))
    print(f"SubnetMask: " + subnet_maskDecimale)
    print(f"WildCard: " + wild_cardDecimale)
    # Indirizzo IP in formato binario
    ip_binary_groups = [format(int(x), '08b') for x in ip_address.split('.')]
    ip_binary = ''.join(ip_binary_groups)
    print(ip_binary_groups)
    print(ip_binary)
    ip_network = ip_binary[0:cidr] + "0" * (32 - cidr)
    ip_broadcast = ip_binary[0:cidr] + "1" * (32 - cidr)
    print(f"Ip rete: {conversioneDecimale(ip_network)}")
    print(f"Ip broadcast: {conversioneDecimale(ip_broadcast)}")

if __name__=="__main__":
    main()
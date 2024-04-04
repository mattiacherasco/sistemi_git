def main():
    ip_address = (input("inserire un ip di un dispositivo: "))
    wild_card = (input("inserire la wild card: "))

    # Indirizzo IP in formato binario
    ip_binary = ''.join(format(int(x), '08b') for x in ip_address.split('.'))

    # Subnet Mask in formato binario (supponiamo una subnet mask /24)
    wild_binary = ''.join(format(int(x), '08b') for x in wild_card.split('.'))

    # Esegui l'operazione OR tra l'indirizzo IP e la subnet mask
    result_binary = ''.join('1' if a == '1' or b == '1' else '0' for a, b in zip(ip_binary, wild_binary))

    # Converti il risultato binario in formato decimale
    result_decimal = '.'.join(str(int(result_binary[i:i+8], 2)) for i in range(0, 32, 8))

    print("Risultato OR [INDIRIZZO BROADCAST]: ", result_decimal)

    subnet_mask = input("inserire la subnetmask: ")
    subnet_binary = ''.join(format(int(x), '08b') for x in subnet_mask.split('.'))

    # Esegui l'operazione AND tra l'indirizzo IP e la subnet mask
    result_binaryAND = ''.join('1' if a == '1' and b == '1' else '0' for a, b in zip(ip_binary, subnet_binary))

    #Converti il risultato binario in formato decimale
    result_decimalAND = '.'.join(str(int(result_binaryAND[i:i+8], 2)) for i in range(0, 32, 8))

    print("Risultato AND [INDIRIZZO RETE]: ", result_decimalAND)


if __name__ == "__main__":
    main()
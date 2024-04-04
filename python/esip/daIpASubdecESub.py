#Data la lista ip_address=["192.168.222.0/27",
# "192,168.100.0/24","192.168.200.0/28","192.168.50.0/22"]
#crea un file “mask.txt”
# in cui salvi le subnet mask associate a ciascun indirizzo IP.

class CalcolaSubnet:
    def __init__(self, listaIp):
        self.listaIp=listaIp           
    
    def calcolaSubnetIp(self):
        with open("/home/mattia/scuola/sistemi/quarta/python_git/prova", "w",) as file:
            for elemento in self.listaIp:
                ip=elemento.split("/")
                subnet= "1" * int(ip[1]) + "0" * (32-int(ip[1]))
                subnetDec = '.'.join(str(int(subnet[i:i+8], 2)) for i in range(0, 32, 8))
                subnet= '.'.join(str(int(subnet[i:i+8])) for i in range(0, 32, 8))
                file.write(f"l'elemento {elemento}\nha come subnet {subnet}\nsubnet decimale {subnetDec}\n\n")
                                 
def main():
    listaIp = ["192.168.222.0/27","192,168.100.0/24","192.168.200.0/28","192.168.50.0/22"]
    calcolaSubnet=CalcolaSubnet(listaIp)
    calcolaSubnet.calcolaSubnetIp()
    
if __name__ == "__main__":
    main()
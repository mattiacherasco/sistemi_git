class Robot:
    def __init__(self, nome, massa, tipologia):
        self.nome = nome
        self.massa = massa
        self.tipologia = tipologia

    def controlloPericolo(self):
        if self.tipologia == "Umanoide" and self.massa > 100:
            return f"Il robot {self.nome} può essere pericoloso."
        else:
            return f"Il robot {self.nome} non è pericoloso."

    def descrizione(self):
        return f"Nome: {self.nome}, Massa: {self.massa}, Tipologia: {self.tipologia}"


def main():
    robot1 = Robot("RoboUno", 150, "Non-umanoide")
    print(robot1.descrizione())
    print(robot1.controlloPericolo())

    robot2 = Robot("RoboDue", 200, "Umanoide")
    print(robot2.descrizione())
    print(robot2.controlloPericolo())

if __name__=="__main__":
    main()
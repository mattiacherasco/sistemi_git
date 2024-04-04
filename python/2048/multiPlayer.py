import pygame
import numpy as np
import random
import socket
import select

class multiPlayerServer:
    def __init__(self):
        self.STARTWIDTH, self.STARTHEIGHT = 1000, 600
        self.WIDTH, self.HEIGHT = 400, 400
        self.ROWS, self.COLS = 4, 4
        self.TILE_SIZE = self.HEIGHT // self.ROWS
        self.WHITE = (250, 250, 250, 250)
        self.BLACK = (0, 0, 0, 0)
        self.COLORECOLONNE = (125, 125, 125, 255)
        self.COLORETABELLA = (200, 200, 200, 255)
        self.COLORENUMERI = self.COLORECOLONNE
        self.win = None
        self.grid = np.zeros((self.ROWS, self.COLS))
        self.score = 0
        self.name = ""
        self.opponentName = ""
        self.font = None
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def calculateScore(self, x):
        self.score += x
        print(self.score)
        
    def choseColor(self, number):
        colors = {
            2: (238, 228, 218, 255),
            4: (237, 224, 200, 255),
            8: (242, 177, 121, 255),
            16: (245, 149, 99, 255),
            32: (246, 124, 95, 255),
            64: (246, 94, 59, 255),
            128: (237, 207, 114, 255),
            256: (237, 204, 97, 255),
            512: (237, 200, 80, 255),
            1024: (237, 197, 63, 255),
            2048: (237, 197, 63, 255),
        }
        return colors.get(number, (0, 0, 0))

    def drawGrid(self):
        for row in range(self.ROWS):
            for col in range(self.COLS):
                pygame.draw.rect(self.win, self.COLORECOLONNE, (col * self.TILE_SIZE, row * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE), 2)
                val = self.grid[row][col]
                if val != 0:
                    pygame.draw.rect(self.win, self.choseColor(val), (col * self.TILE_SIZE + 5, row * self.TILE_SIZE + 5, self.TILE_SIZE - 10, self.TILE_SIZE - 10))
                    font = pygame.font.SysFont('Arial', 30)
                    text = font.render(str(int(val)), True, self.COLORENUMERI)
                    text_rect = text.get_rect(center=(col * self.TILE_SIZE + self.TILE_SIZE // 2, row * self.TILE_SIZE + self.TILE_SIZE // 2))
                    self.win.blit(text, text_rect)
    
    def generateTile(self):
        empty_cells = [(k, j) for k in range(self.ROWS) for j in range(self.COLS) if self.grid[k][j] == 0]
        if empty_cells:
            k, j = random.choice(empty_cells)
            self.grid[k][j] = 2 if random.random() < 0.9 else 4
 
    def moveLeft(self):
        moved = False
        for i in range(self.ROWS):
            for j in range(self.COLS - 1):
                for k in range(j + 1, self.COLS):
                    if self.grid[i][k] != 0:
                        if self.grid[i][j] == 0:
                            self.grid[i][j] = self.grid[i][k]
                            self.grid[i][k] = 0
                            moved = True
                        elif self.grid[i][j] == self.grid[i][k]:
                            self.grid[i][j] *= 2
                            self.calculateScore(self.grid[i][j])
                            self.grid[i][k] = 0
                            moved = True
                            break
                        else:
                            break
        if moved:
            self.generateTile()

    def moveRight(self):
        moved = False
        for i in range(self.ROWS):
            for j in range(self.COLS - 1, 0, -1):
                for k in range(j - 1, -1, -1):
                    if self.grid[i][k] != 0:
                        if self.grid[i][j] == 0:
                            self.grid[i][j] = self.grid[i][k]
                            self.grid[i][k] = 0
                            moved = True
                        elif self.grid[i][j] == self.grid[i][k]:
                            self.grid[i][j] *= 2
                            self.calculateScore(self.grid[i][j])
                            self.grid[i][k] = 0
                            moved = True
                            break
                        else:
                            break
        if moved:
            self.generateTile()

    def moveUp(self):
        moved = False
        for j in range(self.COLS):
            for i in range(self.ROWS - 1):
                for k in range(i + 1, self.ROWS):
                    if self.grid[k][j] != 0:
                        if self.grid[i][j] == 0:
                            self.grid[i][j] = self.grid[k][j]
                            self.grid[k][j] = 0
                            moved = True
                        elif self.grid[i][j] == self.grid[k][j]:
                            self.grid[i][j] *= 2
                            self.calculateScore(self.grid[i][j])
                            self.grid[k][j] = 0
                            moved = True
                            break
                        else:
                            break
        if moved:
            self.generateTile()

    def moveDown(self):
        moved = False
        for j in range(self.COLS):
            for i in range(self.ROWS - 1, 0, -1):
                for k in range(i - 1, -1, -1):
                    if self.grid[k][j] != 0:
                        if self.grid[i][j] == 0:
                            self.grid[i][j] = self.grid[k][j]
                            self.grid[k][j] = 0
                            moved = True
                        elif self.grid[i][j] == self.grid[k][j]:
                            self.grid[i][j] *= 2
                            self.calculateScore(self.grid[i][j])
                            self.grid[k][j] = 0
                            moved = True
                            break
                        else:
                            break
        if moved:
            self.generateTile()

    def isWin(self):
        if any(2048 in row for row in self.grid):
            self.conn.send("Win".encode())
            self.winGame()
        return

    def isEndGame(self):    
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.grid[i][j] == 0:
                    return  
        for i in range(self.ROWS):
            for j in range(self.COLS - 1):
                if self.grid[i][j] == self.grid[i][j+1]:
                    return 
        for i in range(self.ROWS - 1):
            for j in range(self.COLS):
                if self.grid[i][j] == self.grid[i+1][j]:
                    return  
        self.conn.send("Lose".encode())
        self.endGame() 

    def readNewName(self): 
        self.win = pygame.display.set_mode((self.STARTWIDTH, self.STARTHEIGHT))
        pygame.display.set_caption('2048 Instructions')
        self.font = pygame.font.Font(None, 24)
        running = True
        while running:
            self.win.fill(self.WHITE)
            text = [
                f"Giocatore1:{self.name}",
                "",
                f"Giocatore2:{self.opponentName}",
                "",
                "",
                "Premi SPAZIO se il tuo nome è inserito",
                "Premi INVIO se sei pronto alla sfida"
                   ]
            y_offset = 50
            for line in text:
                text_render = self.font.render(line, True, self.BLACK)
                self.win.blit(text_render, (20, y_offset))
                y_offset += 30
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        self.conn.send("Ready".encode())
                        stringReceived = self.conn.recv(1024)  
                        if stringReceived.decode() =="Ready":
                            self.game()
                    elif event.key == pygame.K_SPACE: 
                        self.conn.send(self.name.encode())  
                        stringReceived = self.conn.recv(1024)  
                        self.opponentName = stringReceived.decode() 
                    elif event.key == pygame.K_BACKSPACE:
                        self.name = self.name[:-1]
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                    else:
                        self.name += event.unicode

    def checkOther(self):
        sockets_list = [self.conn]
        readable, _, _ = select.select(sockets_list, [], [], 0.15) 
        for sock in readable:
            message = sock.recv(1024).decode()
            if message == "Stop":
                pygame.quit()
            elif message == "Lose":
                self.winGame()
            elif message == "Win":
                self.endGame()

    def connection(self):
        self.serverSocket.bind(('0.0.0.0', 12345))
        self.serverSocket.listen(1)
        self.conn, self.addr = self.serverSocket.accept()
        self.startGame()

    def startGame(self):
        self.readNewName()
        running = True
        while running:
            self.checkOther()
            self.win.fill(self.WHITE)
            text = [
                f"Benvenuti a 2048 {self.name}, {self.opponentName}!",
                "",
                "Regole del gioco:",
                "- Usa i tasti freccia per muovere i numeri nella griglia.",
                "- Combina i numeri uguali per ottenere numeri più alti.",
                f"- Ottieni un tassello 2048 per vincere e battere {self.opponentName}.",
                "",
                "Premi ESC per uscire dalla partita",
                "",
                "Premi INVIO per iniziare la partita"
            ]
            y_offset = 50
            for line in text:
                text_render = self.font.render(line, True, self.BLACK)
                self.win.blit(text_render, (20, y_offset))
                y_offset += 30
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.conn.send("Ready".encode())
                        if(self.conn.recv(1024).decode()=="Ready"):
                            self.game()
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        self.conn.send("Stop".encode())
                        return
        
    def game(self):
        self.generateTile()
        running = True
        pygame.display.set_caption('2048')
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        while running:
            self.checkOther()
            self.win.fill(self.COLORETABELLA)
            self.drawGrid()
            pygame.display.update()
            self.isEndGame()
            if self.isWin():
                pass
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.moveLeft()
                        elif event.key == pygame.K_RIGHT:
                            self.moveRight()
                        elif event.key == pygame.K_UP:
                            self.moveUp()
                        elif event.key == pygame.K_DOWN:
                            self.moveDown()
                        elif event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            self.conn.send("Stop".encode())
                            return

    def endGame(self):
        self.win = pygame.display.set_mode((self.STARTWIDTH, self.STARTHEIGHT))
        pygame.display.set_caption('2048 lose')
        running = True
        while running:
            self.win.fill(self.WHITE)
            text = [
                f"{self.name} hai perso!",
                self.drawGrid(),
                f"{self.opponentName} ha vinto"
                "",
                "Premi ESC per uscire"                
            ]
            y_offset = 50
            for line in text:
                text_render = self.font.render(line, True, self.BLACK)
                self.win.blit(text_render, (20, y_offset))
                y_offset += 30
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
                    
    def winGame(self):
        self.win = pygame.display.set_mode((self.STARTWIDTH, self.STARTHEIGHT))
        pygame.display.set_caption('2048 win')
        running = True
        while running:
            self.win.fill(self.WHITE)
            text = [
                f"{self.name} hai vinto!",
                self.drawGrid(),
                f"{self.opponentName} ha perso"
                "",
                "Premi ESC per uscire"                
            ]
            y_offset = 50
            for line in text:
                text_render = self.font.render(line, True, self.BLACK)
                self.win.blit(text_render, (20, y_offset))
                y_offset += 30
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return

class multiPlayerClient:
    def __init__(self):
        self.STARTWIDTH, self.STARTHEIGHT = 1000, 600
        self.WIDTH, self.HEIGHT = 400, 400
        self.ROWS, self.COLS = 4, 4
        self.TILE_SIZE = self.HEIGHT // self.ROWS
        self.WHITE = (250, 250, 250, 250)
        self.BLACK = (0, 0, 0, 0)
        self.COLORECOLONNE = (125, 125, 125, 255)
        self.COLORETABELLA = (200, 200, 200, 255)
        self.COLORENUMERI = self.COLORECOLONNE
        self.win = None
        self.grid = np.zeros((self.ROWS, self.COLS))
        self.score = 0
        self.name = ""
        self.opponentName = ""
        self.font = None
        self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def calculateScore(self, x):
        self.score += x
        print(self.score)
        
    def choseColor(self, number):
        colors = {
            2: (238, 228, 218, 255),
            4: (237, 224, 200, 255),
            8: (242, 177, 121, 255),
            16: (245, 149, 99, 255),
            32: (246, 124, 95, 255),
            64: (246, 94, 59, 255),
            128: (237, 207, 114, 255),
            256: (237, 204, 97, 255),
            512: (237, 200, 80, 255),
            1024: (237, 197, 63, 255),
            2048: (237, 197, 63, 255),
        }
        return colors.get(number, (0, 0, 0))

    def drawGrid(self):
        for row in range(self.ROWS):
            for col in range(self.COLS):
                pygame.draw.rect(self.win, self.COLORECOLONNE, (col * self.TILE_SIZE, row * self.TILE_SIZE, self.TILE_SIZE, self.TILE_SIZE), 2)
                val = self.grid[row][col]
                if val != 0:
                    pygame.draw.rect(self.win, self.choseColor(val), (col * self.TILE_SIZE + 5, row * self.TILE_SIZE + 5, self.TILE_SIZE - 10, self.TILE_SIZE - 10))
                    font = pygame.font.SysFont('Arial', 30)
                    text = font.render(str(int(val)), True, self.COLORENUMERI)
                    text_rect = text.get_rect(
                        center=(col * self.TILE_SIZE + self.TILE_SIZE // 2, row * self.TILE_SIZE + self.TILE_SIZE // 2))
                    self.win.blit(text, text_rect)
    
    def generateTile(self):
        empty_cells = [(k, j) for k in range(self.ROWS) for j in range(self.COLS) if self.grid[k][j] == 0]
        if empty_cells:
            k, j = random.choice(empty_cells)
            self.grid[k][j] = 2 if random.random() < 0.9 else 4
 
    def moveLeft(self):
        moved = False
        for i in range(self.ROWS):
            for j in range(self.COLS - 1):
                for k in range(j + 1, self.COLS):
                    if self.grid[i][k] != 0:
                        if self.grid[i][j] == 0:
                            self.grid[i][j] = self.grid[i][k]
                            self.grid[i][k] = 0
                            moved = True
                        elif self.grid[i][j] == self.grid[i][k]:
                            self.grid[i][j] *= 2
                            self.calculateScore(self.grid[i][j])
                            self.grid[i][k] = 0
                            moved = True
                            break
                        else:
                            break
        if moved:
            self.generateTile()

    def moveRight(self):
        moved = False
        for i in range(self.ROWS):
            for j in range(self.COLS - 1, 0, -1):
                for k in range(j - 1, -1, -1):
                    if self.grid[i][k] != 0:
                        if self.grid[i][j] == 0:
                            self.grid[i][j] = self.grid[i][k]
                            self.grid[i][k] = 0
                            moved = True
                        elif self.grid[i][j] == self.grid[i][k]:
                            self.grid[i][j] *= 2
                            self.calculateScore(self.grid[i][j])
                            self.grid[i][k] = 0
                            moved = True
                            break
                        else:
                            break
        if moved:
            self.generateTile()

    def moveUp(self):
        moved = False
        for j in range(self.COLS):
            for i in range(self.ROWS - 1):
                for k in range(i + 1, self.ROWS):
                    if self.grid[k][j] != 0:
                        if self.grid[i][j] == 0:
                            self.grid[i][j] = self.grid[k][j]
                            self.grid[k][j] = 0
                            moved = True
                        elif self.grid[i][j] == self.grid[k][j]:
                            self.grid[i][j] *= 2
                            self.calculateScore(self.grid[i][j])
                            self.grid[k][j] = 0
                            moved = True
                            break
                        else:
                            break
        if moved:
            self.generateTile()

    def moveDown(self):
        moved = False
        for j in range(self.COLS):
            for i in range(self.ROWS - 1, 0, -1):
                for k in range(i - 1, -1, -1):
                    if self.grid[k][j] != 0:
                        if self.grid[i][j] == 0:
                            self.grid[i][j] = self.grid[k][j]
                            self.grid[k][j] = 0
                            moved = True
                        elif self.grid[i][j] == self.grid[k][j]:
                            self.grid[i][j] *= 2
                            self.calculateScore(self.grid[i][j])
                            self.grid[k][j] = 0
                            moved = True
                            break
                        else:
                            break
        if moved:
            self.generateTile()

    def isWin(self):
        if any(2048 in row for row in self.grid):
            self.clientSocket.send("Win".encode())
            self.winGame()
        return

    def isEndGame(self):    
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.grid[i][j] == 0:
                    return  
        for i in range(self.ROWS):
            for j in range(self.COLS - 1):
                if self.grid[i][j] == self.grid[i][j+1]:
                    return 
        for i in range(self.ROWS - 1):
            for j in range(self.COLS):
                if self.grid[i][j] == self.grid[i+1][j]:
                    return  
        self.clientSocket.send("Lose".encode())
        self.endGame() 
            
    def readNewName(self): 
        self.win = pygame.display.set_mode((self.STARTWIDTH, self.STARTHEIGHT))
        pygame.display.set_caption('2048 Instructions')
        self.font = pygame.font.Font(None, 24)
        running = True
        while running:
            self.win.fill(self.WHITE)
            text = [
                f"Giocatore1:{self.name}",
                "",
                f"Giocatore2:{self.opponentName}",
                "",
                "",
                "Premi SPAZIO se il tuo nome è inserito",
                "Premi INVIO se sei pronto alla sfida"
                   ]
            y_offset = 50
            for line in text:
                text_render = self.font.render(line, True, self.BLACK)
                self.win.blit(text_render, (20, y_offset))
                y_offset += 30
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                        self.clientSocket.send("Ready".encode())
                        stringReceived = self.clientSocket.recv(1024)  
                        if stringReceived.decode() == "Ready":
                            self.game()
                    elif event.key == pygame.K_SPACE: 
                        self.clientSocket.send(self.name.encode())  
                        stringReceived = self.clientSocket.recv(1024)  
                        self.opponentName = stringReceived.decode() 
                    elif event.key == pygame.K_BACKSPACE:
                        self.name = self.name[:-1]
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                    else:
                        self.name += event.unicode

    def checkOther(self):
        sockets_list = [self.clientSocket]
        readable, _, _ = select.select(sockets_list, [], [], 0.15) 
        for sock in readable:
            message = sock.recv(1024).decode()
            if message == "Stop":
                pygame.quit()
            elif message == "Lose":
                self.winGame()
            elif message == "Win":
                self.endGame()

    def connection(self):
        ipAddress = ""
        running = True
        self.win = pygame.display.set_mode((self.STARTWIDTH, self.STARTHEIGHT))
        pygame.display.set_caption('2048 - Client Connection')
        self.font = pygame.font.Font(None, 24)
        while running:
            self.win.fill(self.WHITE)
            text = [
                "Inserisci l'indirizzo IP dell'avversario:",
                "",
                f"Indirizzo IP: {ipAddress}",
                "",
                "Premi INVIO per connetterti",
            ]
            y_offset = 50
            for line in text:
                text_render = self.font.render(line, True, self.BLACK)
                self.win.blit(text_render, (20, y_offset))
                y_offset += 30
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.clientSocket.connect((ipAddress, 12345))
                        self.startGame()
                    elif event.key == pygame.K_BACKSPACE:
                        ipAddress = ipAddress[:-1]
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                    else:
                        ipAddress += event.unicode
                if event.type == pygame.QUIT:
                    running = False

    def startGame(self):
        self.readNewName()
        running = True
        while running:
            self.checkOther()
            self.win.fill(self.WHITE)
            text = [
                f"Benvenuti a 2048 {self.name}, {self.opponentName}!",
                "",
                "Regole del gioco:",
                "- Usa i tasti freccia per muovere i numeri nella griglia.",
                "- Combina i numeri uguali per ottenere numeri più alti.",
                f"- Ottieni un tassello 2048 per vincere e battere {self.opponentName}.",
                "",
                "Premi ESC per uscire dalla partita",
                "",
                "Premi INVIO per iniziare la partita"
            ]
            y_offset = 50
            for line in text:
                text_render = self.font.render(line, True, self.BLACK)
                self.win.blit(text_render, (20, y_offset))
                y_offset += 30
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.clientSocket.send("Ready".encode())
                        if(self.clientSocket.recv(1024).decode()=="Ready"):
                            self.game()
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        self.clientSocket.send("Stop".encode())
                        return
        
    def game(self):
        self.generateTile()
        running = True
        pygame.display.set_caption('2048')
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        while running:
            self.checkOther()
            self.win.fill(self.COLORETABELLA)
            self.drawGrid()
            pygame.display.update()
            self.isEndGame()
            if self.isWin():
                pass
            else:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            self.moveLeft()
                        elif event.key == pygame.K_RIGHT:
                            self.moveRight()
                        elif event.key == pygame.K_UP:
                            self.moveUp()
                        elif event.key == pygame.K_DOWN:
                            self.moveDown()
                        elif event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            self.clientSocket.send("Stop".encode())
                            return

    def endGame(self):
        self.win = pygame.display.set_mode((self.STARTWIDTH, self.STARTHEIGHT))
        pygame.display.set_caption('2048 lose')
        running = True
        while running:
            self.win.fill(self.WHITE)
            text = [
                f"{self.name} hai perso!",
                self.drawGrid(),
                f"{self.opponentName} ha vinto"
                "",
                "Premi ESC per uscire"                
            ]
            y_offset = 50
            for line in text:
                text_render = self.font.render(line, True, self.BLACK)
                self.win.blit(text_render, (20, y_offset))
                y_offset += 30
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
                    
    def winGame(self):
        self.win = pygame.display.set_mode((self.STARTWIDTH, self.STARTHEIGHT))
        pygame.display.set_caption('2048 win')
        running = True
        while running:
            self.win.fill(self.WHITE)
            text = [
                f"{self.name} hai vinto!",
                self.drawGrid(),
                f"{self.opponentName} ha perso"
                "",
                "Premi ESC per uscire"                
            ]
            y_offset = 50
            for line in text:
                text_render = self.font.render(line, True, self.BLACK)
                self.win.blit(text_render, (20, y_offset))
                y_offset += 30
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
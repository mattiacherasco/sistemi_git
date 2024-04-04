import pygame
import numpy as np
import random

class singlePlayer:
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
        self.RECORDFILE = "record"
        self.win = None
        self.grid = np.zeros((self.ROWS, self.COLS))
        self.score = 0
        self.record = 0
        self.newName = ""
        self.name = "Player"
        self.font = None
        self.continua=False
        
    def loadRecord(self):
        with open(self.RECORDFILE, "r") as file:
            data = file.read().strip().split()
            if len(data) == 2:
                self.name = data[0]
                self.record = int(data[1])
            else:
                print("Il formato del file record non è valido.")
        return f"{self.name} che ha ottenuto un punteggio di {self.record}"

    def saveRecord(self, name, record):
        with open(self.RECORDFILE, "w") as file:
            file.write(f"{name} {int(record)}")
            
    def calculateScore(self, x):
        self.score += x
        print(self.score)

    def isWin(self):
        if not(self.continua):
            if any(2048 in row for row in self.grid):
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
        self.endGame() 
            
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
        for i in range(self.ROWS): # Itera attraverso le righe
            for j in range(self.COLS - 1): # Itera attraverso le colonne tranne l'ultima
                for k in range(j + 1, self.COLS): # Itera sulle colonne successive a quella attuale
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
        for i in range(self.ROWS): # Itera attraverso le righe della griglia
            for j in range(self.COLS - 1, 0, -1): # Itera attraverso le colonne in ordine inverso tranne la prima
                for k in range(j - 1, -1, -1):  # Itera attraverso le colonne in ordine inverso tranne la prima
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
        for j in range(self.COLS): # Itera attraverso le colonne della griglia
            for i in range(self.ROWS - 1): # Itera attraverso le righe tranne l'ultima
                for k in range(i + 1, self.ROWS): # Itera sulle righe successive a quella attuale
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
        for j in range(self.COLS): # Itera attraverso le colonne della griglia
            for i in range(self.ROWS - 1, 0, -1): # Itera attraverso le righe in ordine inverso tranne la prima
                for k in range(i - 1, -1, -1): # Itera sulle righe precedenti a quella attuale
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
        
    def readNewName(self):
        self.win = pygame.display.set_mode((self.STARTWIDTH, self.STARTHEIGHT))
        pygame.display.set_caption('2048 Instructions')
        self.font = pygame.font.Font(None, 24)
        running = True
        while running:
            self.win.fill(self.WHITE)
            text = [
                "Inserisci il tuo nome concorrente:",
                "",
                f"{self.newName}",
                "",
                "",
                "",
                "Premi INVIO se inserito"
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
                        return 
                    elif event.key == pygame.K_BACKSPACE:
                        self.newName = self.newName[:-1]
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                    else:
                        self.newName += event.unicode

    def startGame(self):
        self.readNewName()
        running = True
        while running:
            self.win.fill(self.WHITE)
            text = [
                f"Benvenuto a 2048 {self.newName}!",
                "",
                "Regole del gioco:",
                "- Usa i tasti freccia per muovere i numeri nella griglia.",
                "- Combina i numeri uguali per ottenere numeri più alti.",
                "- Ottieni un tassello 2048 per vincere.",
                "",
                "Premi ESC per uscire dalla partita",
                "",
                f"Prova a battere il record di {self.loadRecord()}",
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
                        self.game()
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
        
    def game(self):
        self.generateTile()
        running = True
        pygame.display.set_caption('2048')
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        while running:
            self.win.fill(self.COLORETABELLA)
            self.drawGrid()
            pygame.display.update()
            self.isEndGame()
            self.isWin()     
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
                    elif event.key == pygame.K_r:
                        self.__init__()
                        self.startGame()
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()

    def endGame(self):
        self.win = pygame.display.set_mode((self.STARTWIDTH, self.STARTHEIGHT))
        pygame.display.set_caption('2048 - Fine del gioco')
        self.name = self.newName
        self.loadRecord()  # Load record after updating self.name
        record = self.record  # Initialize record here
        if record < self.score:
            self.saveRecord(self.newName, self.score)
            self.record = self.score  # Update self.record with the new score
        record = self.record 
        running = True
        while running:
            self.win.fill(self.WHITE)
            text = [
                "La partita è terminata!",
                self.drawGrid(),
                "",
                f"Punteggio: {self.score}",
                f"Record: {record}",
                "",
                "Premi ESC per uscire dalla partita",
                "Premi R per iniziare una nuova partita"
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
                    if event.key == pygame.K_r:
                        self.__init__()
                        self.startGame()
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return
    def winGame(self):
        self.win = pygame.display.set_mode((self.STARTWIDTH, self.STARTHEIGHT))
        pygame.display.set_caption('2048 win')
        running = True
        while running:
            self.win.fill(self.WHITE)
            text = [
                f"{self.newName} hai vinto!",
                self.drawGrid(),
                "",
                "Premi INVIO per contnuare la partita",
                "",
                "Premi R per iniziare una nuova partita",
                "",
                "Premi ESC per uscire dalla partita",
                "",
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
                        self.continua=True
                        pygame.display.set_caption('2048')
                        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
                        return
                    if event.key == pygame.K_r:
                        self.__init__()
                        self.startGame()
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return

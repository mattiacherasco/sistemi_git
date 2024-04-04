import pygame
from singlePlayer import singlePlayer
from multiPlayer import multiPlayerClient
from multiPlayer import multiPlayerServer

WIDTH, HEIGHT = 1000, 600
WHITE = (250, 250, 250, 250)
LIGHTBLACK = (150, 150, 150, 150)
BLACK = (0, 0, 0, 0)
game = None

def choseMulti():
    global game
    font = pygame.font.Font(None, 30)
    selectedOption = 2
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('2048')
    running = True
    while running:
        win.fill(WHITE)
        text = [
                "seleziona per iniziare la partita",
                "",
                "Crea gruppo e invita l'avversaio",
                "Entra in un gruppo[fonisci il tuo ipAdress]",
            ]
        y_offset = 50
        for selected, line in enumerate(text):
            color = BLACK if selected == selectedOption else LIGHTBLACK
            text_render = font.render(line, True, color)
            win.blit(text_render, (20, y_offset))
            y_offset += 30
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selectedOption = (selectedOption - 1) % 2 + 2
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                elif event.key == pygame.K_DOWN:
                    selectedOption = (selectedOption + 1) % 2 + 2
                elif event.key == pygame.K_RETURN:
                    if selectedOption == 2:
                        game = multiPlayerClient()
                        return
                    elif selectedOption == 3:
                        game = multiPlayerServer()
                        return

def main():
    global game
    pygame.init()
    font = pygame.font.Font(None, 30)
    selectedOption = 2
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('2048')
    running = True
    while running:
        win.fill(WHITE)
        text = [
                "Seleziona modalità di gioco:",
                "",
                "singleplayer",
                "1 vs 1",
            ]
        y_offset = 50
        for idx, line in enumerate(text):
            color = BLACK if idx == selectedOption else (150, 150, 150, 150)
            text_render = font.render(line, True, color)
            win.blit(text_render, (20, y_offset))
            y_offset += 30
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selectedOption = (selectedOption - 1) % 2 + 2
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                elif event.key == pygame.K_DOWN:
                    selectedOption = (selectedOption + 1) % 2 + 2
                elif event.key == pygame.K_RETURN:
                    if selectedOption == 2:
                        game = singlePlayer()
                        game.startGame()
                    elif selectedOption == 3:
                        choseMulti()
                        game.connection()    

if __name__ == "__main__":
    main()

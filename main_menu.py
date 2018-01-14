import pygame

pygame.init()

display_width = 800
display_height = 600

white = (255, 255, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))

clock = pygame.time.Clock()

FPS = 60

class menu():

    menuscreen = pygame.image.load('menupics/menuscreen.png')
    menuscreen = pygame.transform.scale(menuscreen, (800, 600))
    play = pygame.image.load('menupics/play.png')
    play = pygame.transform.scale(play, (150, 80))
    playgreen = pygame.image.load('menupics/playgreen.png')
    playgreen = pygame.transform.scale(playgreen, (150, 80))
    quit = pygame.image.load('menupics/quit.png')
    quit = pygame.transform.scale(quit, (150, 80))
    quitred = pygame.image.load('menupics/quitred.png')
    quitred = pygame.transform.scale(quitred, (150, 80))

    def screen(self, mouse_pos, click):

        #x, y = pygame.mouse.get_pos()
        x, y = mouse_pos

        #print("X:",x)
       # print("Y:",y)
        if(x >= 320 and x <= 469 and y >= 220 and y <= 300): #play button
            gameDisplay.blit(self.menuscreen, (0, 0))
            gameDisplay.blit(self.playgreen, (320, 220))
            gameDisplay.blit(self.quit, (320, 310))
            if (click[0] == 1):
                from level1.level1 import level1
                level1.startLevel(level1)
                print("we out tbh")

        elif(x >= 320 and x <= 470 and y >= 310 and y <= 390):
            gameDisplay.blit(self.menuscreen, (0, 0))
            gameDisplay.blit(self.play, (320, 220))
            gameDisplay.blit(self.quitred, (320, 310))
            if (click[0] == 1):
                return True
        else:
            gameDisplay.blit(self.menuscreen, (0, 0))
            gameDisplay.blit(self.play, (320, 220))
            gameDisplay.blit(self.quit, (320, 310))

        return False

    def gameLoop(self):

        gameExit = False
        while(gameExit == False):
            for event in pygame.event.get():
                click = pygame.mouse.get_pressed()
                if(event.type == pygame.QUIT):
                    gameExit = True
                else:
                    gameDisplay.fill(white)
                    mouse_pos = pygame.mouse.get_pos()
                    gameExit = self.screen(mouse_pos, click)
                    pygame.display.update()
                    clock.tick(FPS)

b = menu()

b.gameLoop()
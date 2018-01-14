import pygame, time, random

pygame.init()

display_width = 800
display_height = 600

white = (255, 255, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))

clock = pygame.time.Clock()

FPS = 60

class level1():

    map = pygame.image.load('level1/map.png')
    playerModel = pygame.image.load('sprites/player.png')
    playerModel = pygame.transform.scale(playerModel, (70, 70))
    enemyUFOModel = pygame.image.load_extended('sprites/enemyUFO.png')
    enemyUFOModel = pygame.transform.scale(enemyUFOModel, (70, 70))
    greenLaser = pygame.image.load('sprites/laserGreen.png')
    greenLaser = pygame.transform.scale(greenLaser, (7, 12))

    laserSound = pygame.mixer.Sound("sounds/lasersound.wav")
    laserSound.set_volume(0.1)

    explosionSound = pygame.mixer.Sound("sounds/explosion.wav")
    explosionSound.set_volume(0.1)

    damageOnPlayer = pygame.mixer.Sound("sounds/damageOnPlayer.wav")
    damageOnPlayer.set_volume(0.1)

    detectedHitOnPlayer = False
    detectedHitOnEnemy = False
    health = 100

    playerLaserYList = []
    playerLaserXList = []

    enemyLaserYList = []
    enemyLaserXList = []
    
    enemyXList = []
    enemyYList = []

    lead_x = 380
    lead_y = 480

    laserY = 500

    start = 0


    def movement(self):

        lead_x_change = 0
        lead_y_change = 0

        playerHitDetected = False

        numOfLasers = 0
        numOfEnemies = 0

        currLaser = 0

        currEnemy = 0

        spaceDown = False

        while(True):
            for event in pygame.event.get():
                # Checks to see if any keys are held down and remembers them with the variable keys.
                keys = pygame.key.get_pressed()
                self.keyPressed = keys
                # If the palyer is holding down one key or the other the car moves in that direction
                if keys[pygame.K_LEFT]:
                    lead_x_change = -5
                    self.left = True
                    self.right = True
                    self.up = True
                    self.down = True
                if keys[pygame.K_RIGHT]:
                    lead_x_change = 5
                    self.right = True
                    self.up = True
                    self.down = True
                    self.left = False
                if keys[pygame.K_UP]:
                    lead_y_change = -5
                    self.up = True
                    self.down = True
                    self.left = False
                    self.right = False
                if keys[pygame.K_DOWN]:
                    lead_y_change = 5
                    self.down = True
                    self.left = False
                    self.right = False
                    self.up = False
                if event.type == pygame.KEYDOWN: #if spacebar is tapped, shoot laser
                    if event.key == pygame.K_SPACE:
                        spaceDown = True
                else:
                    spaceDown = False

                    # If the player is holding down both or neither of the keys the car stops
                if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
                    lead_x_change = 0
                if not keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
                    lead_x_change = 0
                if keys[pygame.K_UP] and keys[pygame.K_DOWN]:
                    lead_y_change = 0
                if not keys[pygame.K_UP] and not keys[pygame.K_DOWN]:
                    lead_y_change = 0
                if keys[pygame.K_UP] and (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
                    lead_y_change = 0
                    lead_x_change = 0
                if keys[pygame.K_DOWN] and (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
                    lead_y_change = 0
                    lead_x_change = 0


            self.lead_x += lead_x_change
            self.lead_y += lead_y_change

            self.start -= 1 #timer for spawning of enemy

            gameDisplay.fill(white)
            gameDisplay.blit(self.map, (0, 0))

            enemyIndex = 0

            #print(self.start)
            if(self.start <= 0):
                self.start = 80
                if(numOfEnemies <= 20):
                    xValue = random.randrange(10, 700)
                    yValue = random.randrange(10, 300)
                    self.enemyXList.append(xValue)
                    self.enemyYList.append(yValue)
                    self.enemyLaserXList.append(xValue)
                    self.enemyLaserYList.append(yValue)
                    print(numOfEnemies)
                    numOfEnemies +=1
                else:
                    if(currEnemy >= 20):
                        currEnemy = 0
                    xValue = random.randrange(10, 700)
                    yValue = random.randrange(10, 300)
                    self.enemyXList[currEnemy] = xValue
                    self.enemyYList[currEnemy] = yValue
                    self.enemyLaserXList[currEnemy] = xValue
                    self.enemyLaserYList[currEnemy] = yValue
                    currEnemy += 1


            enemyLaserIndex = 0
            for x in self.enemyLaserYList:
                self.enemyLaserYList[enemyLaserIndex] += 5
                self.enemy(self, self.enemyXList[enemyIndex], self.enemyYList[enemyIndex])
                self.shootLasers(self, self.enemyLaserXList[enemyIndex], self.enemyLaserYList[enemyIndex])
                laserHitDetected = self.hitDetectionOnPlayer(self, self.enemyLaserXList[enemyIndex], self.enemyLaserYList[enemyIndex], self.lead_x, self.lead_y)
                if (laserHitDetected == True):
                    self.enemyLaserXList[enemyIndex] = -50
                    self.enemyLaserYList[enemyIndex] = -50
                    self.damageOnPlayer.play()
                enemyLaserIndex += 1
                enemyIndex += 1

            self.player(self, self.lead_x, self.lead_y)

            index = 0 #go through each x and y value from the laser's list
            enemyIndex2 = 0 #go through each x and y value from the enemy list
            whichEnemy = 0

            if(spaceDown == True):
                #self.shootLasers(self, self.lead_x)
                self.laserSound.play()
                if(numOfLasers <= 20): #create no more than 20 lasers
                    self.playerLaserYList.append(500)
                    self.playerLaserXList.append(self.lead_x+30)
                    numOfLasers += 1
                else: #once 20 lasers are created then reset the value for the next laser starting at the first one
                    if(currLaser >= 20):
                        currLaser = 0
                    self.playerLaserYList[currLaser] = 500
                    self.playerLaserXList[currLaser] = self.lead_x+30
                    currLaser += 1
                spaceDown = False

            laserHitDetected = False
            #playerHitDetected = self.hitDetectionOnPlayer(self, 0, self.enemyXList, self.enemyYList, self.lead_x, self.lead_y)
            for x in self.playerLaserYList: #keep updating values of X and Y for each laser
                self.playerLaserYList[index] -= 5
                self.shootLasers(self, self.playerLaserXList[index], x)
                while(enemyIndex2 < len(self.enemyYList) and laserHitDetected == False):
                    laserHitDetected = self.hitDetectionOnEnemy(self, self.playerLaserXList[index],
                                                                self.playerLaserYList[index],
                                                                self.enemyXList[enemyIndex2],
                                                                self.enemyYList[enemyIndex2])
                    if(laserHitDetected == True):
                        whichEnemy = enemyIndex2
                        self.explosionSound.play()
                    enemyIndex2 += 1
                enemyIndex2 = 0
                if(laserHitDetected == True):
                    self.enemyXList[whichEnemy] = -50
                    self.enemyYList[whichEnemy] = -50
                    self.playerLaserXList[index] = -100
                    self.playerLaserYList[index] = -100
                if(playerHitDetected == True):
                    self.enemyXList = 0
                    self.enemyYList = -50

                index += 1
                laserHitDetected = False


            self.healthStatus(self)
            pygame.display.update()
            clock.tick(FPS)

    def player(self,  lead_x, lead_y):
        gameDisplay.blit(self.playerModel, (lead_x, lead_y))

    def enemy(self, lead_x, lead_y):
        gameDisplay.blit(self.enemyUFOModel, (lead_x, lead_y))

    def hitDetectionOnEnemy(self, laserX, laserY, enemyX, enemyY):
        if(laserX >= enemyX and laserX <= enemyX + 70 and laserY <= enemyY+20 and laserY >= enemyY):
            print("Hit detected")
            return True
        else:
            return False


    def hitDetectionOnPlayer(self, laserX, laserY, playerX, playerY):
        if (laserX >= playerX and laserX <= playerX + 70 and laserY <= playerY + 20 and laserY >= playerY):
            print("Hit detected")
            self.health -= 10
            return True
        else:
            return False

    def shootLasers(self, lead_x, lead_y):
        gameDisplay.blit(self.greenLaser, (lead_x, lead_y))


    def healthStatus(self):
        smallPlayerModel = pygame.transform.scale(self.playerModel, (20, 20))
        numOfModels = self.health/10
        lead_x = 500
        while(numOfModels >= 0):
            gameDisplay.blit(smallPlayerModel, (lead_x, 5))
            lead_x += 25
            numOfModels -= 1

    def startLevel(self):

        levelOver = False
        while(levelOver == False):
            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                    levelOver = True
            self.movement(self)
            pygame.display.update()
            clock.tick(FPS)


import pygame
import random
import time
import sys
import pauseMenu
from levelSettings import *
from level1 import Level1
from level2 import Level2
from level3 import Level3
from level4 import Level4
import gameObjects
import battleCalcs
import characterSelection
from debug import debug
import time

level1Trigger = True
level2Trigger = False
level3Trigger = False
level4Trigger = False
level1RunBool = False
level2RunBool = False
level3RunBool = False
level4RunBool = False
runMainLoop = True

storedAtk = 0

def setStoredAttack(atk):
    global storedAtk
    storedAtk = atk

def getStoredAttack():
    global storedAtk
    return storedAtk

def draw_text(screen, text, text_color, font_size, x, y):
    text_font = pygame.font.Font("kvn-pokemon-gen-5.ttf", font_size)
    img = text_font.render(text, True, text_color)
    screen.blit(img, (x, y))

def charSwap(heroSource, enemySource):
    swapCharScreen = pygame.display.set_mode((1280, 720))
    text_font = pygame.font.Font("kvn-pokemon-gen-5.ttf", 50)
    swapCharLoop = True
    while swapCharLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                swapCharLoop = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = pygame.mouse.get_pos()
                if (x > 500) and (x < 600) and (y > 500) and (y < 550):
                    swapCharLoop = False
                    return True
                elif (x > 680) and (x < 780) and (y > 500) and (y < 550):
                    swapCharLoop = False
                    return False
        swapCharScreen.fill((255, 255, 255))

        yesText = text_font.render("Yes", True, (0, 0, 0))
        yesText_rect = yesText.get_rect()
        yes_button = pygame.Rect(500, 500, 100, 50)
        yesText_rect.center = yes_button.center
        yesText_rect.x = yesText_rect.x - (yesText_rect.width / 2)
        yesText_rect.y = yesText_rect.y - (yesText_rect.height / 2)
        bg = pygame.image.load('bg2.jpg')
        bg_scaled=pygame.transform.scale(bg,(1280,720))
        noText = text_font.render("No", True, (0, 0, 0))
        noText_rect = noText.get_rect()
        no_button = pygame.Rect(680, 500, 100, 50)
        noText_rect.center = no_button.center
        noText_rect.x = noText_rect.x - (noText_rect.width / 2)
        noText_rect.y = noText_rect.y - (noText_rect.height / 2)

        heroImg = pygame.image.load(heroSource)
        heroImg = pygame.transform.scale(heroImg, (100, 100))
        heroImg_rect = heroImg.get_rect()

        enemyImg = pygame.image.load(enemySource)
        enemyImg = pygame.transform.scale(enemyImg,(100, 100))
        heroImg_rect = heroImg.get_rect()

        text = "Would you like to swap to the enemy character?"
        textPrint = text_font.render(text, True, (255, 0, 0))
        textPrint_rect = textPrint.get_rect()
        textPrint_rect.x = 640 - (textPrint_rect.width / 2)
    
        swapCharScreen.blit(bg_scaled,(0,0))

        swapCharScreen.blit(textPrint, (textPrint_rect.x, 45))
        swapCharScreen.blit(yesText, (yesText_rect.center))
        swapCharScreen.blit(noText, (noText_rect.center))
        swapCharScreen.blit(heroImg, (500, 380))
        swapCharScreen.blit(enemyImg, (680, 380))
     
        pygame.display.update()

def gameOver():
    gameOverScreen = pygame.display.set_mode((1280, 720))
    gameOverLoop = True
    while gameOverLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOverLoop = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = pygame.mouse.get_pos()
                if (x > 0) or (y > 0):
                    gameOverLoop = False
        gameOverScreen.fill((0, 0, 0))
        text = "Game Over!"
        text_font = pygame.font.Font("kvn-pokemon-gen-5.ttf", 50)
        textPrint = text_font.render(text, True, (255, 0, 0))
        textPrint_rect = textPrint.get_rect()
        gameOverScreen.blit(textPrint, (540, 315))
        pygame.display.update()



lebronStats = [85, 75, 60, 70]
lebronMoves = [[0, 100, 10, 1, 1, 0, "Chasedown Block"], [0, 50, 20, 2, 0, 0, "Yabadabadoo Old Navy"], [
    0, 100, 15, 3, 0, 0, "Cleveland!! This is for You!"], [100, 90, 10, 4, 0, 0, "Tomohawk Dunk"]]

luffyStats = [50, 90, 90, 60]
luffyMoves = [[10, 100, 5, 9, 0, 0, "Gatling Punch"], [40, 100, 20, 0, 1, 0, "Jet Pistol"], [
    150, 100, 5, 5, 0, 0, "Giant Pistol"], [0, 100, 5, 10, 0, 0, "Gear Change"]]

bruceStats = [90, 45, 45, 110]
bruceMoves = [[30, 100, 10, 0, 0, 0, "Leg Sweep"], [10, 100, 3, 12, 0, 0, "One Inch Punch"], [15, 100, 10, 0,
                                                                                              1, 0, "Lop Sao Backfist"], [0, 100, 10, 1, 1, 0, "Block"], [7, 100, 5, 9, 0, 15, "Lightning Fast Punches"]]

gruntStats = [40, 40, 40, 40]
gruntMoves = [[30, 100, 5, 4, 0, 0, "Shout"], [50, 100, 10, 0, 0, 0, "Punch"], [
    0, 100, 3, 3, 0, 0, "Get Angry"], [0, 100, 5, 16, 0, 0, "Stop Right There"]]

obamaStats = [45, 120, 25, 120]
obamaMoves = [[0, 100, 3, 7, 0, 0, "Let Me Be Clear"], [20, 100, 5, 17, 0, 0, "Campaign Trail Stomp"], [
    0, 100, 5, 16, 0, 0, "Landslide Victory"], [30, 100, 10, 14, 0, 0, "Endorsement Enforcement"]]

ohmStats = [100, 100, 100, 100]
ohmMoves = [[150, 100, 2, 5, 0, 0, "Super Ohio Throwdown"], [20, 100, 10, 6, 0, 0, "AtOHMic BOHMb"], [
    0, 50, 5, 7, 0, 0, "Attack of the ClOHMs"], [0, 100, 3, 8, 0, 0, "OHMazing Grace"]]

emStats = [70, 100, 50, 20]
emMoves = [[140, 100, 1, 0, 0, 15, "Killshot"], [20, 100, 10, 11, 0, 0, "Rap God"], [0, 100, 1, 13, 0, 0, "Not Afraid"], [
    10, 100, 5, 9, 0, 0, "8 Mile Melee"], [0, 100, 1, 13, 0, 0, "Till I Collapse"], [0, 50, 20, 2, 0, 10, "Music to Be Murdered By"]]

jackStats = [110, 50, 40, 70]
jackMoves = [[0, 100, 5, 1, 0, 0, "Drunken Dodge"], [90, 100, 3, 18, 0, 0, "Crash the Boat"], [
    40, 100, 5, 11, 0, 0, "Slash and Dash"], [0, 100, 1, 19, 0, 0, "Pillage"]]

sharkStats = [100, 30, 60, 70]
sharkMoves = [[0, 100, 10, 11, 0, 0, "Tidal Wave"], [0, 90, 5, 8, 0, 0, "Fish Feast"], [
    10, 100, 10, 0, 0, 0, "Bite"], [20, 100, 10, 6, 0, 0, "Puncture Prey"]]

bearStats = [40, 140, 80, 40]
bearMoves = [[60, 100, 10, 0, 0, 0, "Bite"], [0, 100, 10, 12, 0, 0, "Shake the Tree"], [0, 100, 1, 13, 0, 0,
                                                                                        "Bear Down"], [30, 100, 10, 14, 0, 0, "Berry Bush Beatdown"], [0, 100, 1, 15, 0, 15, "Unbearable Bunker"]]

hero = 0
heroLevel = 5000
grunt = 0
enemy = 0
miniBoss = 0
boss = 0
gruntLevel = heroLevel + 1000
miniBossLevel = heroLevel + 2000
bossLevel = heroLevel + 4000
charSelected = 0
healthLength = 215
playerAttackRectText = ""
enemyAttackRectText = ""

heroHealthBlock = 0
enemyHealthBlock = 0
heroStartingHealth = 0
heroHealthRect = 0
enemyHealthRect = 0
enemyStartingHealth = 0
xpBarStatus = 0
playerDmgText = ""
enemyDmgText = ""

miniBossXP = False
bossXP = False

class Game:

    def __init__(self):
        global lebronStats
        global lebronMoves
        global luffyStats
        global luffyMoves
        global bruceStats
        global bruceMoves
        global hero
        global charSelected
        global heroLevel

        heroLevel = 5000

        pygame.init()
        charSelected = characterSelection.charSelection()
        if (charSelected == 1):
            hero = battleCalcs.Fighter(
                lebronStats, lebronMoves, heroLevel, "lebron.png", "LeBron James")
        elif (charSelected == 2):
            hero = battleCalcs.Fighter(
                bruceStats, bruceMoves, heroLevel, "bruce_lee.png", "Bruce Lee")
        elif (charSelected == 3):
            hero = battleCalcs.Fighter(
                luffyStats, luffyMoves, heroLevel, "luffy.png", "Monkey D. Luffy")

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Super Ohio Throwdown")
        self.clock = pygame.time.Clock()

    def run(self):
        global level1Trigger, level2Trigger, level3Trigger, level4Trigger, level1RunBool, level2RunBool, level3RunBool, level4RunBool, runMainLoop
        nextLevelButton2 = True
        nextLevelButton3 = True
        nextLevelButton4 = True
        runOnce = True

        global lebronStats, lebronMoves
        global luffyStats, luffyMoves
        global bruceStats, bruceMoves
        global gruntStats, gruntMoves
        global obamaStats, obamaMoves
        global ohmStats, ohmMoves
        global emStats, emMoves
        global jackStats, jackMoves
        global sharkStats, sharkMoves
        global bearStats, bearMoves
        global hero, grunt, miniBoss, boss
        global enemy
        global heroLevel, miniBossLevel, bossLevel
        global storedAtk
        global playerAttackRectText, enemyAttackRectText, playerDmgText, enemyDmgText, miniBossXP, bossXP

        global heroHealthBlock, heroStartingHealth, heroHealthRect
        global enemyHealthBlock, enemyStartingHealth, enemyHealthRect
        global xpBarStatus

     
        battleLoopBool = False
        endBattle = False



        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB and runOnce == True:
                        level1Trigger = False
                        level2Trigger = True
                        runOnce = False
                    if event.key == pygame.K_ESCAPE and battleLoopBool == False:
                        
                        pauseMenu.p()
                        if pauseMenu.p()==True:
                            pygame.quit()
                            sys.exit()
                        pauseMenu.p()

            if gameObjects.endOfLevelOne == True:
                level2Trigger = True
                level1Trigger = False
                level3Trigger = False
                level4Trigger = False
                gameObjects.endOfLevelOne = False

            if gameObjects.endOfLevelTwo == True:
                level2Trigger = False
                level1Trigger = False
                level3Trigger = True
                level4Trigger = False

                gameObjects.miniBossFainted = False
                gameObjects.bossFainted = False
                gameObjects.endOfLevelTwo = False

            if gameObjects.endOfLevelThree == True:
                level2Trigger = False
                level1Trigger = False
                level3Trigger = False
                level4Trigger = True

                gameObjects.miniBossFainted = False
                gameObjects.bossFainted = False
                gameObjects.endOfLevelThree = False
            
            if gameObjects.endOfLevelFour == True:
                gameObjects.endOfLevelFour == False
                gameOver()
                pygame.quit()
                sys.exit()

            if level1Trigger == True:
                heroLevel = 5000
                gruntLevel = heroLevel + 1000
                grunt = battleCalcs.Fighter(
                    gruntStats, gruntMoves, gruntLevel, "grunt_battle.png", "Enemy Grunt")
                self.level1 = Level1()
                level1Trigger = False
                level1RunBool = True
                level2Trigger = False
                level2RunBool = False

            elif level2Trigger == True:
                nextLevelButton2 = False
                runMainLoop = False
                self.screen.fill('black')
                line1 = "As you escape from the high-security prison, you find yourself standing on the" 
                line2 = "wide beach with your mind filled with revenge. Suddenly, the notorious pirate," 
                line3 = "Jack Sparrow, and his crew appear before you, forcing you to fight for your"  
                line4 = "freedom and uncover the truth behind your incarceration. Will you be able to" 
                line5 = "defeat Jack Sparrow and uncover the secrets of your imprisonment?"

                line0 = "Continue"

                draw_text(self.screen, line1, (255, 255, 255), 30, 100, 100)
                draw_text(self.screen, line2, (255, 255, 255), 30, 100, 135)
                draw_text(self.screen, line3, (255, 255, 255), 30, 100, 170)
                draw_text(self.screen, line4, (255, 255, 255), 30, 100, 205)
                draw_text(self.screen, line5, (255, 255, 255), 30, 100, 240)
                draw_text(self.screen, line0, (255, 255, 255), 30, 590, 600)

                continueRectangle = pygame.draw.rect(
                    self.screen, "red", pygame.Rect(550, 600, 200, 60), 2)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x, y) = pygame.mouse.get_pos()
                    if (x >= 550) and (x <= 750) and (y >= 600) and (y <= 660):
                        nextLevelButton2 = True

                pygame.display.update()

                if nextLevelButton2 == True:
                    heroLevel = hero.level * 1000
                    gruntLevel = heroLevel + 1000
                    miniBossLevel = heroLevel + 2000
                    bossLevel = heroLevel + 4000
                    print(
                        "-------------------------------------------------------------------------")
                    print(heroLevel)
                    print(gruntLevel)
                    print(miniBossLevel)
                    print(bossLevel)
                    print(
                        "-------------------------------------------------------------------------")
                    grunt = battleCalcs.Fighter(
                        gruntStats, gruntMoves, gruntLevel, "grunt_battle.png", "Enemy Grunt")
                    miniBoss = battleCalcs.Fighter(
                        sharkStats, sharkMoves, miniBossLevel, "shark.png", "Shark")
                    boss = battleCalcs.Fighter(
                        jackStats, jackMoves, bossLevel, "jackSparrow.png", "Captain Sparrow")
                    self.level2 = Level2()
                    runMainLoop = True
                    level2Trigger = False
                    level2RunBool = True
                    level1RunBool = False
                    gameObjects.gruntLoopRunOnce = False
            elif level3Trigger == True:
                nextLevelButton3 = False
                runMainLoop = False
                self.screen.fill('black')

                line1 = "After defeating Jack Sparrow, he reveals a treasure map that leads you to the"   
                line2 = "corrupt former president, Obama's and Eminem's location in Detroit. With the"   
                line3 = "help of your newfound ally, you embark on a perilous journey through treacherous"    
                line4 = "terrain and dangerous enemies to uncover the truth behind the mysterious powerful"  
                line5 = "individual who corrupted Obama and Eminem. Can you defeat Obama and Eminem and" 
                line6 = "uncover the truth behind the powerful individual?"

                line0 = "Continue"

                draw_text(self.screen, line1, (255, 255, 255), 30, 100, 100)
                draw_text(self.screen, line2, (255, 255, 255), 30, 100, 135)
                draw_text(self.screen, line3, (255, 255, 255), 30, 100, 170)
                draw_text(self.screen, line4, (255, 255, 255), 30, 100, 205)
                draw_text(self.screen, line5, (255, 255, 255), 30, 100, 240)
                draw_text(self.screen, line6, (255, 255, 255), 30, 100, 275)
                draw_text(self.screen, line0, (255, 255, 255), 30, 590, 600)

                continueRectangle = pygame.draw.rect(
                    self.screen, "red", pygame.Rect(550, 600, 200, 60), 2)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x, y) = pygame.mouse.get_pos()
                    if (x >= 550) and (x <= 750) and (y >= 600) and (y <= 660):
                        nextLevelButton3 = True

                pygame.display.update()

                if nextLevelButton3 == True:
                    heroLevel = hero.level * 1000
                    gruntLevel = heroLevel + 1000
                    miniBossLevel = heroLevel + 2000
                    bossLevel = heroLevel + 4000
                    print(
                        "-------------------------------------------------------------------------")
                    print(heroLevel)
                    print(gruntLevel)
                    print(miniBossLevel)
                    print(bossLevel)
                    print(
                        "-------------------------------------------------------------------------")
                    grunt = battleCalcs.Fighter(
                        gruntStats, gruntMoves, gruntLevel, "grunt_battle.png", "Enemy Grunt")
                    miniBoss = battleCalcs.Fighter(
                        obamaStats, obamaMoves, miniBossLevel, "obama.png", "Barack Obama")
                    boss = battleCalcs.Fighter(
                        emStats, emMoves, bossLevel, "eminem.png", "Eminem")
                    
                    self.level3 = Level3()
                    runMainLoop = True
                    level3Trigger = False
                    level3RunBool = True
                    level2RunBool = False
                    gameObjects.miniBossLoopRunOnce = False
                    gameObjects.bossLoopRunOnce = False
                    gameObjects.gruntLoopRunOnce = False
            elif level4Trigger == True:
                nextLevelButton4 = False
                runMainLoop = False
                self.screen.fill('black')
                
                line1 = "After you defeat Eminem, he disables the forcefield surrounding Ohio allowing"   
                line2 = "you to enter. You feel the weight of the mission pressing down on you as you"  
                line3 = "enter the fiery wasteland, the lair of the final boss. The obstacles in your"   
                line4 = "path seem insurmountable, but you know that failure is not an option. With" 
                line5 = "each step, the heat intensifies, and the stakes grow higher. As you finally" 
                line6 = "come face to face with the final boss, his fiery aura blazes with an intensity" 
                line7 = "that threatens to consume you. Will you have what it takes to defeat this final" 
                line8 = "foe, uncover his true identity, and bring freedom to your country once and for" 
                line9 = "all? The fate of the land rests in your hands, hero."

                line0 = "Continue"

                draw_text(self.screen, line1, (255, 255, 255), 30, 100, 100)
                draw_text(self.screen, line2, (255, 255, 255), 30, 100, 135)
                draw_text(self.screen, line3, (255, 255, 255), 30, 100, 170)
                draw_text(self.screen, line4, (255, 255, 255), 30, 100, 205)
                draw_text(self.screen, line5, (255, 255, 255), 30, 100, 240)
                draw_text(self.screen, line6, (255, 255, 255), 30, 100, 275)
                draw_text(self.screen, line7, (255, 255, 255), 30, 100, 310)
                draw_text(self.screen, line8, (255, 255, 255), 30, 100, 345)
                draw_text(self.screen, line9, (255, 255, 255), 30, 100, 380)
                draw_text(self.screen, line0, (255, 255, 255), 30, 590, 600)

                continueRectangle = pygame.draw.rect(
                    self.screen, "red", pygame.Rect(550, 600, 200, 60), 2)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    (x, y) = pygame.mouse.get_pos()
                    if (x >= 550) and (x <= 750) and (y >= 600) and (y <= 660):
                        nextLevelButton4 = True

                pygame.display.update()

                if nextLevelButton4 == True:
                    heroLevel = hero.level * 1000
                    gruntLevel = heroLevel + 1000
                    miniBossLevel = heroLevel + 2000
                    bossLevel = heroLevel + 4000
                    print(
                        "-------------------------------------------------------------------------")
                    print(heroLevel)
                    print(gruntLevel)
                    print(miniBossLevel)
                    print(bossLevel)
                    print(
                        "-------------------------------------------------------------------------")
                    grunt = battleCalcs.Fighter(
                        gruntStats, gruntMoves, gruntLevel, "grunt_battle.png", "Enemy Grunt")
                    miniBoss = battleCalcs.Fighter(
                        bearStats, bearMoves, miniBossLevel, "grizzlyBear.png", "Grizzly Bear")
                    boss = battleCalcs.Fighter(
                        ohmStats, ohmMoves, bossLevel, "ohm.png", "Ohm")
                    
                    self.level4 = Level4()
                    runMainLoop = True
                    level4Trigger = False
                    level4RunBool = True
                    level3RunBool = False
                    gameObjects.miniBossLoopRunOnce = False
                    gameObjects.bossLoopRunOnce = False
                    gameObjects.gruntLoopRunOnce = False


            if gameObjects.battleLoopGrunt == True:
                enemy = grunt
                healthLength = 215
                heroHealthBlock = round(healthLength / hero.hp)
                enemyHealthBlock = round(healthLength / enemy.hp)
                heroStartingHealth = hero.hp
                enemyStartingHealth = enemy.hp                
                print(f"Grunt health: {enemy.tempHp}")
                print(f"Hero health: {hero.tempHp}")

                battleLoopBool = True
                gameObjects.battleLoopGrunt = False

            if gameObjects.battleLoopMiniBoss == True:
                miniBossXP = True
                enemy = miniBoss
                healthLength = 215
                heroHealthBlock = round(healthLength / hero.hp)
                enemyHealthBlock = round(healthLength / enemy.hp)
                heroStartingHealth = hero.hp
                enemyStartingHealth = enemy.hp

                battleLoopBool = True
                gameObjects.battleLoopMiniBoss = False
                
                

            if gameObjects.battleLoopBoss == True:
                bossXP = True
                enemy = boss
                healthLength = 215
                heroHealthBlock = round(healthLength / hero.hp)
                enemyHealthBlock = round(healthLength / enemy.hp)
                heroStartingHealth = hero.hp
                enemyStartingHealth = enemy.hp

                battleLoopBool = True
                gameObjects.battleLoopBoss = False

            if battleLoopBool:
                heroHealthBar = 0
                enemyHealthBar = 0
                newSwap = None
                pygame.mixer.music.load("battlemusic.mp3")

                pygame.mixer.music.set_volume(0.1)
                pygame.mixer.music.play(1)

                heroImg = pygame.image.load(hero.imageSource)
                heroImg = pygame.transform.flip(heroImg, True, False)
                heroImg_rect = heroImg.get_rect()
                gruntImg = pygame.image.load(enemy.imageSource)
                gruntImg_rect = heroImg.get_rect()
                battleBg = pygame.image.load("battleBgTemplate.jpg")
                battleBg_rect = battleBg.get_rect()
                battleBorder = pygame.image.load("battleBgBorder.png")
                battleScreen = pygame.display.set_mode(
                    (battleBg_rect.width, battleBg_rect.height))
                battleScreen_rect = battleScreen.get_rect()
                battleRunning = True
                battleFont = pygame.font.Font('kvn-pokemon-gen-5.ttf', 24)
                endMessageFont = pygame.font.Font('kvn-pokemon-gen-5.ttf', 48)

                heroHealthRect = (884, 408, heroHealthBar, 10)
                enemyHealthRect = (335, 152, enemyHealthBar, 10)
                xpBar = (810, 477, xpBarStatus, 12)

                attack1 = (100, 535, (battleScreen_rect.width - 300) / 2, 50)
                attack2 = ((battleScreen_rect.width / 2) + 50, 535,
                           (battleScreen_rect.width - 300) / 2, 50)
                attack3 = (100, 630, (battleScreen_rect.width - 300) / 2, 50)
                attack4 = ((battleScreen_rect.width / 2) + 50, 630,
                           (battleScreen_rect.width - 300) / 2, 50)

                while battleRunning:
                    
                    playerAttack = ""
                    playerEffect = 0
                    enemyAttack = ""
                    enemyEffect = 0
                    playerAttackRect = (25, 325, 225, 100)
                    enemyAttackRect = (1030, 75, 225, 100)
                    printMethod = False

                    heroHealthRect = (884, 408, heroHealthBar, 10)
                    enemyHealthRect = (335, 152, enemyHealthBar, 10)
                    xpBar = (810, 477, xpBarStatus, 12)
                    

                    # event loop
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            battleRunning = False
                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_BACKSPACE:
                                battleRunning = False
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            (x, y) = pygame.mouse.get_pos()
                            if ((x >= 100) and (x <= ((battleScreen_rect.width - 300) / 2) + 100) and (y >= 535) and (y <= 585)):
                                playerAttack = "attack1"
                            elif ((x >= (battleScreen_rect.width / 2) + 50) and (x <= ((battleScreen_rect.width - 300) / 2) + (battleScreen_rect.width / 2) + 50) and (y >= 535) and (y <= 585)):
                                playerAttack = "attack2"
                            elif ((x >= 100) and (x <= ((battleScreen_rect.width - 300) / 2) + 100) and (y >= 630) and (y <= 680)):
                                playerAttack = "attack3"
                            elif ((x >= (battleScreen_rect.width / 2) + 50) and (x <= ((battleScreen_rect.width - 300) / 2) + (battleScreen_rect.width / 2) + 50) and (y >= 630) and (y <= 680)):
                                playerAttack = "attack4"
                    

                    if (playerAttack != ""):
                        enemyMove = random.randint(1, 4)
                        print(hero.move1TempPP)
                        result = False
                        playerDmg = 0
                        enemyDmg = 0

                        if (playerAttack == "attack1"):
                            hero.move1TempPP -= 1
                            playerEffect == hero.move1effect
                            if enemyMove == 1:
                                result = battleCalcs.speedCalc(
                                    hero.move1priority, enemy.move1priority, hero.tempSpd, enemy.tempSpd)
                                enemy.move1TempPP -= 1
                            elif enemyMove == 2:
                                result = battleCalcs.speedCalc(
                                    hero.move1priority, enemy.move2priority, hero.tempSpd, enemy.tempSpd)
                                enemy.move2TempPP -= 1
                            elif enemyMove == 3:
                                result = battleCalcs.speedCalc(
                                    hero.move1priority, enemy.move3priority, hero.tempSpd, enemy.tempSpd)
                                enemy.move3TempPP -= 1
                            elif enemyMove == 4:
                                result = battleCalcs.speedCalc(
                                    hero.move1priority, enemy.move4priority, hero.tempSpd, enemy.tempSpd)
                                enemy.move4TempPP -= 1
                        elif (playerAttack == "attack2"):
                            hero.move2TempPP -= 1
                            playerEffect == hero.move2effect
                            if enemyMove == 1:
                                result = battleCalcs.speedCalc(
                                    hero.move2priority, enemy.move1priority, hero.tempSpd, enemy.tempSpd)
                                enemy.move1TempPP -= 1
                            elif enemyMove == 2:
                                result = battleCalcs.speedCalc(
                                    hero.move2priority, enemy.move2priority, hero.tempSpd, enemy.tempSpd)
                                enemy.move2TempPP -= 1
                            elif enemyMove == 3:
                                result = battleCalcs.speedCalc(
                                    hero.move2priority, enemy.move3priority, hero.tempSpd, enemy.tempSpd)
                                enemy.move3TempPP -= 1
                            elif enemyMove == 4:
                                result = battleCalcs.speedCalc(
                                    hero.move2priority, enemy.move4priority, hero.tempSpd, enemy.tempSpd)
                                enemy.move4TempPP -= 1
                        elif (playerAttack == "attack3"):
                            hero.move3TempPP -= 1
                            playerEffect == hero.move3effect
                            if enemyMove == 1:
                                result = battleCalcs.speedCalc(
                                    hero.move3priority, enemy.move1priority, hero.tempSpd, enemy.tempSpd)
                                enemy.move1TempPP -= 1
                            elif enemyMove == 2:
                                result = battleCalcs.speedCalc(
                                    hero.move3priority, enemy.move2priority, hero.tempSpd, enemy.tempSpd)
                                enemy.move2TempPP -= 1
                            elif enemyMove == 3:
                                result = battleCalcs.speedCalc(
                                    hero.move3priority, enemy.move3priority, hero.tempSpd, enemy.tempSpd)
                                enemy.move3TempPP -= 1
                            elif enemyMove == 4:
                                result = battleCalcs.speedCalc(
                                    hero.move3priority, enemy.move4priority, hero.tempSpd, enemy.tempSpd)
                                enemy.move4TempPP -= 1
                        elif (playerAttack == "attack4"):
                            hero.move4TempPP -= 1
                            playerEffect == hero.move4effect
                            if enemyMove == 1:
                                result = battleCalcs.speedCalc(
                                    hero.move4priority, enemy.move1priority, hero.tempSpd, enemy.tempSpd)
                                enemy.move1TempPP -= 1
                            elif enemyMove == 2:
                                result = battleCalcs.speedCalc(
                                    hero.move4priority, enemy.move2priority, hero.tempSpd, enemy.tempSpd)
                                enemy.move2TempPP -= 1
                            elif enemyMove == 3:
                                result = battleCalcs.speedCalc(
                                    hero.move4priority, enemy.move3priority, hero.tempSpd, enemy.tempSpd)
                                enemy.move3TempPP -= 1
                            elif enemyMove == 4:
                                result = battleCalcs.speedCalc(
                                    hero.move4priority, enemy.move4priority, hero.tempSpd, enemy.tempSpd)
                                enemy.move4TempPP -= 1

                        if (result):
                            if (playerAttack == "attack1" and hero.move1TempPP > 0):
                                Game.effectCheck(hero.move1effect, hero, enemy)
                                playerDmg = battleCalcs.damageCalc(
                                    hero.tempAtk, hero.move1bp, hero.level, enemy.tempDfs)
                                playerAttackRectText = f"Move: {hero.move1name}"
                                Game.afterEffectCheck(hero.move1effect, hero, enemy, playerDmg)
                            elif (playerAttack == "attack2" and hero.move2TempPP > 0):
                                Game.effectCheck(hero.move2effect, hero, enemy)
                                playerDmg = battleCalcs.damageCalc(hero.tempAtk, hero.move2bp, hero.level, enemy.tempDfs)
                                playerAttackRectText = f"Move: {hero.move2name}"
                                Game.afterEffectCheck(hero.move2effect, hero, enemy, playerDmg)
                            elif (playerAttack == "attack3" and hero.move3TempPP > 0):
                                Game.effectCheck(hero.move3effect, hero, enemy)
                                playerDmg = battleCalcs.damageCalc(
                                    hero.tempAtk, hero.move3bp, hero.level, enemy.tempDfs)
                                playerAttackRectText = f"Move: {hero.move3name}"
                                Game.afterEffectCheck(hero.move3effect, hero, enemy, playerDmg)
                            elif (playerAttack == "attack4" and hero.move4TempPP > 0):
                                Game.effectCheck(hero.move4effect, hero, enemy)
                                playerDmg = battleCalcs.damageCalc(
                                    hero.tempAtk, hero.move4bp, hero.level, enemy.tempDfs)
                                playerAttackRectText = f"Move: {hero.move4name}"
                                Game.afterEffectCheck(hero.move4effect, hero, enemy, playerDmg)
                            else:
                                print ("out of PP")
                                playerDmg = 0
                            
                            playerDmgText = f"Damage: {playerDmg}"

                            if (enemy.isProtected == False):
                                enemy.tempHp = enemy.tempHp - playerDmg
                            else:
                                enemy.isProtected = False

                            if (hero.turnsOfChipLeft > 0):
                                    enemy.tempHp -= ((1/16) * enemy.hp)
                                    print(f"the enemy lost {((1/16) * enemy.hp)} to chip")
                                    print(f"turns remaining: {hero.turnsOfChipLeft}")
                                    hero.turnsOfChipLeft -= 1

                            if (enemy.tempHp <= 0 ):
                                enemyHealthBar = 215
                            else:
                                enemyHealthBar = (enemyStartingHealth - enemy.tempHp) * enemyHealthBlock

                            if (enemy.tempHp < 0):
                                if (enemyHealthBar >= 215):
                                    enemyHealthBar = 215
                                heroHealthRect = (884, 408, heroHealthBar, 10)
                                enemyHealthRect = (
                                    335, 152, enemyHealthBar, 10)
                                pygame.draw.rect(
                                    battleScreen, (255, 0, 0), heroHealthRect)
                                pygame.draw.rect(
                                    battleScreen, (255, 0, 0), enemyHealthRect)
                                battleScreen.blit(battleBorder, (0, 500))
                                battleText = pygame.font.Font.render(
                                    endMessageFont, "The enemy fainted!", True, (255, 255, 255))
                                battleScreen.blit(battleText, (50, 550))
                                hero.afterWin((hero.level * 1000) + 1000)
                                if (miniBossXP):
                                   hero.afterWin((hero.level * 1000 ) + 1000)
                                   miniBossXP = False     
                                
                                if (bossXP):
                                   hero.afterWin((hero.level * 1000 ) + 2000)
                                   bossXP = False     
                                
                                hero.reset()

                                for i in range(41):
                                    xpBarStatus = xpBarStatus + 7
                                    xpBar = (810, 477, xpBarStatus, 12)
                                    pygame.draw.rect(battleScreen, (130, 243, 243), xpBar)
                                    time.sleep(0.1)
                                    pygame.display.update()
                                for i in range(5):
                                    pygame.draw.rect(battleScreen, (247, 234, 40), xpBar)
                                    time.sleep(0.1)
                                    pygame.display.update()
                                    pygame.draw.rect(battleScreen, (130, 243, 243), xpBar)
                                    time.sleep(0.1)
                                    pygame.display.update()
                                battleScreen.blit(battleBorder, (0, 500))
                                battleText = pygame.font.Font.render(
                                    endMessageFont, "You leveled up!", True, (255, 255, 255))
                                battleScreen.blit(battleText, (50, 550))
                                print(f"Hero health: {hero.tempHp}")
                                enemy.afterWin(enemy.level * 1000)
                                enemy.reset()
                                print(f"Grunt health: {enemy.tempHp}")
                                time.sleep(1)
                                endBattle = True
                                pygame.display.update()

                                while (endBattle == True):
                                    pygame.mixer.music.load("battlemusic.mp3")

                                    pygame.mixer.music.set_volume(0)
                                    pygame.mixer.music.play(1)
                                    xpBarStatus = 0
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            battleRunning = False
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            (x, y) = pygame.mouse.get_pos()
                                            if ((x >= 0) and (x <= 1280) and (y >= 500) and (y <= 720) and (endBattle == True)):
                                                heroSwapped = charSwap(hero.imageSource, enemy.imageSource)
                                                if (heroSwapped):
                                                    hero = enemy
                                                    endBattle = False
                                                    battleRunning = False
                                                else:
                                                    endBattle = False
                                                    battleRunning = False
                                                hero.usedBlockLast = False
                                                hero.isProtected = False
                                                hero.isChargingUp = True
                                                hero.turnsOfChipLeft = 0
                                
                                endBattle = True
                                pygame.display.update()

                            else:
                                if (enemyMove == 1 and enemy.move1TempPP > 0):
                                    Game.effectCheck(enemy.move1effect, enemy, hero)
                                    enemyDmg = battleCalcs.damageCalc(
                                        enemy.tempAtk, enemy.move1bp, enemy.level, hero.tempDfs)
                                    enemyAttackRectText = f"Move: {enemy.move1name}"
                                    print("PP: " + str(enemy.move1TempPP))
                                    Game.afterEffectCheck(enemy.move1effect, hero, enemy, enemyDmg)
                                elif (enemyMove == 2 and enemy.move2TempPP > 0):
                                    Game.effectCheck(enemy.move2effect, enemy, hero)
                                    enemyDmg = battleCalcs.damageCalc(
                                        enemy.tempAtk, enemy.move2bp, enemy.level, hero.tempDfs)
                                    print("PP: " + str(enemy.move2TempPP))
                                    enemyAttackRectText = f"Move: {enemy.move2name}"
                                    Game.afterEffectCheck(enemy.move2effect, hero, enemy, enemyDmg)
                                elif (enemyMove == 3 and enemy.move3TempPP > 0):
                                    Game.effectCheck(enemy.move3effect, enemy, hero)
                                    enemyDmg = battleCalcs.damageCalc(
                                        enemy.tempAtk, enemy.move3bp, enemy.level, hero.tempDfs)
                                    enemyAttackRectText = f"Move: {enemy.move3name}"
                                    Game.afterEffectCheck(enemy.move3effect, hero, enemy, enemyDmg)
                                elif (enemyMove == 4 and enemy.move4TempPP > 0):
                                    Game.effectCheck(enemy.move4effect, enemy, hero)
                                    enemyDmg = battleCalcs.damageCalc(
                                        enemy.tempAtk, enemy.move4bp, enemy.level, hero.tempDfs)
                                    enemyAttackRectText = f"Move: {enemy.move4name}"
                                    Game.afterEffectCheck(enemy.move4effect, hero, enemy, enemyDmg)
                                
                                enemyDmgText = f"Damage: {enemyDmg}"

                                if (hero.isProtected == False):
                                        hero.tempHp = hero.tempHp - enemyDmg
                                else:
                                    hero.isProtected = False  

                                if (enemy.turnsOfChipLeft > 0):
                                    hero.tempHp -= ((1/16) * hero.hp)
                                    print(f"the hero lost {((1/16) * hero.hp)} to chip")
                                    print(f"turns remaining: {enemy.turnsOfChipLeft}")
                                    enemy.turnsOfChipLeft -= 1  

                                heroHealthBar = (
                                    heroStartingHealth - hero.tempHp) * heroHealthBlock
                                # If player HP is empty, end of battle process starts
                                if (hero.tempHp < 0):
                                    if (heroHealthBar >= 215):
                                        heroHealthBar = 215
                                    heroHealthRect = (
                                        884, 408, heroHealthBar, 10)
                                    enemyHealthRect = (
                                        335, 152, enemyHealthBar, 10)
                                    pygame.draw.rect(
                                        battleScreen, (255, 0, 0), heroHealthRect)
                                    pygame.draw.rect(
                                        battleScreen, (255, 0, 0), enemyHealthRect)
                                    battleScreen.blit(battleBorder, (0, 500))
                                    battleText = pygame.font.Font.render(
                                        endMessageFont, "You fainted!", True, (255, 255, 255))
                                    battleScreen.blit(battleText, (50, 550))
                                    endBattle = True
                                    pygame.display.update()

                                    while (endBattle == True):
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                battleRunning = False
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                (x, y) = pygame.mouse.get_pos()
                                                if ((x >= 0) and (x <= 1280) and (y >= 500) and (y <= 720) and (endBattle == True)):
                                                    gameOver()
                                                    time.sleep(2)
                                                    endBattle = False
                                                    battleRunning = False
                                                    pygame.quit()
                                                    sys.exit()
                                                hero.usedBlockLast = False
                                                hero.isProtected = False
                                                hero.isChargingUp = True
                                                hero.turnsOfChipLeft = 0
                        elif (result == False):
                            if (enemyMove == 1):
                                Game.effectCheck(enemy.move1effect, enemy, hero)
                                enemyDmg = battleCalcs.damageCalc(
                                    enemy.tempAtk, enemy.move1bp, enemy.level, hero.tempDfs)
                                enemyAttackRectText = f"Move: {enemy.move1name}"
                                Game.afterEffectCheck(enemy.move1effect, hero, enemy, enemyDmg)
                            elif (enemyMove == 2):
                                Game.effectCheck(enemy.move2effect, enemy, hero)
                                enemyDmg = battleCalcs.damageCalc(
                                    enemy.tempAtk, enemy.move2bp, enemy.level, hero.tempDfs)
                                enemyAttackRectText = f"Move: {enemy.move2name}"
                                Game.afterEffectCheck(enemy.move2effect, hero, enemy, enemyDmg)
                            elif (enemyMove == 3):
                                Game.effectCheck(enemy.move3effect, enemy, hero)
                                enemyDmg = battleCalcs.damageCalc(
                                    enemy.tempAtk, enemy.move3bp, enemy.level, hero.tempDfs)
                                enemyAttackRectText = f"Move: {enemy.move3name}"
                                Game.afterEffectCheck(enemy.move3effect, hero, enemy, enemyDmg)
                            elif (enemyMove == 4):
                                Game.effectCheck(enemy.move4effect, enemy, hero)
                                enemyDmg = battleCalcs.damageCalc(
                                    enemy.tempAtk, enemy.move4bp, enemy.level, hero.tempDfs)
                                enemyAttackRectText = f"Move: {enemy.move4name}"
                                Game.afterEffectCheck(enemy.move4effect, hero, enemy, enemyDmg)

                            enemyDmgText = f"Damage: {enemyDmg}"
                            
                            if (hero.isProtected == False):
                                    hero.tempHp = hero.tempHp - enemyDmg
                            else:
                                    hero.isProtected = False  

                            if (enemy.turnsOfChipLeft > 0):
                                    hero.tempHp -= ((1/16) * hero.hp)
                                    print(f"the hero lost {((1/16) * hero.hp)} to chip")
                                    print(f"turns remaining: {enemy.turnsOfChipLeft}")
                                    enemy.turnsOfChipLeft -= 1

                            heroHealthBar = (
                                heroStartingHealth - hero.tempHp) * heroHealthBlock
                            # If player HP is empty, end of battle process starts
                            if (hero.tempHp < 0):
                                pygame.mixer.music.load("battlemusic.mp3")

                                pygame.mixer.music.set_volume(0)
                                pygame.mixer.music.play(1)
                                if (heroHealthBar >= 215):
                                    heroHealthBar = 215
                                heroHealthRect = (884, 408, heroHealthBar, 10)
                                enemyHealthRect = (
                                    335, 152, enemyHealthBar, 10)
                                pygame.draw.rect(
                                    battleScreen, (255, 0, 0), heroHealthRect)
                                pygame.draw.rect(
                                    battleScreen, (255, 0, 0), enemyHealthRect)
                                battleScreen.blit(battleBorder, (0, 500))
                                battleText = pygame.font.Font.render(
                                    endMessageFont, "You fainted!", True, (255, 255, 255))
                                battleScreen.blit(battleText, (50, 550))
                                endBattle = True
                                pygame.display.update()

                                while (endBattle == True):
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            battleRunning = False
                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                            (x, y) = pygame.mouse.get_pos()
                                            if ((x >= 0) and (x <= 1280) and (y >= 500) and (y <= 720) and (endBattle == True)):
                                                gameOver()
                                                time.sleep(2)
                                                endBattle = False
                                                battleRunning = False
                                                pygame.quit()
                                                sys.exit()
                                            hero.usedBlockLast = False
                                            hero.isProtected = False
                                            hero.isChargingUp = True
                                            hero.turnsOfChipLeft = 0
                            else:
                                if (playerAttack == "attack1"):
                                    Game.effectCheck(hero.move1effect, hero, enemy)
                                    playerDmg = battleCalcs.damageCalc(
                                        hero.tempAtk, hero.move1bp, hero.level, enemy.tempDfs)
                                    playerAttackRectText = f"Move: {hero.move1name}"
                                    Game.afterEffectCheck(hero.move1effect, hero, enemy, playerDmg)
                                elif (playerAttack == "attack2"):
                                    Game.effectCheck(hero.move2effect, hero, enemy)
                                    playerDmg = battleCalcs.damageCalc(
                                        hero.tempAtk, hero.move2bp, hero.level, enemy.tempDfs)
                                    playerAttackRectText = f"Move: {hero.move2name}"
                                    Game.afterEffectCheck(hero.move2effect, hero, enemy, playerDmg)
                                elif (playerAttack == "attack3"):
                                    Game.effectCheck(hero.move3effect, hero, enemy)
                                    playerDmg = battleCalcs.damageCalc(
                                        hero.tempAtk, hero.move3bp, hero.level, enemy.tempDfs)
                                    playerAttackRectText = f"Move: {hero.move3name}"
                                    Game.afterEffectCheck(hero.move3effect, hero, enemy, playerDmg)
                                elif (playerAttack == "attack4"):
                                    Game.effectCheck(hero.move4effect, hero, enemy)
                                    playerDmg = battleCalcs.damageCalc(
                                        hero.tempAtk, hero.move4bp, hero.level, enemy.tempDfs)
                                    playerAttackRectText = f"Move: {hero.move4name}"
                                    Game.afterEffectCheck(hero.move4effect, hero, enemy, playerDmg)

                                playerDmgText = f"Damage: {playerDmg}"

                                if (enemy.isProtected == False):
                                        enemy.tempHp = enemy.tempHp - playerDmg
                                else:
                                    enemy.isProtected = False  

                                if (hero.turnsOfChipLeft > 0):
                                    enemy.tempHp -= ((1/16) * enemy.hp)
                                    print(f"the enemy lost {((1/16) * enemy.hp)} to chip")
                                    print(f"turns remaining: {hero.turnsOfChipLeft}")
                                    hero.turnsOfChipLeft -= 1


                                enemyHealthBar = (
                                    enemyStartingHealth - enemy.tempHp) * enemyHealthBlock
                                # If enemy HP is empty, end of battle process starts
                                if (enemy.tempHp < 0):
                                    pygame.mixer.music.load("battlemusic.mp3")

                                    pygame.mixer.music.set_volume(0)
                                    pygame.mixer.music.play(1)
                                    if (enemyHealthBar >= 215):
                                        enemyHealthBar = 215
                                    heroHealthRect = (
                                        884, 408, heroHealthBar, 10)
                                    enemyHealthRect = (
                                        335, 152, enemyHealthBar, 10)
                                    pygame.draw.rect(
                                        battleScreen, (255, 0, 0), heroHealthRect)
                                    pygame.draw.rect(
                                        battleScreen, (255, 0, 0), enemyHealthRect)
                                    battleScreen.blit(battleBorder, (0, 500))
                                    battleText = pygame.font.Font.render(
                                        endMessageFont, "Enemy fainted!", True, (255, 255, 255))
                                    battleScreen.blit(battleText, (50, 550))
                                    hero.afterWin((hero.level * 1000) + 1000)
                                    if (miniBossXP):
                                        hero.afterWin((hero.level * 1000 ) + 1000)
                                        miniBossXP = False     
                                    
                                    if (bossXP):
                                        hero.afterWin((hero.level * 1000 ) + 2000)
                                        bossXP = False     
                                    
                                    hero.reset()

                                    for i in range(41):
                                        xpBarStatus = xpBarStatus + 7
                                        xpBar = (810, 477, xpBarStatus, 12)
                                        pygame.draw.rect(battleScreen, (130, 243, 243), xpBar)
                                        time.sleep(0.1)
                                        pygame.display.update()
                                    for i in range(5):
                                        pygame.draw.rect(battleScreen, (247, 234, 40), xpBar)
                                        time.sleep(0.1)
                                        pygame.display.update()
                                        pygame.draw.rect(battleScreen, (130, 243, 243), xpBar)
                                        time.sleep(0.1)
                                        pygame.display.update()
                                    battleScreen.blit(battleBorder, (0, 500))
                                    battleText = pygame.font.Font.render(
                                        endMessageFont, "You leveled up!", True, (255, 255, 255))
                                    battleScreen.blit(battleText, (50, 550))
                                    print(f"Hero health: {hero.tempHp}")
                                    enemy.afterWin(enemy.level * 1000)
                                    enemy.reset()
                                    print(f"Grunt health: {enemy.tempHp}")
                                    time.sleep(1)
                                    endBattle = True
                                    pygame.display.update()

                                    while (endBattle == True):
                                        
                                        xpBarStatus = 0
                                        for event in pygame.event.get():
                                            if event.type == pygame.QUIT:
                                                battleRunning = False
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                (x, y) = pygame.mouse.get_pos()
                                                if ((x >= 0) and (x <= 1280) and (y >= 500) and (y <= 720) and (endBattle == True)):
                                                    heroSwapped = charSwap(hero.imageSource, enemy.imageSource)
                                                    if (heroSwapped):
                                                        hero = enemy
                                                        endBattle = False
                                                        battleRunning = False
                                                    else:
                                                        endBattle = False
                                                        battleRunning = False
                                                hero.usedBlockLast = False
                                                hero.isProtected = False
                                                hero.isChargingUp = True
                                                hero.turnsOfChipLeft = 0

                                    endBattle = True
                                    pygame.display.update()
    
                        printMethod = True

                    battleScreen.blit(battleBg, (0, 0))
                    battleScreen.blit(
                        heroImg, ((battleScreen_rect.width / 2) - 335, 320))
                    battleScreen.blit(battleBorder, (0, 500))
                    battleScreen.blit(
                        gruntImg, ((battleScreen_rect.width / 2) + 158, 88))

                    pygame.draw.rect(battleScreen, (240, 240, 240), attack1)
                    pygame.draw.rect(battleScreen, (240, 240, 240), attack2)
                    pygame.draw.rect(battleScreen, (240, 240, 240), attack3)
                    pygame.draw.rect(battleScreen, (240, 240, 240), attack4)

                    pygame.draw.rect(battleScreen, (255, 0, 0), heroHealthRect)
                    pygame.draw.rect(battleScreen, (255, 0, 0), enemyHealthRect)

                    levelFont = pygame.font.Font('kvn-pokemon-gen-5.ttf', 30)
                    attackFont = pygame.font.Font('kvn-pokemon-gen-5.ttf', 30)

                    while printMethod:
                        battleScreen.blit(battleBorder, (0, 500))
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                printMethod = False
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                (x, y) = pygame.mouse.get_pos()
                                if (y > 500):
                                    printMethod = False
                                    
                        pygame.draw.rect(battleScreen, (255, 0, 0), heroHealthRect)
                        pygame.draw.rect(battleScreen, (255, 0, 0), enemyHealthRect)

                        playerAttackText = attackFont.render(playerAttackRectText, True, (0, 0, 0))
                        playerDmgTextTest = attackFont.render(playerDmgText, True, (0, 0, 0))
                        playerAttackText_rect = playerAttackText.get_rect()
                        playerAttackText_rect.x = 150
                        playerAttackText_rect.y = 550
                        battleScreen.blit(playerAttackText, (playerAttackText_rect.x, playerAttackText_rect.y))
                        battleScreen.blit(playerDmgTextTest, (playerAttackText_rect.x, playerAttackText_rect.y + playerAttackText_rect.height + 2))

                        enemyAttackText = attackFont.render(enemyAttackRectText, True, (0, 0, 0))
                        enemyDmgTextTest = attackFont.render(enemyDmgText, True, (0, 0, 0))
                        enemyAttackText_rect = enemyAttackText.get_rect()
                        enemyAttackText_rect.x = 690
                        enemyAttackText_rect.y = 550
                        battleScreen.blit(enemyAttackText, (enemyAttackText_rect.x, enemyAttackText_rect.y))
                        battleScreen.blit(enemyDmgTextTest, (enemyAttackText_rect.x, enemyAttackText_rect.y + enemyAttackText_rect.height + 2))

                        text = f"{hero.level}"
                        heroLevelPrint = levelFont.render(text, True, (0, 0, 0))
                        battleScreen.blit(heroLevelPrint, (1055, 343))

                        text = f"{enemy.level}"
                        enemyLevelPrint = levelFont.render(text, True, (0, 0, 0))
                        battleScreen.blit(enemyLevelPrint, (505, 87))

                        text = f"{hero.hp}"
                        enemyLevelPrint = levelFont.render(text, True, (0, 0, 0))
                        battleScreen.blit(enemyLevelPrint, (1046, 417))

                        text = f"{hero.tempHp}"
                        enemyLevelPrint = levelFont.render(text, True, (0, 0, 0))
                        battleScreen.blit(enemyLevelPrint, (975, 417))

                        text = f"{hero.fighterName}"
                        enemyLevelPrint = levelFont.render(text, True, (0, 0, 0))
                        battleScreen.blit(enemyLevelPrint, (750, 343))

                        text = f"{enemy.fighterName}"
                        enemyLevelPrint = levelFont.render(text, True, (0, 0, 0))
                        battleScreen.blit(enemyLevelPrint, (200, 87))
                        pygame.display.update()
                    
                    text = f"{hero.level}"
                    heroLevelPrint = levelFont.render(text, True, (0, 0, 0))
                    battleScreen.blit(heroLevelPrint, (1055, 343))

                    text = f"{enemy.level}"
                    enemyLevelPrint = levelFont.render(text, True, (0, 0, 0))
                    battleScreen.blit(enemyLevelPrint, (505, 87))

                    text = f"{hero.hp}"
                    enemyLevelPrint = levelFont.render(text, True, (0, 0, 0))
                    battleScreen.blit(enemyLevelPrint, (1046, 417))

                    text = f"{hero.tempHp}"
                    enemyLevelPrint = levelFont.render(text, True, (0, 0, 0))
                    battleScreen.blit(enemyLevelPrint, (975, 417))

                    text = f"{hero.fighterName}"
                    enemyLevelPrint = levelFont.render(text, True, (0, 0, 0))
                    battleScreen.blit(enemyLevelPrint, (750, 343))

                    text = f"{enemy.fighterName}"
                    enemyLevelPrint = levelFont.render(text, True, (0, 0, 0))
                    battleScreen.blit(enemyLevelPrint, (200, 87))

                    move1Text = (hero.move1name + "   PP: " + str(hero.move1TempPP))
                    attack1Text = battleFont.render(move1Text, True, (0, 0, 0))
                    attack1Text_rect = attack1Text.get_rect()
                    battleScreen.blit(attack1Text, (100 + ((((battleScreen_rect.width - 300) / 2) -
                                      attack1Text_rect.width) / 2), 535 + ((50 - attack1Text_rect.height) / 2)))

                    move2Text = (hero.move2name + "   PP: " + str(hero.move2TempPP))
                    attack2Text = battleFont.render(move2Text, True, (0, 0, 0))
                    attack2Text_rect = attack2Text.get_rect()
                    battleScreen.blit(attack2Text, (((battleScreen_rect.width / 2) + 50) + (
                        (((battleScreen_rect.width - 300) / 2) - attack2Text_rect.width) / 2), 535 + ((50 - attack2Text_rect.height) / 2)))

                    move3Text = (hero.move3name + "   PP: " + str(hero.move3TempPP))
                    attack3Text = battleFont.render(move3Text, True, (0, 0, 0))
                    attack3Text_rect = attack3Text.get_rect()
                    battleScreen.blit(attack3Text, (100 + ((((battleScreen_rect.width - 300) / 2) -
                                      attack3Text_rect.width) / 2), 630 + ((50 - attack3Text_rect.height) / 2)))

                    move4Text = (hero.move4name + "   PP: " + str(hero.move4TempPP))
                    attack4Text = battleFont.render(move4Text, True, (0, 0, 0))
                    attack4Text_rect = attack4Text.get_rect()
                    battleScreen.blit(attack4Text, (((battleScreen_rect.width / 2) + 50) + (
                        (((battleScreen_rect.width - 300) / 2) - attack4Text_rect.width) / 2), 630 + ((50 - attack4Text_rect.height) / 2)))
                    pygame.display.update()
                battleLoopBool = False

            self.screen.fill('black')

            if level1RunBool == True:
                self.level1.run()
            elif level2RunBool == True:
                self.level2.run()
            elif level3RunBool == True:
                self.level3.run()
            elif level4RunBool == True:
                self.level4.run()

            if runMainLoop == True:
                message = gameObjects.notFaintedMessage
                draw_text(self.screen, message, (255, 0, 0), 30, 300, 600)
                pygame.display.update()
                self.clock.tick(FPS)

    def effectCheck(effectID, hero, enemy):
        if (effectID == 1):
        # 1 - The user runs with high speeds and blocks the enemies attack, this move has priority. If this move is repeated consecutively, its accuracy is halved. 
            if (hero.usedBlockLast == False):
                hero.isProtected = True
                hero.usedBlockLast = True
                print("protect hit")
                print(hero.usedBlockLast)
            elif (hero.usedBlockLast == True):
                rngCheck = random.randint(1, 2)
                print(f"rngCheck result: {rngCheck}")
                if (rngCheck == 1):
                    hero.isProtected = True
                    hero.usedBlockLast = True
                    print("protect hit")
                else:
                    hero.isProtected = False
                    hero.usedBlockLast = False
                    print("protect missed")
            

        if (effectID == 3):
        # 3 - Increases attack stat by 1 stage - maxes out at 6
            if (hero.tempAtk < (hero.atk * 4)):
                    hero.tempAtk += (hero.atk * 0.5)
                    print("Attack was raised 1 stage")
                    print(hero.tempAtk)
            else:
                print ("Attack stat maxed, no change")
        elif (effectID == 4):
        # 4 - This move has a 20% chance of lowering the opponents defense by 1 stage.
            if (enemy.tempDfs > (enemy.dfs / 4)):
                rngCheck = random.randint(1, 5)
                if (rngCheck == 1):
                    enemy.tempDfs -= enemy.dfs * 0.125
                    print("Defense was lowered 1 stage")
                else:
                    print ("no defense change")
        elif (effectID == 5):
        #5 - T1 charge up (no damage), T2 attack
            if (hero.isChargingUp == True):
                print(f"{hero.fighterName} is charging up!")
                setStoredAttack(hero.tempAtk)
                print(hero.tempAtk)
                hero.tempAtk = 0
            elif (hero.isChargingUp == False):
                print(f"{hero.fighterName} is attacking!")



        elif (effectID == 7):
        # 7 - Decreases opponent accuracy by 1/8th if it hits
            if (enemy.tempAcc > 0.25):
                enemy.tempAcc -= 0.125
                print("Accuracy was lowered 12%")
        elif (effectID == 8):
        # 8 - heals 50% health
            if (hero.tempHp + (0.5 * hero.hp) < hero.hp):
                hero.tempHp = round(hero.tempHp + (0.5 * hero.hp))
            else:
                hero.tempHp = hero.hp
        elif (effectID == 10):
        # 10 - Switch user attack and defense stats
            print(f"attack: {hero.tempAtk}, defense: {hero.tempDfs}")
            temp = hero.tempDfs
            hero.tempDfs = hero.tempAtk
            hero.tempAtk = temp
            print("atk and dfs switched")
            print(f"attack: {hero.tempAtk}, defense: {hero.tempDfs}")
        elif (effectID == 11):
        #11 - increases speed stat by 1 stage - maxes out at 6
            if (hero.tempSpd < 4 * hero.spd):
                hero.tempSpd += round(0.5 * hero.spd)
                print(f"new speed: {hero.tempSpd}")
        elif (effectID == 12):
        # 12 - drops opponent defense stat by 1 stage - maxes out at 6
            if (enemy.tempDfs > 0):#0.25 * enemy.dfs):
                enemy.tempDfs /= 1.2#-= round(0.5 * enemy.dfs)
                print(f"enemy defense: {enemy.tempDfs}")
        elif (effectID == 14):
        # 14 - heals 25% health
            if (hero.tempHp + (0.25 * hero.hp) < hero.hp):
                hero.tempHp = round(hero.tempHp + (0.25 * hero.hp))
                print("health healed")
            else:
                hero.tempHp = hero.hp
        if (effectID == 15):
        # 15 - Increases defense stat by 1 stage - maxes out at 6
            if (hero.tempDfs < (hero.dfs * 4)):
                    hero.tempDfs += (hero.dfs * 0.5)
                    print("Defense was raised 1 stage")
                    print(hero.tempDfs)
            else:
                print ("Defense stat maxed, no change")
        elif (effectID == 16):
        # 16 - drops opponent speed by 1 stage - maxes
            if (enemy.tempSpd > 0.25 * enemy.spd):
                enemy.tempSpd -= round(0.125 * enemy.spd)
                print(f"enemy speed: {enemy.tempSpd}")
        elif (effectID == 19):
        # 19 - Switch user defense into enemy defense stat
            print(f"hero defense: {hero.tempDfs}, enemy defense: {enemy.tempDfs}")
            hero.tempDfs = enemy.tempDfs
            print("dfs switched")
            print(f"hero defense: {hero.tempDfs}, enemy defense: {enemy.tempDfs}")
        else:
            print("id not reached")

    def afterEffectCheck(effectID, hero, enemy, damage):
            if (effectID == 5):
            #5 - T1 charge up (no damage), T2 attack
                if (hero.isChargingUp == True):
                    hero.tempAtk = getStoredAttack()
                    print(f"stored attack = {getStoredAttack()}")
                    hero.isChargingUp = False
                elif (hero.isChargingUp == False):
                    hero.isChargingUp = True
            elif (effectID == 6):
            # 6 - Ohm uses his toxic voice chat energy to irradiate the battle. Opponent takes 1/16th chip damage per turn for the next 5 turns
                if (hero.turnsOfChipLeft == 0):
                    hero.turnsOfChipLeft = 4
            #12 - only works if user is under 25% hp. drops defense by 50%, increases attack and speed by 100%
            elif (effectID == 13):
                if (hero.tempHp <= round(0.25 * hero.hp)):
                    print(f"old: {hero.tempDfs}, {hero.tempAtk}, {hero.tempSpd} ")
                    hero.tempDfs = round(0.5 * hero.tempDfs)
                    hero.tempAtk *= 2
                    hero.tempSpd *= 2
                    print(f"new: {hero.tempDfs}, {hero.tempAtk}, {hero.tempSpd} ")

            elif (effectID == 17):
            # 17 - increases attack 10% each time the move is used up to 200%
                if (hero.tempAtk < (hero.atk * 2)):
                    hero.tempAtk += round(0.10 * hero.atk)
                    print(f"new attack {hero.tempAtk}")
                
            elif (effectID == 18):
            #18 - deals 33% damage of attack to user
                recoilDamage = round(0.33 * damage)
                print(f"recoil damage: {recoilDamage}")
                if ((hero.tempHp - recoilDamage) > 0):
                    hero.tempHp -= recoilDamage
                else:
                    hero.tempHp = 0



if __name__ == '__main__':
    game = Game()
    game.run()

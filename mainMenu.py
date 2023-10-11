#Main Menu 
#PLEASE START HERE (RUN THIS FILE)
import pygame, time
from main import Game as game
import main
pygame.init()

fps = 120
clock = pygame.time.Clock()
obamaFix = 1
startGame = False

pygame.display.set_caption("Super Ohio Throwdown")
pygame.mixer.music.load("menumusic.mp3")

bg = pygame.image.load('ohioBackground.jpg')
bg_rect = bg.get_rect()
keys = {'right':False, 'up':False, 'left':False, 'down':False}

screen = pygame.display.set_mode((1280, 720))
screen_rect = screen.get_rect()

controlScreen = pygame.display.set_mode((1280, 720))
controlScreen_rect = controlScreen.get_rect()

creditsScreen = pygame.display.set_mode((1280, 720))
creditsScreen_rect = controlScreen.get_rect()

logo = pygame.image.load('ohiologo.png')
logo_rect = logo.get_rect()
logo_rect.x = (screen.get_rect().centerx - (logo_rect.width / 2))
logo_rect.y = (screen.get_rect().centery - (logo_rect.height/2) - 150) / 2

controlsTab_rect = pygame.Rect((screen.get_rect().centerx - (logo_rect.width / 2)), (screen.get_rect().centery - (logo_rect.height/2) + 50), 275, 100)
creditsTab_rect = pygame.Rect((screen.get_rect().centerx - (logo_rect.width / 2) + 325), (screen.get_rect().centery - (logo_rect.height/2) + 50), 275, 100)
startTab_rect = pygame.Rect((screen.get_rect().centerx - (logo_rect.width / 2)), (screen.get_rect().centery - (logo_rect.height/2) + 175), 600, 100)
exitTab_rect = pygame.Rect((screen.get_rect().centerx - (logo_rect.width / 2)), (screen.get_rect().centery - (logo_rect.height/2) + 300), 600, 100)

menuFont = pygame.font.Font('kvn-pokemon-gen-5.ttf', 48)
controlsText = pygame.font.Font.render(menuFont, "Controls", True, (255, 255, 255))
controlsText_rect = controlsText.get_rect()

creditsText = pygame.font.Font.render(menuFont, "Credits", True, (255, 255, 255))
creditsText_rect = controlsText.get_rect()

startText = pygame.font.Font.render(menuFont, "Start", True, (255, 255, 255))
startText_rect = controlsText.get_rect()
print(startText_rect.width)

exitText = pygame.font.Font.render(menuFont, "Exit", True, (255, 255, 255))
exitText_rect = controlsText.get_rect()

backText = pygame.font.Font.render(menuFont, "Back", True, (255, 255, 255))

level = 0

running = True
controlsMenuActive = False
creditsActive = False
while running:
    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            (x, y) = pygame.mouse.get_pos()
            if (x >= startTab_rect.x and x <= (startTab_rect.x + startTab_rect.width) and y >= startTab_rect.y and y <= (startTab_rect.y + startTab_rect.height) and controlsMenuActive == False):
                
                controlScreen.fill('black')
                line1 = "The player faces a devastating defeat at the hands of a powerful unknown"
                line2 = "individual, leading to a 20-year period in the maximum security FunTime" 
                line3 = "jail. After years of isolation, the player finally earns a phone call" 
                line4 = "for their good behavior. With the opportunity to choose an ally from three" 
                line5 = "potential characters, the player sets their sights on breaking out of their" 
                line6 = "confines. The chosen ally is then dispatched to the jail, ready to aid the"
                line7 = "player in their daring escape. Will they make it out alive? Only time will tell."

                line0 = "Loading..."

                main.draw_text(controlScreen, line1, (255, 255, 255), 30, 100, 100)
                main.draw_text(controlScreen, line2, (255, 255, 255), 30, 100, 135)
                main.draw_text(controlScreen, line3, (255, 255, 255), 30, 100, 170)
                main.draw_text(controlScreen, line4, (255, 255, 255), 30, 100, 205)
                main.draw_text(controlScreen, line5, (255, 255, 255), 30, 100, 240)
                main.draw_text(controlScreen, line6, (255, 255, 255), 30, 100, 275)
                main.draw_text(controlScreen, line7, (255, 255, 255), 30, 100, 310)
                main.draw_text(controlScreen, line0, (255, 255, 255), 30, 590, 600)

                pygame.display.update()
                time.sleep(20)
            
                newGame = game()
                newGame.run()
                pygame.display.update()
                    
            elif (x >= exitTab_rect.x and x <= (exitTab_rect.x + exitTab_rect.width) and y >= exitTab_rect.y and y <= (exitTab_rect.y + exitTab_rect.height) and controlsMenuActive == False):
                running = False
            elif (x >= controlsTab_rect.x and x <= (controlsTab_rect.x + controlsTab_rect.width) and y >= controlsTab_rect.y and y <= (controlsTab_rect.y + controlsTab_rect.height) and controlsMenuActive == False):
                controlsMenuActive = True
            elif (x >= creditsTab_rect.x and x <= (creditsTab_rect.x + creditsTab_rect.width) and y >= creditsTab_rect.y and y <= (creditsTab_rect.y + creditsTab_rect.height) and creditsActive == False):
                creditsActive = True


    while controlsMenuActive:
            controlScreen.blit(bg, (0,0))
            controlsMenuText1 = pygame.font.Font.render(menuFont, "Use the WASD keys to move", True, (255, 255, 255))
            controlsMenuText2 = pygame.font.Font.render(menuFont, "Click in battles to select your moves / move forward", True, (255, 255, 255))
            controlsMenuText3 = pygame.font.Font.render(menuFont, "ESC key in overworld to access pause menu", True, (255, 255, 255))
            controlsMenuText4 = pygame.font.Font.render(menuFont, 'To quit the game, access the pause menu and press "Quit" ', True, (255, 255, 255))
            battleTutorial = pygame.image.load("tutorialAttack.jpg")
            battleTutorialImg = pygame.transform.scale(battleTutorial, (427, 240))
            
            controlScreen.blit(controlsMenuText1, ((controlScreen_rect.centerx) - (0.5 * controlsMenuText1.get_rect().width), (0)))
            controlScreen.blit(controlsMenuText2, ((controlScreen_rect.centerx) - (0.5 * controlsMenuText2.get_rect().width), (60)))
            controlScreen.blit(controlsMenuText3, ((controlScreen_rect.centerx) - (0.5 * controlsMenuText3.get_rect().width), (400)))
            controlScreen.blit(controlsMenuText4, ((5 + controlScreen_rect.centerx) - (0.5 * controlsMenuText4.get_rect().width), (460)))
            controlScreen.blit(battleTutorialImg, ((controlScreen_rect.centerx - (0.5 * battleTutorialImg.get_rect().width)), (170)))
            pygame.draw.rect(controlScreen, (0, 0, 255), exitTab_rect)
            controlScreen.blit(backText, (exitTab_rect.centerx - (0.5 * backText.get_rect().width), exitTab_rect.y))
            pygame.display.update()
            clock.tick(fps)

            while (controlsMenuActive == True):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        controlsMenuActive = False
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        (x, y) = pygame.mouse.get_pos()
                        if (x >= exitTab_rect.x and x <= (exitTab_rect.x + exitTab_rect.width) and y >= exitTab_rect.y and y <= (exitTab_rect.y + exitTab_rect.height) and controlsMenuActive == True):
                            controlsMenuActive = False

    while creditsActive:
            creditsScreen.blit(bg, (0,0))
            creditsMenuText1 = pygame.font.Font.render(menuFont, "Programmed by: ", True, (255, 255, 255))
            creditsMenuText2 = pygame.font.Font.render(menuFont, "Aarya Patel", True, (255, 255, 255))
            creditsMenuText3 = pygame.font.Font.render(menuFont, "Ohm Patel", True, (255, 255, 255))
            creditsMenuText4 = pygame.font.Font.render(menuFont, "Sridhar Patel", True, (255, 255, 255))
            creditsMenuText5 = pygame.font.Font.render(menuFont, "and Tiago Alves", True, (255, 255, 255))

            creditsScreen.blit(creditsMenuText1, ((creditsScreen_rect.centerx) - (0.5 * creditsMenuText1.get_rect().width), (25)))
            creditsScreen.blit(creditsMenuText2, ((creditsScreen_rect.centerx) - (0.5 * creditsMenuText1.get_rect().width), (125)))
            creditsScreen.blit(creditsMenuText3, ((creditsScreen_rect.centerx) - (0.5 * creditsMenuText1.get_rect().width), (225)))
            creditsScreen.blit(creditsMenuText4, ((creditsScreen_rect.centerx) - (0.5 * creditsMenuText1.get_rect().width), (325)))
            creditsScreen.blit(creditsMenuText5, ((creditsScreen_rect.centerx) - (0.5 * creditsMenuText1.get_rect().width), (425)))
            pygame.draw.rect(creditsScreen, (0, 0, 255), exitTab_rect)
            creditsScreen.blit(backText, (exitTab_rect.centerx - (0.5 * backText.get_rect().width), exitTab_rect.y))
            pygame.display.update()
            clock.tick(fps)

            while (creditsActive == True):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        creditsActive = False
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        (x, y) = pygame.mouse.get_pos()
                        if (x >= exitTab_rect.x and x <= (exitTab_rect.x + exitTab_rect.width) and y >= exitTab_rect.y and y <= (exitTab_rect.y + exitTab_rect.height) and creditsActive == True):
                            creditsActive = False
    
    screen.blit(bg, (0,0))
    screen.blit(logo, logo_rect)
    pygame.draw.rect(screen, (255, 0, 0), controlsTab_rect)
    screen.blit(controlsText, ((controlsTab_rect.centerx - 90), (controlsTab_rect.centery - 50)))
    pygame.draw.rect(screen, (255, 0, 0), creditsTab_rect)
    screen.blit(creditsText, ((creditsTab_rect.centerx - 75), (creditsTab_rect.centery - 50)))
    pygame.draw.rect(screen, (255, 0, 0), startTab_rect)
    screen.blit(startText, (startTab_rect.centerx - (0.5 * startText.get_rect().width), startTab_rect.y))
    pygame.draw.rect(screen, (255, 0, 0), exitTab_rect)
    screen.blit(exitText, (10 + exitTab_rect.centerx - (0.5 * backText.get_rect().width), exitTab_rect.y))
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
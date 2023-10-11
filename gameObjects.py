import pygame
from levelSettings import *

battleLoopGrunt = False
gruntLoopRunOnce = False
level1Grunt = True
counterGrunt = 0

battleLoopMiniBoss = False
miniBossLoopRunOnce = False

battleLoopBoss = False
bossLoopRunOnce = False

endOfLevelOne = False
endOfLevelOneRunOnce = False

endOfLevelTwo = False
endOfLevelTwoRunOnce = False

endOfLevelThree = False
endOfLevelThreeRunOnce = False

endOfLevelFour = False
endOfLevelFourRunOnce = False

miniBossFainted = False
bossFainted = False
notFaintedMessage = ""

# Level 1 Sprites


class PrisionTile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "prisonfloortile.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)


class DoorTile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "prisonDoor.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)


class DoorTileFlipped(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "prisonDoor.png").convert_alpha()
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect(topleft=position)

class GruntTile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "grunt.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

# Level 2 Sprites

class WaterTile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "watertile.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)


class GrassTile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "grasstile.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)


class SandTile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "sandtile.jpg").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

class PalmTree(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "palmTree.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

class BlueUmbrella(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "blueUmbrella.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

class DeadFish(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "deadFish.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

class PirateShip(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "pirateShip.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)


class MiniBossShark(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        shark = pygame.image.load('shark.png')
        self.image = pygame.transform.scale(shark, (64, 64))
        self.rect = self.image.get_rect(topleft=position)


class BossJackSparrow(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        jackSparrow = pygame.image.load('jackSparrow.png')
        self.image = pygame.transform.scale(jackSparrow, (64, 64))
        self.rect = self.image.get_rect(topleft=position)


class BoatTile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "boat.png").convert_alpha()
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect(topleft=position)

# Level 3 Sprites

class StageTile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "stage.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

class NPC1(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "npc1.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

class NPC2(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "npc2.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

class NPC3(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "npc3.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

class NPC4(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "npc4.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

class NPC5(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "npc5.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

class Invisible(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "invisible.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

class Car(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "yellowCar.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

class MiniBossObama(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        obama = pygame.image.load('obama.png')
        self.image = pygame.transform.scale(obama, (64, 64))
        self.rect = self.image.get_rect(topleft=position)

class BossEminem(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        eminem = pygame.image.load('eminem.png')
        self.image = pygame.transform.scale(eminem, (64, 64))
        self.rect = self.image.get_rect(topleft=position)

# Level 4 Sprites
class LavaTile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "lavatile.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

class Plane(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "plane.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

class MiniGrizzlyBear(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        grizzlyBear = pygame.image.load('grizzlyBear.png')
        self.image = pygame.transform.scale(grizzlyBear, (64, 64))
        self.rect = self.image.get_rect(topleft=position)

class BossOhm(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        ohm = pygame.image.load('ohm.png')
        self.image = pygame.transform.scale(ohm, (64, 64))
        self.rect = self.image.get_rect(topleft=position)

# ALL LEVELS


class Tile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load(
            "new_rock.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)


class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups, obstacle_sprites, grunt_sprite, miniBoss_sprite, boss_sprite, door_sprite, boat_sprite, car_sprite, plane_sprite):
        super().__init__(groups)
        self.image = pygame.image.load(
            "sridhar_player_icon.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=position)

        self.direction = pygame.math.Vector2()
        self.speed = 5

        self.obstacle_sprites = obstacle_sprites
        self.grunt_sprite = grunt_sprite
        self.miniBoss_sprite = miniBoss_sprite
        self.boss_sprite = boss_sprite
        self.door_sprite = door_sprite
        self.boat_sprite = boat_sprite
        self.car_sprite = car_sprite
        self.plane_sprite = plane_sprite

        self.tempSpeedx = self.rect.x
        self.tempSpeedy = self.rect.y

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_RIGHT]:
            self.direction.x = 1
        else:
            self.direction.x = 0

    def move(self):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()

        self.tempSpeedx = self.rect.x
        self.tempSpeedy = self.rect.y

        self.rect.x += self.direction.x * self.speed
        self.collision("horizontal")
        self.rect.y += self.direction.y * self.speed
        self.collision("vertical")

    def collision(self, direction):
        global gruntLoopRunOnce
        global battleLoopGrunt
        global level1Grunt
        global miniBossLoopRunOnce
        global battleLoopMiniBoss
        global bossLoopRunOnce
        global battleLoopBoss
        global endOfLevelOne
        global endOfLevelOneRunOnce
        global endOfLevelTwo
        global endOfLevelTwoRunOnce
        global endOfLevelThree
        global endOfLevelThreeRunOnce
        global endOfLevelFour
        global endOfLevelFourRunOnce
        global miniBossFainted 
        global bossFainted 
        global notFaintedMessage

        global counterGrunt


        if direction == "horizontal":
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right

        if direction == "vertical":
            for sprite in self.obstacle_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom

        if gruntLoopRunOnce == False:
            for sprite in self.grunt_sprite:
                if sprite.rect.colliderect(self.rect):
                    gruntLoopRunOnce = True

                    # if level1Grunt == True:
                    #     self.rect.x = self.rect.x + 120
                    #     level1Grunt = False
                    # else:
                    self.rect.x = self.tempSpeedx
                    self.rect.y = self.tempSpeedy

                    counterGrunt = counterGrunt + 1

                    battleLoopGrunt = True

                    sprite.kill()
                    gruntLoopRunOnce = False
                    

        if miniBossLoopRunOnce == False:
            for sprite in self.miniBoss_sprite:
                if sprite.rect.colliderect(self.rect):
                    battleLoopMiniBoss = True
                    miniBossFainted = True
                    miniBossLoopRunOnce = True
                    sprite.kill()

        
        if bossLoopRunOnce == False:
            for sprite in self.boss_sprite:
                if sprite.rect.colliderect(self.rect):
                    if miniBossFainted == True:
                        notFaintedMessage = ""
                        bossFainted = True
                        battleLoopBoss = True
                        bossLoopRunOnce = True
                        sprite.kill()
                    else: 
                        notFaintedMessage = "Defeat the Mini Boss before you can fight the boss"
                else:
                    notFaintedMessage = ""
        

        if endOfLevelOneRunOnce == False:
            for sprite in self.door_sprite:
                if sprite.rect.colliderect(self.rect):
                    endOfLevelOne = True
                    endOfLevelOneRunOnce = True
        
        if endOfLevelTwoRunOnce == False:
            for sprite in self.boat_sprite:
                if sprite.rect.colliderect(self.rect):
                    if bossFainted == True:
                        notFaintedMessage = ""
                        endOfLevelTwo = True
                        endOfLevelTwoRunOnce = True
                    else: 
                        notFaintedMessage = "Defeat the Boss before you can enter the boat"
                    

        if endOfLevelThreeRunOnce == False:
            for sprite in self.car_sprite:
                if sprite.rect.colliderect(self.rect):
                    if bossFainted == True:
                        notFaintedMessage = ""
                        endOfLevelThree = True
                        endOfLevelThreeRunOnce = True
                    else: 
                        notFaintedMessage = "Defeat the Boss before you can enter the car"
        
        if endOfLevelFourRunOnce == False:
            for sprite in self.plane_sprite:
                if sprite.rect.colliderect(self.rect):
                    if bossFainted == True:
                        notFaintedMessage = ""
                        endOfLevelFour = True
                        endOfLevelFourRunOnce = True
                    else: 
                        notFaintedMessage = "Defeat the Boss before you can enter the plane"

    def update(self):
        self.input()
        self.move()

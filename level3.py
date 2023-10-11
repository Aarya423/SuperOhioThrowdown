import pygame
from levelSettings import *
from gameObjects import Tile, Player, GruntTile, PrisionTile, StageTile, Car, MiniBossObama, BossEminem, NPC1, NPC2, NPC3, NPC4, NPC5, Invisible


class Level3:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # setup sprite groups
        self.visible_sprites = CameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        self.grunt_sprite = pygame.sprite.Group()
        self.miniBoss_sprite = pygame.sprite.Group()
        self.boss_sprite = pygame.sprite.Group()
        self.door_sprite = pygame.sprite.Group()
        self.boat_sprite = pygame.sprite.Group()
        self.car_sprite = pygame.sprite.Group()
        self.plane_sprite = pygame.sprite.Group()

        # setup sprite
        self.create_map()

    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP3):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE

                if col == " " or col == "p" or col == "g" or col == "o" or col == "c" or col == "1" or col == "2" or col == "3" or col == "4" or col == "5":
                    PrisionTile((x, y), [self.visible_sprites])
                
                if col == "s" or col == "e" or col == "i":
                    StageTile((x, y), [self.visible_sprites])

                

        for row_index, row in enumerate(WORLD_MAP3):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE

                if col == "x":
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
                
                if col == "1":
                    NPC1((x, y), [self.visible_sprites, self.obstacle_sprites])

                if col == "2":
                    NPC2((x, y), [self.visible_sprites, self.obstacle_sprites])

                if col == "3":
                    NPC3((x, y), [self.visible_sprites, self.obstacle_sprites])

                if col == "4":
                    NPC4((x, y), [self.visible_sprites, self.obstacle_sprites])

                if col == "5":
                    NPC5((x, y), [self.visible_sprites, self.obstacle_sprites])

                if col == "i":
                    Invisible((x, y), [self.visible_sprites, self.obstacle_sprites])

                if col == "p":
                    self.player = Player(
                        (x, y), [self.visible_sprites], self.obstacle_sprites, self.grunt_sprite, self.miniBoss_sprite, self.boss_sprite, self.door_sprite, self.boat_sprite, self.car_sprite, self.plane_sprite)
                    
                if col == "g":
                    GruntTile((x, y), [self.visible_sprites,
                                       self.grunt_sprite])
                    
                if col == "o":
                    MiniBossObama((x, y), [self.visible_sprites,
                                           self.miniBoss_sprite])

                if col == "e":
                    BossEminem((x, y), [self.visible_sprites,
                                             self.boss_sprite])
                
                if col == "c":
                    Car((x, y), [self.visible_sprites,
                             self.car_sprite])
                

    def run(self):
        # update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player):
        # getting the offset for the y and the x
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in self.sprites():
            offset_rect = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_rect)
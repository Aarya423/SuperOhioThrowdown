import pygame
from levelSettings import *
from gameObjects import Tile, Player, GrassTile, WaterTile, SandTile, GruntTile, MiniBossShark, BossJackSparrow, BoatTile, PalmTree, PirateShip, BlueUmbrella, DeadFish


class Level2:
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
        for row_index, row in enumerate(WORLD_MAP2):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE

                if col == "g" or col == "p":
                    GrassTile((x, y), [self.visible_sprites])

                if col == " " or col == "m" or col == "b" or col == "q" or col == "d" or col == "t" or col == "u" or col == "f":
                    SandTile((x, y), [self.visible_sprites])

                if col == "w" or col == "s":
                    WaterTile((x, y), [self.visible_sprites,
                              self.obstacle_sprites])

        for row_index, row in enumerate(WORLD_MAP2):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE

                if col == "x":
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])

                if col == "t":
                    PalmTree((x, y), [self.visible_sprites, self.obstacle_sprites])

                if col == "u":
                    BlueUmbrella((x, y), [self.visible_sprites, self.obstacle_sprites])

                if col == "f":
                    DeadFish((x, y), [self.visible_sprites, self.obstacle_sprites])
                    
                if col == "s":
                    PirateShip((x, y), [self.visible_sprites,
                              self.obstacle_sprites])

                if col == "p":
                    self.player = Player(
                        (x, y), [self.visible_sprites], self.obstacle_sprites, self.grunt_sprite, self.miniBoss_sprite, self.boss_sprite, self.door_sprite, self.boat_sprite, self.car_sprite, self.plane_sprite)

                if col == "q":
                    GruntTile(
                        (x, y), [self.visible_sprites, self.grunt_sprite])

                if col == "m":
                    MiniBossShark((x, y), [self.visible_sprites,
                                           self.miniBoss_sprite])

                if col == "b":
                    BossJackSparrow((x, y), [self.visible_sprites,
                                             self.boss_sprite])

                if col == "d":
                    BoatTile((x, y), [self.visible_sprites,
                             self.boat_sprite])

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

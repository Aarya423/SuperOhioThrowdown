import pygame
from levelSettings import *
from gameObjects import Tile, Player, PrisionTile, DoorTile, GruntTile, DoorTileFlipped


class Level1:
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
        for row_index, row in enumerate(WORLD_MAP1):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE

                if col == " " or col == "p" or col == "g":
                    PrisionTile((x, y), [self.visible_sprites])

        for row_index, row in enumerate(WORLD_MAP1):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE

                if col == "x" or col == "w":
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites])

                if col == "p":
                    self.player = Player(
                        (x, y), [self.visible_sprites], self.obstacle_sprites, self.grunt_sprite, self.miniBoss_sprite, self.boss_sprite, self.door_sprite, self.boat_sprite, self.car_sprite, self.plane_sprite)

                if col == "d":
                    DoorTile((x, y), [self.visible_sprites,
                             self.door_sprite])

                if col == "f":
                    DoorTileFlipped((x, y), [self.visible_sprites,
                                             self.door_sprite])

                if col == "g":
                    GruntTile((x, y), [self.visible_sprites,
                                       self.grunt_sprite])

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

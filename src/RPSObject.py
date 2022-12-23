import pygame
from enum import Enum
import itertools

class RPSType(Enum):
    Paper = "Paper"
    Scissors = "Scissors"
    Stone = "Rock"


class Window():
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth
        self.left = 0
        self.right = width
        self.top = 0
        self.bot = heigth
    
    def getTupel(self):
        return (self.width, self.heigth)
        


class RPSCircle(pygame.sprite.Sprite):

    alive = True

    def __init__(self, type: RPSType, startpos, velocity, startdir, imagepath: str, width = 100):
        super().__init__()
        self.type = type
        self.pos = pygame.math.Vector2(startpos)
        self.velocity = velocity
        self.dir = pygame.math.Vector2(startdir).normalize()
        self.image = pygame.transform.scale(
            pygame.image.load(imagepath).convert_alpha(), (width, width))
        self.rect = self.image.get_rect(
            center = (round(self.pos.x), round(self.pos.y)))
        self.radius = width/2

    def reflect(self, NV):
        self.dir = self.dir.reflect(pygame.math.Vector2(NV))
    
    def get_name(self):
        return str(self.type.name)

    def update(self):
        self.pos += self.dir * self.velocity
        self.rect.center = round(self.pos.x), round(self.pos.y)

    def wincheck(self, other):
        if self.type == RPSType.Paper:
                if other.type == RPSType.Scissors:
                    self.alive = False
        elif self.type == RPSType.Scissors:
                if other.type == RPSType.Stone:
                    self.alive = False
        elif self.type == RPSType.Stone:
            if other.type == RPSType.Paper:
                self.alive = False

    
    def reflect_if_collided(self, window_size: Window): # TODO: Weak type-checking ..
        if self.rect.left <= window_size.left:
            self.reflect((1, 0))
        if self.rect.right >= window_size.right:
            self.reflect((-1, 0))
        if self.rect.top <= window_size.top:
            self.reflect((0, 1))
        if self.rect.bottom >= window_size.bot:
            self.reflect((0, -1))
    
    # def die_if_killed(self, other_circles: list):
    #     for circle in other_circles:
    #         if self.pos.distance_to(circle.pos) < self.radius + circle.radius -2:
    #             new_vector = circle.dir - self.dir
    #             self.wincheck(circle)
                
                
# Helpers

def kill_dead_sprites(sprites: pygame.sprite.Group):
    for a, b in itertools.permutations(sprites, 2):
        if a.pos.distance_to(b.pos) < a.radius + b.radius -2:
                 new_vector = b.dir - a.dir
                 a.wincheck(b)




import pygame
from enum import Enum
import itertools

# Thanks to Rabbid76 for great tutorials regarding pygame!!!

class RPSType(Enum):
    Paper = "./img/Papier.png"
    Scissors = "./img/Schere.png"
    Stone = "./img/Stein.png"

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

    def __init__(self, type: RPSType, startpos, velocity, startdir, width = 70):
        super().__init__()
        self.type = type
        self.pos = pygame.math.Vector2(startpos)
        self.velocity = velocity
        self.dir = pygame.math.Vector2(startdir).normalize()
        self.image = pygame.transform.scale(
            pygame.image.load(self.type.value).convert_alpha(), (width, width))
        self.rect = self.image.get_rect(
            center = (round(self.pos.x), round(self.pos.y)))
        self.radius = width/2
        self.width = width

    def reflect(self, NV):
        self.dir = self.dir.reflect(pygame.math.Vector2(NV))
    
    def get_name(self):
        return str(self.type.name)

    def load_image(self):
        self.image = pygame.transform.scale(
            pygame.image.load(self.type.value).convert_alpha(), (self.width, self.width))

    def update(self):
        self.pos += self.dir * self.velocity
        self.rect.center = round(self.pos.x), round(self.pos.y)

    def wincheck(self, other):
        if self.type == RPSType.Paper:
            if other.type == RPSType.Scissors:
                self.type = RPSType.Scissors
                self.load_image()
        elif self.type == RPSType.Scissors:
            if other.type == RPSType.Stone:
                self.type = RPSType.Stone
                self.load_image()
        elif self.type == RPSType.Stone:
            if other.type == RPSType.Paper:
                self.type = RPSType.Paper
                self.load_image()

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

def find_collisions(sprites: pygame.sprite.Group):
    for a, b in itertools.permutations(sprites, 2):
        if a.pos.distance_to(b.pos) < a.radius + b.radius -2:
                 a.wincheck(b)


def reflectBalls(ball_1, ball_2):
    v1 = pygame.math.Vector2(ball_1.rect.center)
    v2 = pygame.math.Vector2(ball_2.rect.center)
    r1 = ball_1.rect.width // 2
    r2 = ball_2.rect.width // 2
    d = v1.distance_to(v2)
    if d < r1 + r2 - 2:
        ball_1.wincheck(ball_2)
        dnext = (v1 + ball_1.dir).distance_to(v2 + ball_2.dir)
        nv = v2 - v1
        if dnext < d and nv.length() > 0:
            ball_1.dir = ball_1.dir.reflect(nv)
            ball_2.dir = ball_2.dir.reflect(nv)

def window_collisions(group: pygame.sprite.Group, window_size):
    [sprite.reflect_if_collided(window_size) for sprite in group]
    





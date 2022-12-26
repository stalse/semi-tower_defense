import pygame
import os
from .enemy import Enemy

imgs = []
for x in range(4):
    add_str = str(x)
    imgs.append(pygame.transform.scale(pygame.image.load(os.path.join("Snake" + add_str + ".png")), (64, 64)))


class Snake(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "snake"
        self.money = 1
        self.max_health = 1
        self.health = self.max_health
        self.imgs = imgs[:]

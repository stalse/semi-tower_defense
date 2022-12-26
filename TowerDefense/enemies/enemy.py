import pygame
import math
import os


class Enemy:
    imgs = []

    def __init__(self):
        self.width = 32
        self.height = 48
        self.animation_count = 0
        self.health = 3
        self.vel = 3
        self.path = [(-64, 340), (6, 340), (157, 340), (180, 340), (180, 277),
                    (180, 140), (215, 140), (420, 140), (420, 310),
                    (420, 410), (581, 410), (708, 410), (730, 410), (730, 363), (730, 275), (872, 275), (1000, 275),
                    (1134, 275), (1194, 275), (1220, 275)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.img = None
        self.dis = 0
        self.path_pos = 0
        self.move_count = 0
        self.move_dis = 0
        self.max_health = 0
        self.speed_increase = 1.2

    def draw(self, win):
        self.img = self.imgs[self.animation_count]
        self.animation_count += 1

        if self.animation_count >= len(self.imgs):
            self.animation_count = 0

        win.blit(self.img, (self.x, self.y))
        self.move()

    def collide(self, X, Y):
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False

    def move(self):
        x1, y1 = self.path[self.path_pos]
        if self.path_pos + 1 >= len(self.path):
            x2, y2 = (1220, 454)
        else:
            x2, y2 = self.path[self.path_pos + 1]

        dirn = ((x2 - x1) * 2, (y2 - y1) * 2)
        length = math.sqrt((dirn[0]) ** 2 + (dirn[1]) ** 2)
        if length != 0:
            dirn = (dirn[0] / length, dirn[1] / length)

        move_x, move_y = ((self.x + dirn[0]), (self.y + dirn[1]))

        self.x = move_x
        self.y = move_y

        if dirn[0] >= 0:
            if dirn[1] >= 0:
                if self.x >= x2 and self.y >= y2:
                    self.path_pos += 1
            else:
                if self.x >= x2 and self.y <= y2:
                    self.path_pos += 1

    def hit(self, damage):
            self.health -= damage
            if self.health <= 0:
                return True
            return False

import pygame
from towers.tower import Tower
import os
import math
from towers.menu import Menu
import time


menu_bg = pygame.transform.scale(pygame.image.load(os.path.join("side.png")), (150, 70))


archer_imgs1 = []


archer_imgs1.append(pygame.transform.scale(pygame.image.load(os.path.join("tower.png")),(90, 90)))



class ArcherTowerLong(Tower):
    def __init__(self, x,y):
        super().__init__(x, y)
        self.archer_imgs = archer_imgs1[:]
        self.archer_count = 0
        self.range = 200
        self.original_range = self.range
        self.inRange = False
        self.damage = 1
        self.original_damage = self.damage
        self.width = self.height = 90
        self.moving = False
        self.name = "tower"
        self.timer = time.time()

        self.menu = Menu(self, self.x, self.y, menu_bg, [2000, 5000,"MAX"])

    def get_upgrade_cost(self):
        return self.menu.get_item_cost()

    def draw(self, win):
        super().draw_radius(win)
        super().draw(win)


    def change_range(self, r):
        self.range = r

    def attack(self, enemies):
        money = 0
        self.inRange = False
        enemy_closest = []
        for enemy in enemies:
            x = enemy.x
            y = enemy.y

            dis = math.sqrt((self.x - x)**2 + (self.y - y)**2)
            if dis < self.range:
                self.inRange = True
                enemy_closest.append(enemy)

        enemy_closest.sort(key=lambda x: x.path_pos)
        #enemy_closest = enemy_closest[::-1]
        if len(enemy_closest) > 0:
            first_enemy = enemy_closest[0]
            if time.time() - self.timer >= 0.5:
                self.timer = time.time()
                if first_enemy.hit(self.damage) == True:
                    money = first_enemy.money * 2
                    enemies.remove(first_enemy)

        return money
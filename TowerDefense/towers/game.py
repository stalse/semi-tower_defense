import os.path
import pygame
from enemies.snake import Snake
from towers.menu import VerticalMenu
from towers.DamageTower import ArcherTowerLong
import time
import random
pygame.font.init()
pygame.init()

side_img = pygame.transform.scale(pygame.image.load(os.path.join("side.png")), (150, 700))
buy_tower = pygame.transform.scale(pygame.image.load(os.path.join("tower.png")), (100, 100))



pygame.mixer.music.load(os.path.join("ost.mp3"))

attack_tower_names = ["tower"]

waves = [
    [20],
    [35],
    [60],
    [100],
]

class Game:
    def __init__(self, win):
        self.width = 1200
        self.height = 700
        self.money = 200
        self.win = win
        self.damage = 1
        self.enemies = [Snake()]
        self.attack_towers = []
        self.lives = 3
        self.timer = time.time()
        self.selected_tower = None
        self.bg = pygame.image.load(os.path.join("bg.png"))
        self.bg = pygame.transform.scale(self.bg, (self.width, self.height))
        self.life_font = pygame.font.SysFont("comicsans", 65)
        self.menu = VerticalMenu(self.width - side_img.get_width() + 70, 250, side_img)
        self.menu.add_btn(buy_tower, "buy_tower", 100)
        self.moving_object = None
        self.clicks = []
        self.wave = 0
        self.current_wave = waves[self.wave][:]

    def gen_enemies(self):
        if sum(self.current_wave) == 0:
            if len(self.enemies) == 0:
                self.wave += 1
                self.current_wave = waves[self.wave]
        else:
            wave_enemies = [Snake()]
            for x in range(len(self.current_wave)):
                if self.current_wave[x] != 0:
                    self.enemies.append(wave_enemies[x])
                    self.current_wave[x] = self.current_wave[x] - 1
                    break

    def run(self):
        pygame.mixer.music.play(loops=-1)
        run = True
        clock = pygame.time.Clock()
        enemy_check = []


        #for enemy in enemies:
           # enemy_check.append(enemy)

        #damage_enemy = enemy_check[0]

        while run:
            clock.tick(60)

            pos = pygame.mouse.get_pos()

            if time.time() - self.timer >= random.randrange(1, 20):
                self.timer = time.time()
                self.gen_enemies()

            pos = pygame.mouse.get_pos()

            if self.moving_object:
                self.moving_object.move(pos[0], pos[1])
                tower_list = self.attack_towers[:]
                collide = False
                for tower in tower_list:
                    if tower.collide(self.moving_object):
                        collide = True
                        tower.place_color = (255, 0, 0, 100)
                        self.moving_object.place_color = (255, 0, 0, 100)
                    else:
                        tower.place_color = (0, 0, 255, 100)
                        if not collide:
                            self.moving_object.place_color = (0, 0, 255, 100)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

                if event.type == pygame.MOUSEBUTTONUP:
                    if self.moving_object:
                        not_allowed = False
                        tower_list = self.attack_towers[:]
                        for tower in tower_list:
                            if tower.collide(self.moving_object):
                                not_allowed = True

                        if not not_allowed and self.point_to_line(self.moving_object):
                            if self.moving_object.name in attack_tower_names:
                                self.attack_towers.append(self.moving_object)

                            self.moving_object.moving = False
                            self.moving_object = None

                    side_menu_button = self.menu.get_clicked(pos[0], pos[1])
                    if side_menu_button:

                        cost = self.menu.get_item_cost(side_menu_button)
                        if self.money >= cost:
                            self.money -= cost
                            self.add_tower(side_menu_button)

                    btn_clicked = None
                    if self.selected_tower:
                        btn_clicked = self.selected_tower.menu.get_clicked(pos[0], pos[0])

                    if not (btn_clicked):
                        for tw in self.attack_towers:
                            if tw.click(pos[0], pos[1]):
                                tw.selected = True
                                self.selected_tower = tw
                            else:
                                tw.selected = False

                to_del = []
                for en in self.enemies:
                    en.move()
                    if en.x > 1150:
                        to_del.append(en)

                #if event.type == pygame.MOUSEBUTTONDOWN:
                    #if damage_enemy.hit(self.damage) == True:
                    #    enemies.remove(damage_enemy)
                    #check = [Snake()]
                    #if Snake() in check:
                        #self.enemies.remove(0)

                for d in to_del:
                    self.lives -= 1
                    self.enemies.remove(d)

                for tw in self.attack_towers:
                    self.money += tw.attack(self.enemies)

                if self.lives <= 0:
                    run = False
                    pygame.quit()

            self.draw()

    def point_to_line(self, tower):
        return True


    def draw(self):
        self.win.blit(self.bg, (0, 0))

        if self.moving_object:
            for tower in self.attack_towers:
                tower.draw_placement(self.win)

            self.moving_object.draw_placement(self.win)

        for tw in self.attack_towers:
            tw.draw(self.win)

        if self.selected_tower:
            self.selected_tower.draw(self.win)

        if self.moving_object:
            self.moving_object.draw(self.win)

        self.menu.draw(self.win)
        text = self.life_font.render(str(self.lives), 1, (255, 255, 255))
        self.win.blit(text, (text.get_width() - 10, 13))
        for en in self.enemies:
            en.draw(self.win)

        pygame.display.update()

    def add_tower(self, name):
        x, y = pygame.mouse.get_pos()
        name_list = ["buy_tower"]
        object_list = [ArcherTowerLong(x, y)]

        try:
            obj = object_list[name_list.index(name)]
            self.moving_object = obj
            obj.moving = True
        except Exception as e:
            print(str(e) + "NOT VALID NAME")

win = pygame.display.set_mode((1350, 700))
g = Game(win)
g.run()

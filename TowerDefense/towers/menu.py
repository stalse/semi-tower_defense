import pygame
pygame.font.init()

class Button:
    def __init__(self, menu, img, name):
        self.name = name
        self.img = img
        self.x = menu.x - 50
        self.y = menu.y - 110
        self.menu = menu
        self.width = self.img.get_width()
        self.height = self.img.get_height()

    def click(self, X, Y):
        pass
        if X <= self.x + self.width and X >= self.x:
            if Y <= self.y + self.height and Y >= self.y:
                return True
        return False


    def draw(self, win):
        win.blit(self.img, (self.x, self.y))

    def update(self):
        self.x = self.menu.x
        self.y = self.menu.y


class VerticalButton(Button):
    def __init__(self, x, y, img, name, cost):
        self.name = name
        self.img = img
        self.x = x
        self.y = y
        self.width = self.img.get_width()
        self.height = self.img.get_height()
        self.cost = cost


class Menu:
    def __init__(self, tower, x, y, img, item_cost):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.item_cost = item_cost
        self.buttons = []
        self.items = 0
        self.bg = img
        self.font = pygame.font.SysFont("comicsans", 25)
        self.tower = tower

    def add_btn(self, img, name):
        self.items += 1
        self.buttons.append(Button(self, img, name))

    def draw(self, win):
        win.blit(self.bg, (self.x + self.bg.get_width()/2, self.y-120))
        for item in self.buttons:
            item.draw(win)

    def get_item_cost(self, name):
        for btn in self.buttons:
            if btn.name == name:
                return btn.cost
        return -1

    def get_clicked(self, X, Y):
        for btn in self.buttons:
            if btn.click(X,Y):
                return btn.name

        return None

    def update(self):
        for btn in self.buttons:
            btn.update()


class VerticalMenu(Menu):
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.width = img.get_width()
        self.height = img.get_height()
        self.buttons = []
        self.items = 0
        self.bg = img
        self.font = pygame.font.SysFont("comicsans", 25)

    def add_btn(self, img, name, cost):
        self.items += 1
        btn_x = self.x + 120
        btn_y = self.y + (self.items-1)*120
        self.buttons.append(VerticalButton(btn_x, btn_y, img, name, cost))

    def draw(self, win):
        win.blit(self.bg, (self.x + self.bg.get_width()/2, self.y-120))
        for item in self.buttons:
            item.draw(win)
            text = self.font.render(str(item.cost), 1, (255,255,255))
            win.blit(text, (item.x + item.width/2 - text.get_width()/2, item.y + item.height + 5))

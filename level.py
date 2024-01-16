import random
import pygame


class Level():

    brick_colors = [(200, 50, 80), (45, 80, 240), (46, 235, 70),
                    (150, 50, 180), (230, 170, 80), (60, 230, 220), (180, 210, 80)]

    def __init__(self, screen: pygame.Surface, baground_color: tuple):
        self.screen = screen
        self.rows = 7
        self.rows_bricks = 9
        self.length = int(screen.get_width()*0.8)//self.rows_bricks
        self.width = 40
        self.spacing = 4
        self.bricks = []
        self.random_color = []
        self.background_color = baground_color
        for i in range(10, self.rows*(self.width), self.width):
            for j in range(int(screen.get_width()*0.1), int(screen.get_width()*0.9 - self.length)+1, self.length):
                self.bricks.append([j, i])
                self.random_color.append(random.choice(self.brick_colors))

    def show(self):
        num = 1
        color_index = 1
        for item in self.bricks:
            pygame.draw.rect(self.screen, self.brick_colors[color_index-1], ((
                item[0], item[1]), (self.length-self.spacing, self.width-self.spacing)))
            num += 1
            if num > color_index * self.rows_bricks:
                color_index += 1

    def update(self, cordinate):
        pygame.draw.rect(self.screen, self.background_color, (cordinate,
                                                              (self.length-self.spacing, self.width-self.spacing)))

    def remove(self, brick):
        self.bricks.remove(brick)

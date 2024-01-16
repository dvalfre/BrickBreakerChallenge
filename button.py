import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))
screen.fill((255, 255, 255))


class Button():

    def __init__(self, screen, colorButton, colorText, cordinates=(0, 0), dimensions=(100, 100), text='Click Here', textSize=10):
        self.screen = screen
        self.colorButton = colorButton
        self.colorText = colorText
        self.X, self.Y = cordinates
        self.width, self.length = dimensions
        self.text = text
        self.textSize = textSize

    def show(self):
        pygame.draw.rect(self.screen, self.colorButton,
                         ((self.X, self.Y), (self.width, self.length)))
        font = pygame.font.Font('freesansbold.ttf', self.textSize)
        caption = font.render(self.text, True, self.colorText)
        self.screen.blit(caption, (int(self.X + self.width*0.05),
                                   int(self.Y + self.length*0.2)))

    def isOverMouse(self):
        x, y = pygame.mouse.get_pos()
        if self.X < x < self.X + self.width and self.Y < y < self.Y + self.length:
            return True
        return False

    def changeColor(self, changeColorButton, changeColorText):
        pygame.draw.rect(self.screen, changeColorButton,
                         ((self.X, self.Y), (self.width, self.length)))
        font = pygame.font.Font('freesansbold.ttf', self.textSize)
        caption = font.render(self.text, True, changeColorText)
        self.screen.blit(caption, (int(self.X + self.width*0.05),
                                   int(self.Y + self.length*0.2)))

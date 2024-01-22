import random
import pygame
from collidable import Collidable

# Brick class inherits from Collidable
class Brick(Collidable):
    def __init__(self, position, color, length, width):
        super().__init__(position, length, width)
        self.color = color

# Level class for creating and managing the game level
class Level:
    brick_colors = [(200, 50, 80), (45, 80, 240), (46, 235, 70),
                    (150, 50, 180), (230, 170, 80), (60, 230, 220), (180, 210, 80)]

    # Initialize the level with a reference to the screen and the background color
    def __init__(self, screen: pygame.Surface, background_color: tuple):
        self.screen = screen
        self.rows = 7
        self.rows_bricks = 9
        self.length = int(screen.get_width() * 0.8) // self.rows_bricks
        self.width = 40
        self.spacing = 4
        self.bricks = []
        self.background_color = background_color
        self.create_bricks()

    # Create the bricks for the level
    def create_bricks(self):
        for row in range(10, self.rows * (self.width), self.width):
            for col in range(int(self.screen.get_width() * 0.1), int(self.screen.get_width() * 0.9 - self.length) + 1, self.length):
                position = [col, row]
                color = random.choice(self.brick_colors)
                brick = Brick(position, color, self.length - self.spacing, self.width - self.spacing)
                self.bricks.append(brick)

    # Draw the bricks on the screen
    def show(self):
        for brick in self.bricks:
            pygame.draw.rect(self.screen, brick.color, (brick.position, (self.length - self.spacing, self.width - self.spacing)))

    # Update the screen when a brick is removed
    def update(self, coordinate):
        pygame.draw.rect(self.screen, self.background_color, (coordinate, (self.length - self.spacing, self.width - self.spacing)))

    # Remove a brick from the level
    def remove(self, brick):
        self.bricks.remove(brick)

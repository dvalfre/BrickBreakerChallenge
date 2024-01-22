import pygame
from collidable import Collidable

# Paddle class inherits from Collidable
class Paddle(Collidable):
    paddle_color = (80, 50, 30)

    # Initialize the paddle with a reference to the screen
    def __init__(self, screen: pygame.Surface):
        self.paddleX = int(screen.get_width()*0.45)
        self.paddleY = int(screen.get_height()*0.95)
        self.length = 120
        self.screen = screen
        super().__init__([self.paddleX, self.paddleY], self.length, 10)

    # Draw the paddle on the screen
    def show(self):
        thickness = 10
        pygame.draw.rect(self.screen, self.paddle_color, ((
            self.paddleX, self.paddleY), (self.length, thickness)))

    # Move the paddle to the left
    def move_left(self):
        self.velocity = 15
        self.paddleX += -self.velocity
        self.position[0] = self.paddleX

    # Move the paddle to the right
    def move_right(self):
        self.velocity = 15
        self.paddleX += self.velocity
        self.position[0] = self.paddleX

    # Stop the paddle's movement
    def stop(self):
        self.velocity = 0

    # Check if the paddle hits the screen boundaries and stop it if it does
    def boundries(self):
        if self.paddleX >= (self.screen.get_width() - self.length):
            self.paddleX = self.screen.get_width() - self.length
        elif self.paddleX <= 0:
            self.paddleX = 0
        self.position[0] = self.paddleX

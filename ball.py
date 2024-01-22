import pygame
from paddle import Paddle
from collidable import Collidable

# Ball class inherits from Collidable
class Ball(Collidable):
    color = (50, 40, 255)

    # Initialize the ball with a reference to the paddle and the screen
    def __init__(self, paddle: Paddle, screen: pygame.Surface):
        self.ballX = int(screen.get_width()/2)
        self.ballY = int(screen.get_height()*0.8)
        self.x_vel = 8
        self.y_vel = -8
        self.ball_radius = 10
        self.max_x_vel = 10
        self.paddle = paddle
        self.screen = screen
        super().__init__([self.ballX, self.ballY], self.ball_radius, self.ball_radius)

    # Draw the ball on the screen
    def show(self):
        pygame.draw.circle(self.screen, self.color,
                           (self.ballX, self.ballY), self.ball_radius)

    # Update the ball's position based on its velocity
    def move(self):
        self.ballX += self.x_vel
        self.ballY += self.y_vel
        self.position = [self.ballX, self.ballY]

    # Change the ball's direction based on where it hits the paddle
    def collision_change(self):
        center = self.paddle.paddleX + self.paddle.length/2
        left_end = self.paddle.paddleX
        right_end = self.paddle.paddleX + self.paddle.length
        self.y_vel = -self.y_vel
        if left_end < self.ballX < center:
            ratio = (center - self.ballX)/(self.paddle.length/2)
            self.x_vel += -self.max_x_vel * ratio
        elif center < self.ballX < right_end:
            ratio = (self.ballX - center)/(self.paddle.length/2)
            self.x_vel += self.max_x_vel * ratio

    # Check if the ball hits the screen boundaries and reverse its direction if it does
    def boundries(self):
        if self.ballY <= (0 + self.ball_radius):
            self.y_vel = -self.y_vel
        if self.ballX <= (0 + self.ball_radius):
            self.x_vel = -self.x_vel
        if self.ballX >= (self.screen.get_width() - self.ball_radius):
            self.x_vel = -self.x_vel

    # Limit the ball's horizontal velocity to prevent it from going too fast
    def limit_vel(self):
        if -self.max_x_vel > self.x_vel:
            self.x_vel = -self.max_x_vel
        elif self.x_vel > self.max_x_vel:
            self.x_vel = self.max_x_vel

    # Update the ball's position, check for collisions, and limit its velocity
    def update(self):
        self.move()
        self.boundries()
        self.limit_vel()

import unittest
import pygame
from paddle import Paddle
from ball import Ball

class TestBall(unittest.TestCase):
    def setUp(self):
        self.screen = pygame.Surface((600, 400))
        self.paddle = Paddle(self.screen)
        self.ball = Ball(self.paddle, self.screen)

    def test_initial_position(self):
        self.assertEqual(self.ball.ballX, int(self.screen.get_width()/2))
        self.assertEqual(self.ball.ballY, int(self.screen.get_height()*0.8))

    def test_move(self):
        initial_x = self.ball.ballX
        initial_y = self.ball.ballY
        self.ball.move()
        self.assertEqual(self.ball.ballX, initial_x + self.ball.x_vel)
        self.assertEqual(self.ball.ballY, initial_y + self.ball.y_vel)

    def test_boundries(self):
        self.ball.ballX = self.screen.get_width()
        self.ball.boundries()
        self.assertEqual(self.ball.x_vel, -8)

        self.ball.ballX = -10
        self.ball.boundries()
        self.assertEqual(self.ball.x_vel, 8)

        self.ball.ballY = -10
        self.ball.boundries()
        self.assertEqual(self.ball.y_vel, 8)

    def test_limit_vel(self):
        self.ball.x_vel = 20
        self.ball.limit_vel()
        self.assertEqual(self.ball.x_vel, self.ball.max_x_vel)

        self.ball.x_vel = -20
        self.ball.limit_vel()
        self.assertEqual(self.ball.x_vel, -self.ball.max_x_vel)

if __name__ == '__main__':
    unittest.main()
import unittest
import pygame
from paddle import Paddle

class TestPaddle(unittest.TestCase):
    def setUp(self):
        self.screen = pygame.Surface((600, 400))
        self.paddle = Paddle(self.screen)

    def test_initial_position(self):
        self.assertEqual(self.paddle.paddleX, int(self.screen.get_width()*0.45))
        self.assertEqual(self.paddle.paddleY, int(self.screen.get_height()*0.95))

    def test_move_left(self):
        initial_position = self.paddle.paddleX
        self.paddle.move_left()
        self.assertEqual(self.paddle.paddleX, initial_position - 15)

    def test_move_right(self):
        initial_position = self.paddle.paddleX
        self.paddle.move_right()
        self.assertEqual(self.paddle.paddleX, initial_position + 15)

    def test_stop(self):
        self.paddle.stop()
        self.assertEqual(self.paddle.velocity, 0)

    def test_boundries(self):
        self.paddle.paddleX = self.screen.get_width()
        self.paddle.boundries()
        self.assertEqual(self.paddle.paddleX, self.screen.get_width() - self.paddle.length)

        self.paddle.paddleX = -10
        self.paddle.boundries()
        self.assertEqual(self.paddle.paddleX, 0)

if __name__ == '__main__':
    unittest.main()
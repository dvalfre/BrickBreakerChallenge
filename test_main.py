import unittest
from ball import Ball
from paddle import Paddle
from level import Level
import pygame

class TestBrickBreaker(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.paddle = Paddle(self.screen)
        self.ball = Ball(self.paddle, self.screen)
        self.level = Level(self.screen, (200, 200, 200))

    def test_ball_update(self):
        initial_ball_position = self.ball.position.copy()
        self.ball.update()
        self.assertNotEqual(self.ball.position, initial_ball_position)

    def test_paddle_move_left(self):
        initial_paddle_position = self.paddle.position.copy()
        self.paddle.move_left()
        self.assertLess(self.paddle.position[0], initial_paddle_position[0])

    def test_paddle_move_right(self):
        initial_paddle_position = self.paddle.position.copy()
        self.paddle.move_right()
        self.assertGreater(self.paddle.position[0], initial_paddle_position[0])

    def test_level_creation(self):
        self.assertEqual(len(self.level.bricks), 70)

    def test_level_remove_brick(self):
        initial_brick_count = len(self.level.bricks)
        self.level.remove(self.level.bricks[0])
        self.assertEqual(len(self.level.bricks), initial_brick_count - 1)

if __name__ == '__main__':
    unittest.main()

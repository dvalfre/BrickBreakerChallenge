import unittest
import pygame
from level import Level

class TestLevel(unittest.TestCase):
    def setUp(self):
        self.screen = pygame.Surface((600, 600))
        self.level = Level(self.screen, (255, 255, 255))

    def test_initial_bricks(self):
        # Test that the correct number of bricks are created
        self.assertEqual(len(self.level.bricks), self.level.rows * self.level.rows_bricks)

    def test_remove(self):
        # Test that a brick can be removed
        brick = self.level.bricks[0]
        self.level.remove(brick)
        self.assertNotIn(brick, self.level.bricks)

    def test_brick_colors_dict(self):
        # Test that each brick has a color assigned in the dictionary
        for brick in self.level.bricks:
            self.assertTrue(tuple(brick) in self.level.brick_colors_dict)
            self.assertTrue(self.level.brick_colors_dict[tuple(brick)] in self.level.brick_colors)

    def test_brick_color_removal(self):
        # Test that the color of a brick is removed from the dictionary when the brick is removed
        brick = self.level.bricks[0]
        self.level.remove(brick)
        self.assertFalse(tuple(brick) in self.level.brick_colors_dict)

if __name__ == '__main__':
    unittest.main()
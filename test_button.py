import unittest
import pygame
from button import Button

class TestButton(unittest.TestCase):
    def setUp(self):
        self.screen = pygame.Surface((600, 600))
        self.button = Button(self.screen, (255, 0, 0), (0, 0, 0), (50, 50), (100, 50), 'Test', 32)

    def test_initial_position(self):
        self.assertEqual(self.button.X, 50)
        self.assertEqual(self.button.Y, 50)

    def test_isOverMouse(self):
        pygame.mouse.set_pos((55, 55))
        self.assertTrue(self.button.isOverMouse())

        pygame.mouse.set_pos((0, 0))
        self.assertFalse(self.button.isOverMouse())

if __name__ == '__main__':
    unittest.main()
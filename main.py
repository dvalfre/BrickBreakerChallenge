import pygame
from ball import Ball
from level import Level
from button import Button
from paddle import Paddle

pygame.init()

# Screen dimensions
scr_width = 800
scr_height = 600

# Initialize the game screen
screen = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption("Brick Breaker")

# Function to display "Game Over" message
def show_gameover():
    global scr_height
    global scr_width
    text = pygame.font.Font("freesansbold.ttf", int(scr_height*0.1))
    gameover = text.render("GAME OVER", True, (255, 23, 20))
    screen.blit(gameover, (int(scr_width*0.25), int(scr_height*0.4)))

# Function to display "You Win" message
def show_you_win():
    global scr_height
    global scr_width
    text = pygame.font.Font("freesansbold.ttf", int(scr_height*0.1))
    you_win = text.render("YOU WIN", True, (0, 255, 0))
    screen.blit(you_win, (int(scr_width*0.3), int(scr_height*0.4)))

clock = pygame.time.Clock()
background_color = (200, 200, 200)

# Main game loop
while True:
    # Initialize game objects
    paddle = Paddle(screen)
    ball = Ball(paddle, screen)
    level = Level(screen, background_color)
    over = False
    clicked_replay = False

    # Variables to track paddle movement
    key_left = False
    key_right = False

    # Inner game loop
#    while True:
    while True:

        clock.tick(30)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    key_left = True
                if event.key == pygame.K_RIGHT:
                    key_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    paddle.stop()
                    key_left = False
                if event.key == pygame.K_RIGHT:
                    paddle.stop()
                    key_right = False

        # Game logic

        # Handle paddle movement
        if key_left == True:
            paddle.move_left()
        if key_right == True:
            paddle.move_right()

        # Update ball position and handle collisions
        ball.update()
        if ball.collides_with(paddle):
            ball.collision_change()
        for brick in level.bricks:
            if ball.collides_with(brick):
                ball.y_vel = -ball.y_vel
                level.remove(brick)

        # Check if player has won
        if len(level.bricks) == 0:
            show_you_win()
            over = True
            # Display replay button
            b = Button(screen, (80, 45, 200), (200, 250, 255),
                       (260, 350), (150, 60), "REPLAY", 30)
            state = 'original'
            while not clicked_replay:
                b.show()
                for event in pygame.event.get():
                    if b.isOverMouse() == True:
                        if event.type == pygame.MOUSEBUTTONUP:
                            clicked_replay = True
                        state = 'changed'
                    elif b.isOverMouse() == False:
                        state = 'original'
                    if event.type == pygame.QUIT:
                        pygame.quit()
                if state == 'changed':
                    b.changeColor((80, 240, 80), (14, 37, 100))
                if clicked_replay == True:
                    break
                pygame.display.update()

        # Handle paddle boundaries
        paddle.boundries()
        if ball.ballY > scr_height:
            show_gameover()
            over = True
            # Display replay button
            b = Button(screen, (80, 45, 200), (200, 250, 255),
                       (260, 350), (150, 60), "REPLAY", 30)
            state = 'original'
            while True:
                b.show()
                for event in pygame.event.get():
                    if b.isOverMouse() == True:
                        if event.type == pygame.MOUSEBUTTONUP:
                            clicked_replay = True
                        state = 'changed'
                    elif b.isOverMouse() == False:
                        state = 'original'
                    if event.type == pygame.QUIT:
                        pygame.quit()
                if state == 'changed':
                    b.changeColor((80, 240, 80), (14, 37, 100))
                if clicked_replay == True:
                    break
                pygame.display.update()

#        if clicked_replay:
#            break

        # Render game objects
        screen.fill(background_color)
        paddle.show()
        level.show()

        ball.show()
        if over == True:
            break

        pygame.display.update()
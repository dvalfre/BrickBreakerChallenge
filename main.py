import pygame
from ball import Ball
from level import Level
from button import Button
from paddle import Paddle

pygame.init()

scr_width = 800
scr_height = 600

screen = pygame.display.set_mode((scr_width, scr_height))
pygame.display.set_caption("Brick Breaker")


def brick_collision(level: Level, ball: Ball):
    for _, brick in enumerate(level.bricks):
        x, y = brick
        if (x < ball.ballX < (x + level.length) and
                y > ball.ballY > (y + level.width)):
            # Invert the y direction
            ball.y_vel = -ball.y_vel
            center = x + level.length/2
            if x < ball.ballX < center:
                ratio = (center - ball.ballX)/(level.length/2)
                ball.x_vel += -ball.max_x_vel * ratio
            elif center < ball.ballX < (x + level.length):
                ratio = (ball.ballX - center)/(level.length/2)
                ball.x_vel += ball.max_x_vel * ratio

            level.remove(brick)


def show_gameover():
    global scr_height
    global scr_width
    text = pygame.font.Font("freesansbold.ttf", int(scr_height*0.1))
    gameover = text.render("GAME OVER", True, (255, 23, 20))
    screen.blit(gameover, (int(scr_width*0.25), int(scr_height*0.4)))


clock = pygame.time.Clock()
background_color = (200, 200, 200)
while True:

    # initial positions
    paddle = Paddle(screen)
    ball = Ball(paddle, screen)
    level = Level(screen, background_color)
    over = False
    clicked_replay = False

    # paddle movement switches
    key_left = False
    key_right = False

    while True:

        clock.tick(30)

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

        # GAME LOGIC

        # paddle movement switches
        if key_left == True:
            paddle.move_left()
        if key_right == True:
            paddle.move_right()

        # ball machanics
        ball.update()

        ball_bottom = ball.ballY + ball.ball_radius
        ball_within_paddle = paddle.paddleX < ball.ballX < (
            paddle.paddleX + paddle.length)

        if paddle.paddleY + 10 > ball_bottom > paddle.paddleY and ball_within_paddle:
            ball.collision_change()
        # brick collision
        brick_collision(level, ball)

        # paddle boundries
        paddle.boundries()
        if ball.ballY > scr_height:
            show_gameover()
            over = True
            # REPLAY BUTTON
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

        screen.fill(background_color)
        paddle.show()
        level.show()

        ball.show()
        if over == True:
            break

        pygame.display.update()

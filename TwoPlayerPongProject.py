import pygame
import numpy as np

# pygame setup
pygame.init()

#origin is at the top left corner
# right side is positive x
# bottom is positive y
x_min = 0; y_min = 0;

#bottom right corner is x_max,y_max
x_max= 1280; y_max = 720;

#time increment
dt = 0.02

#initialize the screen size
screen = pygame.display.set_mode((x_max, y_max)) #16:9

#some constants
vx = -10 #speed of ball in the x-direction
vy = 10 #speed of ball in the y-direction
dx = 20 #speed of paddle


#set the default font for all text
my_font = pygame.font.SysFont('Arial', 20)

#title of the game
pygame.display.set_caption('Pong Game by Danielle Lee')


#initial ball position and size
ball_size = 10;
ball_pos = pygame.Vector2(x_max-100,y_min+100)
paddle_size = pygame.Vector2(100,20)
paddle2_size = pygame.Vector2(100,20)
paddle_pos = pygame.Vector2(100,600)
paddle2_pos = pygame.Vector2(100, 100)


#initialize the continuous loop
running = True

score_number = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    score_text = my_font.render(f"Score: {score_number}", True, (255, 255, 255))
    screen.blit(score_text, (x_min + 50, y_max / 2))

    #draw the ball and the paddle
    pygame.draw.circle(screen, "red", ball_pos, ball_size)
    pygame.draw.rect(screen,"blue",[paddle_pos.x, paddle_pos.y, paddle_size.x, paddle_size.y])
    pygame.draw.rect(screen, "blue", [paddle2_pos.x, paddle2_pos.y, paddle2_size.x, paddle2_size.y])

    #update the ball position.
    ball_pos.x += vx * dt
    ball_pos.y += vy * dt

    #Paddle movement is programmed here

## Player 1 controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle_pos.x -= dx * dt
    if keys[pygame.K_RIGHT]:
        paddle_pos.x += dx * dt
    if keys[pygame.K_DOWN]:
        paddle_pos.y += dx * dt
    if keys[pygame.K_UP]:
        paddle_pos.y -= dx * dt

## Player 2 controls
    if keys[pygame.K_a]:
        paddle2_pos.x -= dx * dt
    if keys[pygame.K_d]:
        paddle2_pos.x += dx * dt
    if keys[pygame.K_s]:
        paddle2_pos.y += dx * dt
    if keys[pygame.K_w]:
        paddle2_pos.y -= dx * dt

    #1) You need to write code to detect the walls and the paddle

    if paddle_pos.x < x_min: #paddle left bounds
        paddle_pos.x = x_min
    elif paddle_pos.x > x_max - 100: #paddle right bounds
        paddle_pos.x = x_max - 100

    if paddle_pos.y > y_max - 20:
        paddle_pos.y = y_max - 20
    elif paddle_pos.y < y_max - 200:
        paddle_pos.y = y_max - 200

    if paddle2_pos.x < x_min:  # paddle left bounds
        paddle2_pos.x = x_min
    elif paddle2_pos.x > x_max - 100:  # paddle right bounds
        paddle2_pos.x = x_max - 100

    if paddle2_pos.y < y_min:
        paddle2_pos.y = y_min
    elif paddle2_pos.y > y_min + 200:
        paddle2_pos.y = y_min + 200

    #2) You also need to write code that will ensure the proper physics after the ball bounces
    # of the walls and paddles
    ex = 1 + 0.1 * np.random.rand()
    ey = 1 + 0.1 * np.random.rand()

    # left wall and right wall
    if (ball_pos.x - (ball_size / 2)) <= x_min or (ball_pos.x + (ball_size / 2)) >= x_max:  # left and right walls
        vx = -1 * ex * vx

    # paddle and paddle2
    elif (((paddle_pos.y - 10) < ball_pos.y < (paddle_pos.y)) \
                and (paddle_pos.x < ball_pos.x < paddle_pos.x + 100)) \
            or (((paddle2_pos.y) < ball_pos.y < (paddle2_pos.y + 30)) \
                and (paddle2_pos.x < ball_pos.x < paddle2_pos.x + 100)):  # top and bottom paddle
        vy = -1 * ey * vy
        score_number += 1

    #Signal the game is over if the ball goes down
    if (ball_pos.y>=y_max):
        text_game_over = my_font.render("Game Over Player 2 Wins!", False, (0, 255, 255))
        screen.blit(text_game_over, (x_max/2 - 100,y_max/2))
        running = False
    elif (ball_pos.y <= y_min):
        text_game_over = my_font.render("Game Over Player 1 Wins!", False, (255, 0, 255))
        screen.blit(text_game_over, (x_max/2 - 100,y_max/2))
        running = False

    # flip() the display to put your work on screen
    pygame.display.flip()

    #pause for 2000 ms before exiting
    if (running==False):
        pygame.time.wait(2000)


pygame.quit()

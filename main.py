import random

import pygame

time = pygame.time.Clock()

# initialize pygame
pygame.init()

# Score
font = pygame.font.Font("freesansbold.ttf", 25)
opponentScore = 0
playerScore = 0

# _Over

fontS = pygame.font.Font("freesansbold.ttf", 64)
fontZ = pygame.font.Font("freesansbold.ttf", 32)

_Done = False

# screen
screen_width = 800  # the width
screen_height = 600  # the height
screen = pygame.display.set_mode((screen_width, screen_height))  # the screen
pygame.display.set_caption("Ping Pong By @MANDLIWH2")  # the title
iconImg = pygame.image.load("images/iconImg.png")  # load the image of the icon
pygame.display.set_icon(iconImg)  # applying the icon image

# Game Rectangles

ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)  # ball Rect
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)  # player Rect
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)  # opponent Rect

# Visuals

bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)

# ball Speed

ball_speed_x = 5
ball_speed_y = 5


# Functions

def show_score(x, y):
    score = font.render("PLAYER 1: " + str(x) + " | " + " PLAYER 2 : " + str(y), True, (255, 255, 255))
    screen.blit(score, (0, 0))


def _Random():
    final = random.choice((1, -1))
    return final


def _BallRestart():
    global ball_speed_x
    global ball_speed_y
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_x *= _Random()
    ball_speed_y *= _Random()


def _Over(winner):
    global _Done
    game_over = fontS.render("GAME OVER", True, (255, 255, 255))
    _Win = fontZ.render("WINNER : " + str(winner), True, (255, 255, 255))
    screen.blit(game_over, (200, 250))
    screen.blit(_Win, (200 + 16, 350))
    _Done = True


# opponent
opponentSpeed = 1


# player
player_speed = 0

# game loop
running = True
while running:
    # the background
    screen.fill(bg_color)
    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # Player Movement Mechanics
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_speed = 7
            if event.key == pygame.K_DOWN:
                player_speed = -7
        if event.type == pygame.KEYUP:
            player_speed *= -1
    # Opponent AI Mechanics
    if ball.y > opponent.y:
        opponent.y += opponentSpeed
    if ball.y < opponent.y:
        opponent.y -= opponentSpeed
    # Ball Mechanics
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    # Player Loop Incrementation
    player.y += player_speed
    # Ball Collisions
    if ball.colliderect(player):
        ball_speed_x *= -1
    if ball.colliderect(opponent):
        ball_speed_x *= -1
    if ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.top <= 0:
        ball_speed_y *= -1
    # Scoring Mechanics
    if ball.right >= screen_width + 20:
        _BallRestart()
        opponentScore += 1
    if ball.left <= - 20:
        _BallRestart()
        playerScore += 1
    # Game Over
    if opponentScore == 10:
        ball.center = (screen_width / 2, screen_height / 2)
        _Over("AI")
    if playerScore == 10:
        ball.center = (screen_width / 2, screen_height / 2)
        _Over("YOU")
    # player Border Limits
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
    # opponent Border Limits
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
    # Drawing The Recs
    if not _Done:
        pygame.draw.rect(screen, light_grey, player)
        pygame.draw.rect(screen, light_grey, opponent)
        pygame.draw.aaline(screen, light_grey, ((screen_width / 2), 0), ((screen_width / 2), screen_height))
        pygame.draw.ellipse(screen, light_grey, ball)
        # Showing The Score
        show_score(opponentScore, playerScore)

    # Updating The System
    pygame.display.update()
    time.tick(60)

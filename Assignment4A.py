# Class: CSE 1321L
# Section: BJD
# Term: Fall 2024
# Instructor: Tejaswini Karanam
# Name: Zachary Taylor
# Program: Assignment4A.py
import pygame, sys, random
from pygame.locals import *

#setup pygame window
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Fruit catching game')
score = 0

#welcome message
print("Welcome to the fruit catching game! Try to catch all the fruit! If you miss one, you lose. To leave, press the escape key.")

#make the surface and the fruit and basket rects
gameSurf = pygame.Surface((800, 600))
gameSurf.fill((0, 0, 0))

fruit = pygame.Rect(0, 0, 20, 20)
pygame.draw.rect(gameSurf, (255, 0, 0), fruit)
basket = pygame.Rect(0, 580, 100, 20)
pygame.draw.rect(gameSurf, (255, 255, 255), basket)

screen.blit(gameSurf, (0, 0))

while True:
    #keys and events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        print(f"You quit the game with a score of: {score}")
        sys.exit(0) #quit if escape key is pressed
    elif keys[pygame.K_LEFT] and basket.topleft != (0, 580):
        basket = basket.move(-5, 0) #move basket left if its not touching the edge
    elif keys[pygame.K_RIGHT] and basket.topleft != (700, 580):
        basket = basket.move(5, 0) #move basket right if its not touching the edge
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)

    #fruit logic
    if fruit.colliderect(basket):
        score +=1
        print(f"New score: {score}")
        fruit.topleft = ((random.randint(0, 780)), 0)
    elif fruit.centery == 589:
        print(f"Game over! Your score: {score}")
        sys.exit(0)
    else:
        fruit = fruit.move(0, 3)

    #redraw surface
    gameSurf.fill((0, 0, 0))
    pygame.draw.rect(gameSurf, (255, 0, 0), fruit)
    pygame.draw.rect(gameSurf, (255, 255, 255), basket)
    screen.blit(gameSurf, (0, 0))
    pygame.display.flip()
    clock.tick(60)
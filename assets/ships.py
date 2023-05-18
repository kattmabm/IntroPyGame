from os import path
import pygame

SPEED = 5
WIDTH = 50
HEIGHT = 45
SIZE = (WIDTH, HEIGHT)
YELLOW = pygame.image.load(path.join("assets", "spaceship_yellow.png"))
YELLOW = pygame.transform.scale(YELLOW, SIZE)
RED = pygame.image.load(path.join("assets", "spaceship_red.png"))
RED = pygame.transform.scale(RED, SIZE)
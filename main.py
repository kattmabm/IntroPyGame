import pygame
import os
import constants.color as color
import constants.window as window
import assets.ships as ships

WIN = pygame.display.set_mode(window.SIZE)
pygame.display.set_caption("Learning PyGame!")

BORDER = pygame.Rect(window.BORDER_XMIN, 0, window.BORDER_WIDTH, window.HEIGHT)


def handle_wasd_movement(ship: pygame.Rect, keys: pygame.key.ScancodeWrapper):
    if keys[pygame.K_w]:
        ship.y -= ships.SPEED
    if keys[pygame.K_a]:
        ship.x -= ships.SPEED
    if keys[pygame.K_s]:
        ship.y += ships.SPEED
    if keys[pygame.K_d]:
        ship.x += ships.SPEED

def handle_arrow_movement(ship: pygame.Rect, keys: pygame.key.ScancodeWrapper):
    if keys[pygame.K_UP]:
        ship.y -= ships.SPEED
    if keys[pygame.K_LEFT]:
        ship.x -= ships.SPEED
    if keys[pygame.K_DOWN]:
        ship.y += ships.SPEED
    if keys[pygame.K_RIGHT]:
        ship.x += ships.SPEED


def draw_window(red_ship: pygame.Rect, yellow_ship: pygame.Rect):
    WIN.fill(color.WHITE)
    SHIP_YELLOW = pygame.transform.rotate(ships.YELLOW, -90)
    SHIP_RED = pygame.transform.rotate(ships.RED, 90)
    pygame.draw.rect(WIN, color.BLACK, BORDER)
    WIN.blit(SHIP_YELLOW, (yellow_ship.x, yellow_ship.y))
    WIN.blit(SHIP_RED, (red_ship.x, red_ship.y))
    pygame.display.update()


def main():
    red = pygame.Rect(700, 300, ships.WIDTH, ships.HEIGHT)
    yellow = pygame.Rect(100, 300, ships.WIDTH, ships.HEIGHT)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(window.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        handle_wasd_movement(yellow, keys)
        handle_arrow_movement(red, keys)
        
            

        draw_window(red, yellow)
    pygame.quit()

if __name__ == "__main__":
    main()

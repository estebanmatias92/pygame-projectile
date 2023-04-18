import pygame
from projectile import Projectile

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

projectiles = pygame.sprite.Group()

clock = pygame.time.Clock()

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            projectile = Projectile(x, y)
            projectiles.add(projectile)

    screen.fill((0, 0, 0))

    projectiles.update()
    projectiles.draw(screen)

    pygame.display.flip()

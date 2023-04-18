import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = -5
    

    def update(self):
        self.rect.x -= self.speed
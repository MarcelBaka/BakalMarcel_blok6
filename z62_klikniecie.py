import pygame
import random

pygame.init()
ekran = pygame.display.set_mode((800, 600))
bloki = [{'rect': pygame.Rect(random.randint(0, 750), random.randint(0, 550), 50, 50), 'kolor': (255, 255, 255)} for _ in range(5)]

dziala = True
while dziala:
    for z in pygame.event.get():
        if z.type == pygame.QUIT:
            dziala = False
        if z.type == pygame.MOUSEBUTTONDOWN and z.button == 1:
            for b in bloki:
                if b['rect'].collidepoint(z.pos):
                    b['kolor'] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    ekran.fill((0, 0, 0))
    for b in bloki:
        pygame.draw.rect(ekran, b['kolor'], b['rect'])
    pygame.display.flip()
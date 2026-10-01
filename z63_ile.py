import pygame
import random

pygame.init()
ekran = pygame.display.set_mode((800, 600))
czcionka = pygame.font.Font(None, 36)
bloki = [pygame.Rect(random.randint(0, 750), random.randint(0, 550), 40, 40) for _ in range(10)]
gracz = pygame.Rect(0, 0, 40, 40)

dziala = True
while dziala:
    for z in pygame.event.get():
        if z.type == pygame.QUIT:
            dziala = False

    gracz.center = pygame.mouse.get_pos()
    ile = len(gracz.collidelistall(bloki))

    ekran.fill((0, 0, 0))
    for b in bloki:
        pygame.draw.rect(ekran, (100, 100, 100), b)
    pygame.draw.rect(ekran, (255, 0, 0), gracz)
    ekran.blit(czcionka.render(str(ile), True, (255, 255, 255)), (10, 10))
    pygame.display.flip()
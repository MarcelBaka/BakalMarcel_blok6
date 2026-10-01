import pygame

pygame.init()
ekran = pygame.display.set_mode((800, 600))
zegar = pygame.time.Clock()
gracz = pygame.Rect(100, 100, 50, 50)
cel = pygame.Rect(400, 300, 50, 50)

dziala = True
while dziala:
    dt = zegar.tick(60) / 1000
    for z in pygame.event.get():
        if z.type == pygame.QUIT:
            dziala = False

    k = pygame.key.get_pressed()
    gracz.x += (k[pygame.K_RIGHT] - k[pygame.K_LEFT]) * 300 * dt
    gracz.y += (k[pygame.K_DOWN] - k[pygame.K_UP]) * 300 * dt

    hitbox = gracz.inflate(-20, -20)
    kolor = (255, 0, 0) if hitbox.colliderect(cel) else (0, 255, 0)

    ekran.fill((0, 0, 0))
    pygame.draw.rect(ekran, kolor, gracz, 1)
    pygame.draw.rect(ekran, kolor, hitbox)
    pygame.draw.rect(ekran, kolor, cel)
    pygame.display.flip()
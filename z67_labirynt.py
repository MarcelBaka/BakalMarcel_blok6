import pygame

pygame.init()
ekran = pygame.display.set_mode((800, 600))
zegar = pygame.time.Clock()
czcionka = pygame.font.Font(None, 36)
gracz = pygame.Rect(20, 20, 30, 30)
sciany = [pygame.Rect(0, 0, 800, 10), pygame.Rect(0, 590, 800, 10), pygame.Rect(0, 0, 10, 600), pygame.Rect(790, 0, 10, 600), pygame.Rect(100, 100, 600, 20), pygame.Rect(100, 200, 20, 300), pygame.Rect(200, 200, 500, 20)]
meta = pygame.Rect(700, 500, 50, 50)
x, y = 20.0, 20.0
czas = 0.0
koniec = False

dziala = True
while dziala:
    dt = zegar.tick(60) / 1000
    for z in pygame.event.get():
        if z.type == pygame.QUIT:
            dziala = False

    k = pygame.key.get_pressed()
    if not koniec:
        czas += dt
        vx = (k[pygame.K_RIGHT] - k[pygame.K_LEFT]) * 200
        vy = (k[pygame.K_DOWN] - k[pygame.K_UP]) * 200
        
        x += vx * dt
        gracz.x = x
        for s in sciany:
            if gracz.colliderect(s):
                if vx > 0: gracz.right = s.left
                elif vx < 0: gracz.left = s.right
                x = gracz.x
                
        y += vy * dt
        gracz.y = y
        for s in sciany:
            if gracz.colliderect(s):
                if vy > 0: gracz.bottom = s.top
                elif vy < 0: gracz.top = s.bottom
                y = gracz.y
                
        if gracz.colliderect(meta):
            koniec = True

    ekran.fill((30, 30, 30))
    for s in sciany:
        pygame.draw.rect(ekran, (150, 150, 150), s)
    pygame.draw.rect(ekran, (0, 255, 0), meta)
    pygame.draw.rect(ekran, (255, 0, 0), gracz)
    ekran.blit(czcionka.render(f"Czas: {czas:.1f}", True, (255, 255, 255)), (20, 20))
    pygame.display.flip()
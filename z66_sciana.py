import pygame

pygame.init()
ekran = pygame.display.set_mode((800, 600))
zegar = pygame.time.Clock()
gracz = pygame.Rect(100, 300, 40, 40)
sciana = pygame.Rect(400, 100, 20, 400)
x, y = 100.0, 300.0

dziala = True
while dziala:
    dt = zegar.tick(60) / 1000
    for z in pygame.event.get():
        if z.type == pygame.QUIT:
            dziala = False

    k = pygame.key.get_pressed()
    vx = (k[pygame.K_RIGHT] - k[pygame.K_LEFT]) * 300
    vy = (k[pygame.K_DOWN] - k[pygame.K_UP]) * 300
    
    x += vx * dt
    gracz.x = x
    if gracz.colliderect(sciana):
        if vx > 0: gracz.right = sciana.left
        elif vx < 0: gracz.left = sciana.right
        x = gracz.x
        
    y += vy * dt
    gracz.y = y
    if gracz.colliderect(sciana):
        if vy > 0: gracz.bottom = sciana.top
        elif vy < 0: gracz.top = sciana.bottom
        y = gracz.y
        
    ekran.fill((0, 0, 0))
    pygame.draw.rect(ekran, (100, 100, 100), sciana)
    pygame.draw.rect(ekran, (0, 255, 0), gracz)
    pygame.display.flip()
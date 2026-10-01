import pygame
import math

pygame.init()
EKRAN = pygame.Rect(0, 0, 900, 600)
ekran = pygame.display.set_mode(EKRAN.size)
zegar = pygame.time.Clock()
czcionka = pygame.font.Font(None, 24)

sposob = 1
x, y = 60.0, 300.0
vx, vy = 0.0, 0.0
gracz = pygame.Rect(0, 0, 40, 40)
przeszkody = [pygame.Rect(300, 100, 50, 200), pygame.Rect(500, 400, 50, 200), pygame.Rect(600, 100, 50, 200)]
meta = pygame.Rect(880, 0, 20, 600)
czas = 0.0
dotkniecia = 0
koniec = False

def st_natychmiast(x, y, dt, k):
    dx = k[pygame.K_RIGHT] - k[pygame.K_LEFT]
    dy = k[pygame.K_DOWN] - k[pygame.K_UP]
    return x + dx * 320 * dt, y + dy * 320 * dt

def st_mysz(x, y, dt):
    mx, my = pygame.mouse.get_pos()
    dx, dy = mx - x, my - y
    odl = math.hypot(dx, dy)
    if odl > 3:
        x += dx / odl * 320 * dt
        y += dy / odl * 320 * dt
    return x, y

def st_rozped(x, y, vx, vy, dt, k):
    kx = k[pygame.K_RIGHT] - k[pygame.K_LEFT]
    ky = k[pygame.K_DOWN] - k[pygame.K_UP]
    vx += kx * 900 * dt
    vy += ky * 900 * dt
    if kx == 0: vx = max(0, vx - 700 * dt) if vx > 0 else min(0, vx + 700 * dt)
    if ky == 0: vy = max(0, vy - 700 * dt) if vy > 0 else min(0, vy + 700 * dt)
    vx = max(-320, min(320, vx))
    vy = max(-320, min(320, vy))
    return x + vx * dt, y + vy * dt, vx, vy

dziala = True
while dziala:
    dt = zegar.tick(60) / 1000
    for z in pygame.event.get():
        if z.type == pygame.QUIT:
            dziala = False
        if z.type == pygame.KEYDOWN:
            if z.key == pygame.K_1: sposob = 1
            if z.key == pygame.K_2: sposob = 2
            if z.key == pygame.K_3: sposob = 3
            if z.key == pygame.K_r:
                x, y, vx, vy, czas, dotkniecia, koniec = 60.0, 300.0, 0.0, 0.0, 0.0, 0, False

    k = pygame.key.get_pressed()
    if not koniec:
        czas += dt
        stare_rect = gracz.copy()
        if sposob == 1: x, y = st_natychmiast(x, y, dt, k)
        elif sposob == 2: x, y = st_mysz(x, y, dt)
        else: x, y, vx, vy = st_rozped(x, y, vx, vy, dt, k)
        
        gracz.center = (x, y)
        gracz.clamp_ip(EKRAN)
        x, y = gracz.center
        
        if gracz.collidelist(przeszkody) != -1 and stare_rect.collidelist(przeszkody) == -1:
            dotkniecia += 1
        if gracz.colliderect(meta):
            koniec = True
    
    ekran.fill((30, 30, 30))
    for p in przeszkody:
        pygame.draw.rect(ekran, (200, 50, 50), p)
    pygame.draw.rect(ekran, (50, 200, 50), meta)
    pygame.draw.rect(ekran, (200, 200, 200), gracz)
    ekran.blit(czcionka.render(f"Sposob: {sposob} | Czas: {czas:.1f} | Dotkniecia: {dotkniecia}", True, (255,255,255)), (10, 10))
    pygame.display.flip()
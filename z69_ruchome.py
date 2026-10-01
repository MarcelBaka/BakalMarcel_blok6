import pygame
import random

pygame.init()
ekran = pygame.display.set_mode((800, 600))
zegar = pygame.time.Clock()
czcionka = pygame.font.Font(None, 36)
x, y = 400.0, 300.0
gracz = pygame.Rect(0, 0, 40, 40)
punkty, zycia, predkosc, porcje, nietykalnosc = 0, 3, 300.0, 0, 0.0

kolce = [{'r': pygame.Rect(random.randint(50, 750), random.randint(50, 550), 40, 40), 'vx': random.choice([-150, 150]), 'vy': random.choice([-150, 150])} for _ in range(5)]

def generuj_monety():
    return [{'r': pygame.Rect(random.randint(50, 750), random.randint(50, 550), s, s), 'w': w} for s, w in [(16, 50), (24, 25), (32, 10)] for _ in range(5)]
monety = generuj_monety()

dziala = True
while dziala:
    dt = zegar.tick(60) / 1000
    for z in pygame.event.get():
        if z.type == pygame.QUIT:
            dziala = False

    if zycia > 0:
        k = pygame.key.get_pressed()
        x += (k[pygame.K_RIGHT] - k[pygame.K_LEFT]) * predkosc * dt
        y += (k[pygame.K_DOWN] - k[pygame.K_UP]) * predkosc * dt
        gracz.center = (x, y)
        gracz.clamp_ip(ekran.get_rect())
        x, y = gracz.center

        if nietykalnosc > 0:
            nietykalnosc -= dt

        hitbox = gracz.inflate(-10, -10)
        for m in monety[:]:
            if hitbox.colliderect(m['r']):
                punkty += m['w']
                monety.remove(m)

        if not monety:
            monety = generuj_monety()
            predkosc *= 1.1
            porcje += 1

        for k_obj in kolce:
            k_obj['r'].x += k_obj['vx'] * dt
            k_obj['r'].y += k_obj['vy'] * dt
            if k_obj['r'].left < 0 or k_obj['r'].right > 800: k_obj['vx'] *= -1
            if k_obj['r'].top < 0 or k_obj['r'].bottom > 600: k_obj['vy'] *= -1
            
            if nietykalnosc <= 0 and hitbox.colliderect(k_obj['r']):
                zycia -= 1
                nietykalnosc = 1.5

    ekran.fill((0, 0, 0))
    for k_obj in kolce:
        pygame.draw.rect(ekran, (255, 0, 0), k_obj['r'])
    for m in monety:
        pygame.draw.ellipse(ekran, (255, 255, 0), m['r'])
    if nietykalnosc <= 0 or int(nietykalnosc * 10) % 2 == 0:
        pygame.draw.rect(ekran, (0, 255, 0), gracz)

    tekst = f"Punkty: {punkty} Zycia: {zycia}" if zycia > 0 else f"KONIEC! Wynik: {punkty}, Porcje: {porcje}"
    ekran.blit(czcionka.render(tekst, True, (255, 255, 255)), (10, 10))
    pygame.display.flip()
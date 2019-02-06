import pygame,sys;

max_tps = 100.0
pygame.init()
# rozmiar okienka
screen = pygame.display.set_mode((1280,720))
# rozmiar i położenie początkowe przedmiotu
box = pygame.Rect(250,250,100,100)
clock=pygame.time.Clock()
delta = 0.0
while True:
    # Obsługa zdarzeń
    for event in pygame.event.get():
        # zamykanie okienka X i minimalizowanie
        if event.type == pygame.QUIT:
            sys.exit(0)
        #Wyjście escapem
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)

    #Ticking
    delta += clock.tick()/1000.0
    while delta >1 / max_tps:
        delta -=1/max_tps

        #poruszanie klawiszami
        keys =pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            box.x +=1
        if keys[pygame.K_LEFT]:
            box.x -=1
        if keys[pygame.K_UP]:
            box.y -=1
        if keys[pygame.K_DOWN]:
            box.y +=1
    # efekt, że rysunek się przemieszcza, a nie zostawia ślad
    screen.fill((0,0,0))
    #rysowanie tego przedmiotu, kolor
    pygame.draw.rect(screen,(0,255,0),box)
    #dzięki temu się pojawia
    pygame.display.flip()
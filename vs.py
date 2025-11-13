import pygame
tela_largura = 950
tela_altura = 700
prot_altura = 150
prot_largura = 10
velocidade = 10
p1_x, p1_y = 50,325
p2_x, p2_y = 850,325

tela = pygame.display.set_mode((tela_largura, tela_altura))
fps = pygame.time.Clock()
rodando = True
while rodando:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    p1 = pygame.draw.rect(tela,(255,255,255), (p1_x, p1_y,prot_largura, prot_altura))
    p2 = pygame.draw.rect(tela,(255,255,255), (p2_x, p2_y,prot_largura, prot_altura))
    pygame.display.update()
    controles = pygame.key.get_pressed()
    if controles[pygame.K_w] and p1_y >= 0:
        p1_y -= velocidade
    if controles[pygame.K_s] and p1_y < 650 - prot_altura - velocidade:
        p1_y += velocidade
    if controles[pygame.K_UP] and p2_y >= 0:
        p2_y -= velocidade
    if controles[pygame.K_DOWN] and p2_y < 650 - prot_altura - velocidade:
        p2_y += velocidade
    tela.fill((0,0,0))

    bola_px, bola_py = 445,350
    bola = pygame.draw.rect(tela, (255,255,255), (bola_px,bola_py,30,30))
    bola_velx, bola_vely = 5,5
    bola_px += bola_velx
    fps.tick(60)



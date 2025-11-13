import pygame
tela_largura = 950
tela_altura = 700
prot_altura = 150
prot_largura = 10
velocidade = 5
p1_x, p1_y = 50,325
p2_x, p2_y = 900,325
bola_px, bola_py = 445,350
bola_velx, bola_vely = 4.5,4.5

tela = pygame.display.set_mode((tela_largura, tela_altura))
fps = pygame.time.Clock()
rodando = True
while rodando:
    fps.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    
    controles = pygame.key.get_pressed()
    if controles[pygame.K_w] and p1_y >= 0:
        p1_y -= velocidade
    if controles[pygame.K_s] and p1_y < tela_altura - prot_altura - velocidade:
        p1_y += velocidade
    if controles[pygame.K_UP] and p2_y >= 0:
        p2_y -= velocidade
    if controles[pygame.K_DOWN] and p2_y < tela_altura - prot_altura - velocidade:
        p2_y += velocidade

    bola_px += bola_velx
    bola_py += bola_vely

    if bola_py <= 0 or bola_py >= tela_altura - 30:
        bola_vely = -bola_vely

    tela.fill((0,0,0))
    p1 = pygame.draw.rect(tela,(255,255,255), (p1_x, p1_y,prot_largura, prot_altura))
    p2 = pygame.draw.rect(tela,(255,255,255), (p2_x, p2_y,prot_largura, prot_altura))
    bola = pygame.draw.rect(tela, (255,255,255), (bola_px,bola_py,30,30))
    if bola.colliderect(p1) or bola.colliderect(p2):
        bola_velx = -bola_velx
    pygame.display.flip()
    
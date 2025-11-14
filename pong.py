import pygame
pygame.init()
#banco de variáveis
tela_largura = 950
tela_altura = 700

prot_altura = 150
prot_largura = 10
velocidade = 5
p1_x, p1_y = 0,325
p2_x, p2_y = 940,325
pontos_p1 = 0
pontos_p2 = 0
pontos_vit = 10
font = pygame.font.Font(None, 60)

bola_px, bola_py = 445,350
bola_velx, bola_vely = 4.5,4.5
bola_raio = 15

tela = pygame.display.set_mode((tela_largura, tela_altura))
fps = pygame.time.Clock()
rodando = True

#loop principal
while rodando:
    fps.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    #controles
    controles = pygame.key.get_pressed()
       #$controles player 1
    if controles[pygame.K_w] and p1_y >= 0:
        p1_y -= velocidade
    if controles[pygame.K_s] and p1_y < tela_altura - prot_altura - velocidade:
        p1_y += velocidade
       #$controles player 2
    if controles[pygame.K_UP] and p2_y >= 0:
        p2_y -= velocidade
    if controles[pygame.K_DOWN] and p2_y < tela_altura - prot_altura - velocidade:
        p2_y += velocidade

    #movimento da bola
    bola_px += bola_velx
    bola_py += bola_vely

    if bola_py - bola_raio <= 0 or bola_py + bola_raio >= tela_altura:
        bola_vely = -bola_vely
    bola_rect = pygame.Rect(bola_px - bola_raio, bola_py - bola_raio, bola_raio * 2, bola_raio * 2)
    
    #tela/colisões/players
    tela.fill((0,0,0))
    p1 = pygame.draw.rect(tela,(255,255,255), (p1_x, p1_y,prot_largura, prot_altura))
    p2 = pygame.draw.rect(tela,(255,255,255), (p2_x, p2_y,prot_largura, prot_altura))
    placar_texto = font.render(f"{pontos_p1}     {pontos_p2}", True,(255,255,255))
    tela.blit(placar_texto, (tela_largura // 2 - 50, 20))
    bola = pygame.draw.circle(tela, (255,255,255), (int(bola_px), int(bola_py)), bola_raio)
    if bola_rect.colliderect(p1) or bola_rect.colliderect(p2):
        bola_velx = -bola_velx
    if bola_px < 0:
        pontos_p2 += 1
        bola_px, bola_py = tela_largura // 2, tela_altura // 2
        bola_velx = -bola_velx
    if bola_px > tela_largura:
        pontos_p1 += 1
        bola_px, bola_py = tela_largura // 2, tela_altura // 2
        bola_velx = -bola_velx

    if pontos_p1 >= pontos_vit or pontos_p2 >= pontos_vit:
        rodando = False

    pygame.display.flip()
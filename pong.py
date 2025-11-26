import pygame
import random
pygame.init()
#banco de variáveis
tela_largura = 950
tela_altura = 700
prot_altura_original = 150
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

#função dos powerups
powerup_ativo = False
powerup_x = 0
powerup_y = 0
powerup_tamanho = 40
powerup_tempo = 0          
powerup_intervalo = 180 
powerup_efeito = None 
powerup_efeito_tempo = 0
def powerspwn():
    global powerup_ativo, powerup_tempo, powerup_x, powerup_y
    powerup_x = random.randint(50, tela_largura - 50)
    powerup_y = random.randint(50, tela_altura - 50)
    powerup_tempo = 300
    powerup_ativo = True

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
    if bola_rect.colliderect(p1):
        bola_velx = -bola_velx
        bola_vely += 1
        bola_velx += 1
    elif bola_rect.colliderect(p2):
        bola_velx = -bola_velx
        bola_velx -= 1
        bola_vely -= 1       
    if bola_px < 0:
        pontos_p2 += 1
        bola_px, bola_py = tela_largura // 2, tela_altura // 2
        bola_velx = -bola_velx
        bola_velx, bola_vely = 4.5, 4.5
    if bola_px > tela_largura:
        pontos_p1 += 1
        bola_px, bola_py = tela_largura // 2, tela_altura // 2
        bola_velx = -bola_velx
        bola_velx, bola_vely = 4.5, 4.5
    if pontos_p1 >= pontos_vit or pontos_p2 >= pontos_vit:
        rodando = False

    #powerups
    if not powerup_ativo:
        if random.randint(0, powerup_intervalo) == 0:
            powerspwn()
    
    else:
        powerup_tempo -= 1
        if powerup_tempo <= 0:
            powerup_ativo = False

    if powerup_ativo:
        powerup_rect = pygame.draw.rect(tela, (0,255,0),(powerup_x, powerup_y, powerup_tamanho, powerup_tamanho))
    
    if powerup_ativo and bola_rect.colliderect(powerup_rect):
        powerup_ativo = False

        efeito = random.choice(["velocidade+","colisão maior","velocidade-","colisão menor"])

        if efeito == "velocidade+":
            bola_velx *= 2
            bola_vely *= 2
            powerup_efeito = "velocidade+"
            powerup_efeito_tempo = 300
        
        elif efeito == "colisão maior":
            prot_altura = max(50, prot_altura + 100)
            powerup_efeito = "colisão maior"
            powerup_efeito_tempo = 300

        elif efeito == "colisão menor":
            prot_altura = max (50, prot_altura / 2)
            powerup_efeito = "colisão menor"
            powerup_efeito_tempo = 300

        elif efeito == "velocidade-":
            bola_velx /= 2
            bola_vely /= 2
            powerup_efeito = "velocidade-"
            powerup_efeito_tempo = 300
        
    if powerup_efeito is not None:
            powerup_efeito_tempo -= 1

            if powerup_efeito_tempo <= 0:
                
                if powerup_efeito in ["colisão maior","colisão menor"]:
                    prot_altura = prot_altura_original               
                elif powerup_efeito == "velocidade+":
                    bola_velx /= 2
                    bola_vely /= 2
                elif powerup_efeito == "velocidade-":
                    bola_vely *= 1.5
                    bola_velx *= 1.5

                powerup_efeito = None   
            
   
    pygame.display.flip()
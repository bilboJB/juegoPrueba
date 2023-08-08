import pygame
from sys import exit
from random import randint
pygame.init()
game_Active = True
def movimiento_enemigo(enemigos_list):
    if enemigos_list:
        for enemigos_rect in enemigos_list:
            enemigos_rect.x -= 5
            if enemigos_rect.bottom == 300:
                screen.blit(slime,enemigos_rect)
            else:
                screen.blit(fantasma,enemigos_rect)
        enemigos_list = [enemigo for enemigo in enemigos_list if enemigo.x > -16]
        return enemigos_list
    else:
        return []
def colisiones(player,enemigos_list):
    if enemigos_list:
        for enemigos_rect in enemigos_list:
             if player.colliderect(enemigos_rect):
                 return False
    return True

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Proyecto")
reloj = pygame.time.Clock()
fondo = pygame.Surface((800,400))
fondo.fill("cyan4")
piso = pygame.Surface((800,100))
piso.fill("darkgoldenrod")
font = pygame.font.Font("font/NotJamSlab14.ttf",50)
texto = font.render("le bomb",False,"cornsilk")
textoOver = font.render("GAME OVER",False,"white")
texto_Rect = texto.get_rect(center = (300,50))
fantasma = pygame.image.load("Characters/Enemies/sprites/Ghost/ghost1.png").convert_alpha()
slime = pygame.image.load("Characters/Enemies/sprites/Slime/slime3.png").convert_alpha()
enemigos_rect_list = []
player = pygame.image.load("Characters/Player/sprites/Player-run/player-run1.png").convert_alpha()
player_Rect = player.get_rect(bottomright = (80,300))
gravedad = 0
timer_enemigos = pygame.USEREVENT + 1
pygame.time.set_timer(timer_enemigos,1400)
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_Active:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and player_Rect.bottom >= 300:
                    gravedad = -15
            if evento.type == timer_enemigos:
                if randint(0,1):
                    enemigos_rect_list.append(fantasma.get_rect(midbottom = (900,250)))
                else:
                    enemigos_rect_list.append(slime.get_rect(midbottom = (900,300)))
        else:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                game_Active = True
        
    if game_Active:
        screen.blit(fondo,(0,0))
        screen.blit(piso,(0,300))
        screen.blit(texto,texto_Rect)
        gravedad +=1
        player_Rect.y += gravedad
        enemigos_rect_list = movimiento_enemigo(enemigos_rect_list)
        if player_Rect.bottom >= 300:
            player_Rect.bottom = 300
        screen.blit(player,player_Rect)
        game_Active = colisiones(player_Rect,enemigos_rect_list)
    else:
        screen.fill("cyan4")
        screen.blit(textoOver,texto_Rect)
        enemigos_rect_list.clear()
        player_Rect.bottom = 300
    pygame.display.update()
    reloj.tick(60)
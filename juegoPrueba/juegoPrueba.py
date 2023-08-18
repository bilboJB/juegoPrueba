import pygame
from sys import exit
from random import randint
pygame.init()
game_Active = True
def movimiento_Enemigo(enemigos_list):
    if enemigos_list:
        for enemigos_rect in enemigos_list:
            enemigos_rect.x -= 5
            if enemigos_rect.bottom == 300:
                screen.blit(slime_Surf,enemigos_rect)
            else:
                screen.blit(fantasma_Surf,enemigos_rect)
        enemigos_list = [enemigo for enemigo in enemigos_list if enemigo.x > -16]
        return enemigos_list
    else:
        return []
def colisiones_Player(player,enemigos_list):
    if enemigos_list:
        for enemigos_rect in enemigos_list:
             if player.colliderect(enemigos_rect):
                 return False
    return True
def player_Animacion():
    global player_Index
    if player_Rect.bottom < 300:
        return player_Jump
    elif player_Index == 10:
        player_Index = 0
        return player_Shoot
    else:
        player_Index += 0.1
        if player_Index > len(player_Run):
            player_Index = 0
        return player_Run[int(player_Index)]
def movimiento_Proyectil(proyectil_List):
    if proyectil_List:
        for proyectil_Rect in proyectil_List:
            proyectil_Rect.x +=3
            screen.blit(proyectil,proyectil_Rect)
        proyectil_List = [proyectil for proyectil in proyectil_List if proyectil.x < 900]
        return proyectil_List
    else:
        return []
def mostrar_Score(puntos):
    score_Surf = font.render(f"{puntos}",False,"cornsilk")
    score_Rect = score_Surf.get_rect(center = (400,50))
    screen.blit(score_Surf,score_Rect)
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Proyecto")
reloj = pygame.time.Clock()
fondo = pygame.image.load("Characters/Enviroment/cielo.png").convert_alpha()
piso = pygame.image.load("Characters/Enviroment/piso.png").convert_alpha()
proyectil = pygame.Surface((5,3))
proyectil.fill("white")
proyectil_Rect_List = []
font = pygame.font.Font("font/NotJamSlab14.ttf",50)
texto = font.render("le bomb",False,"cornsilk")
textoOver = font.render("GAME OVER",False,"white")
texto_Rect = texto.get_rect(center = (300,200))
fantasma_1 = pygame.image.load("Characters/Enemies/sprites/Ghost/ghost1.png").convert_alpha()
fantasma_2 = pygame.image.load("Characters/Enemies/sprites/Ghost/ghost2.png").convert_alpha()
fantasma = [fantasma_1,fantasma_2]
fantasma_Index = 0
fantasma_Surf = fantasma[fantasma_Index]
slime_1 = pygame.image.load("Characters/Enemies/sprites/Slime/slime1.png").convert_alpha()
slime_2 = pygame.image.load("Characters/Enemies/sprites/Slime/slime2.png").convert_alpha()
slime = [slime_1,slime_2]
slime_Index = 0
slime_Surf = slime[slime_Index]
enemigos_rect_list = []
player_Run1 = pygame.image.load("Characters/Player/sprites/Player-run/player-run1.png").convert_alpha()
player_Run2 = pygame.image.load("Characters/Player/sprites/Player-run/player-run2.png").convert_alpha()
player_Run3 = pygame.image.load("Characters/Player/sprites/Player-run/player-run3.png").convert_alpha()
player_Index = 0
player_Run = [player_Run1,player_Run2,player_Run3]
player_Jump = pygame.image.load("Characters/Player/sprites/Player-jump/player-jump1.png").convert_alpha()
player_Shoot = pygame.image.load("Characters/Player/sprites/Player-shoot/player-shoot3.png").convert_alpha()
player_Surf = player_Run[player_Index]
player_Rect = player_Surf.get_rect(bottomright = (80,300))
gravedad = 0
puntaje = 0
timer_enemigos = pygame.USEREVENT + 1
pygame.time.set_timer(timer_enemigos,1000)
timer_Fantasma = pygame.USEREVENT + 2
pygame.time.set_timer(timer_Fantasma,450)
timer_Slime = pygame.USEREVENT + 3
pygame.time.set_timer(timer_Slime,500)
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_Active:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and player_Rect.bottom >= 300:
                    gravedad = -15
                if evento.key == pygame.K_RETURN and len(proyectil_Rect_List)<8:
                    proyectil_Rect_List.append(proyectil.get_rect(midleft = player_Rect.midright))
                    player_Index = 10
            if evento.type == timer_enemigos:
                if randint(0,1):
                    enemigos_rect_list.append(fantasma_1.get_rect(midbottom = (900,250)))
                else:
                    enemigos_rect_list.append(slime_1.get_rect(midbottom = (900,300)))
            if evento.type == timer_Fantasma:
                if fantasma_Index == 0:
                    fantasma_Index = 1
                else:
                    fantasma_Index = 0
                fantasma_Surf = fantasma[fantasma_Index]
            if evento.type == timer_Slime:
                if slime_Index == 0:
                    slime_Index = 1
                else:
                    slime_Index = 0
                slime_Surf = slime[slime_Index]
        else:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                game_Active = True
                puntaje = 0
        
    if game_Active:
        screen.blit(fondo,(0,0))
        screen.blit(piso,(0,300))
        if gravedad < 100:
            gravedad +=1
        player_Rect.y += gravedad
        enemigos_rect_list = movimiento_Enemigo(enemigos_rect_list)
        proyectil_Rect_List = movimiento_Proyectil(proyectil_Rect_List)
        if player_Rect.bottom >= 300:
            player_Rect.bottom = 300
        for proyectils in proyectil_Rect_List:
            for enemigo in enemigos_rect_list:
                if proyectils.colliderect(enemigo):
                    proyectil_Rect_List.remove(proyectils)
                    enemigos_rect_list.remove(enemigo)
                    puntaje += 1
        player_Surf_Actual = player_Animacion()
        screen.blit(player_Surf_Actual,player_Rect)
        mostrar_Score(puntaje)
        game_Active = colisiones_Player(player_Rect,enemigos_rect_list)
    else:
        screen.fill("cyan4")
        screen.blit(textoOver,texto_Rect)
        mostrar_Score(puntaje)
        enemigos_rect_list.clear()
        proyectil_Rect_List.clear()
        player_Rect.bottom = 300
    pygame.display.update()
    reloj.tick(60)
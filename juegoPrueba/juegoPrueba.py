import pygame
from sys import exit
pygame.init()
game_Active = True
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
fantasma_Rect = fantasma.get_rect(midbottom = (600,300))
player = pygame.image.load("Characters/Player/sprites/Player-run/player-run1.png").convert_alpha()
player_Rect = player.get_rect(bottomright = (80,300))
gravedad = 0
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_Active:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE and player_Rect.bottom >= 300:
                    gravedad = -15
        else:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                game_Active = True
                fantasma_Rect.left = 800
    if game_Active:
        screen.blit(fondo,(0,0))
        screen.blit(piso,(0,300))
        screen.blit(texto,texto_Rect)
        gravedad +=1
        player_Rect.y += gravedad
        if player_Rect.bottom >= 300:
            player_Rect.bottom = 300
        fantasma_Rect.x -= 3
        if fantasma_Rect.right < 0:
            fantasma_Rect.left = 800
        screen.blit(fantasma,fantasma_Rect)
        screen.blit(player,player_Rect)
        if fantasma_Rect.colliderect(player_Rect):
            game_Active = False
    else:
        screen.fill("cyan4")
        screen.blit(textoOver,texto_Rect)
    pygame.display.update()
    reloj.tick(60)
import pygame

pygame.init()

screen=pygame.display.set_mode((500,500))

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=False

    pygame.draw.rect(screen,(0,125,200),pygame.Rect(60,70,60,70))
    pygame.display.flip()
    
    
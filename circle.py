import pygame

pygame.init()

screen=pygame.display.set_mode((500,500))

screen.fill((0,0,0))

gr=(0,255,0)

pygame.draw.circle(screen,gr,(100,100),50,3)
pygame.draw.circle(screen,gr,(300,300),50)

pygame.display.update()

run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
            
pygame.quit()            





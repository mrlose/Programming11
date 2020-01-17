import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
done=False

object_list=[]

for i in range(30):
    x=random.randint(0,400)
    y=random.randint(-300, 0)
    object_list.append([x,y])

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0,0,0))
    
    for i in range(30):
        pygame.draw.circle(screen,(255,255,255), object_list[i], 5)
        
        object_list[i][1] += 1

        if object_list[i][1] > 300:
            y=random.randint(-300, 0)
            object_list[i][1] = y
            x=random.randint(0,400)
            object_list[i][0] = x

    pygame.display.flip()
    clock.tick(20)

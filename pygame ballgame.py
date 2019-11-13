import pygame
import os
x=100
y=100
x1=1
y1=100
speed1=3
speed2=3

_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
                image = pygame.image.load(canonicalized_path)
                _image_library[path] = image
        return image

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        screen.fill((255, 255, 255))
        
        screen.blit(get_image('ball.png'), (x, y))
        
        color = (0, 128, 255)
        pygame.draw.rect(screen, color, pygame.Rect(x1, y1 ,5, 60))
        pygame.display.flip()
        clock.tick(60)
        
        x=x+speed1
        y=y+speed2

        if x>400:
                speed1=speed1*-1
        if y<0 or y>300:
                speed2=speed2*-1
        if (y1-50)<y<(y1+50) and (x1-6)<x<(x1+5):
                speed1=speed1*-1
                speed2=speed2*-1

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: y1 -= 3
        if pressed[pygame.K_DOWN]: y1 += 3

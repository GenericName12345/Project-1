import sys, pygame
from pygame.locals import *

pygame.init()


screen_info = pygame.display.Info()
x = screen_info.current_w
y = screen_info.current_h
screen = pygame.display.set_mode((x, y))
Clock = pygame.time.Clock()
Color = (0, 0, 255)
image = pygame.image.load("fish.png")
rect = image.get_rect()
rect.center = (x//2, y//2)

speed = pygame.math.Vector2(-1,-1)
def update ():
    rect.move_ip(speed)

def main():
    print("Hello World")
    while   True:
        Clock.tick(60)
        screen.fill(Color)
        update()
        screen.blit(image, rect)
        pygame.display.flip()

if __name__ == "__main__":
    main()

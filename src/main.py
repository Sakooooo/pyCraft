import pygame
import sys 

pygame.init()

if (pygame.get_init() == False):
    print("[ERROR] pygame failed init")
    print(pygame.get_error())
    sys.exit(1)

isRunning = True

window = pygame.display.set_mode((800, 800))


while (isRunning):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            isRunning = False

print("Pygame has exited sucessfully :)")
sys.exit(0)



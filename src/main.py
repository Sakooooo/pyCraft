import pygame
import sys 
import os

pygame.init()

if (pygame.get_init() == False):
    print("[ERROR] pygame failed init")
    print(pygame.get_error())
    sys.exit(1)

isRunning = True

window = pygame.display.set_mode((1000, 700))

testimg = pygame.image.load(os.path.join("./res/test.png"))

while (isRunning):
    # TODO(sako):: make this a different file
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            isRunning = False
    window.fill("grey")

    #window.blit(testimg, (0, 0))

    pygame.display.flip()

print("Pygame has exited sucessfully :)")
# quit
pygame.quit
# just incase
sys.exit(0)



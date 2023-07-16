import pygame
import sys 
import os
import cube

pygame.init()

if (pygame.get_init() == False):
    print("[ERROR] pygame failed init")
    print(pygame.get_error())
    sys.exit(1)

fov = 90
lookSpeed = 10
WIDTH , HEIGHT = 1000, 700

camera_rot_y = 0 
camera_rot_x = 0 
camera_rot_z = 0

isRunning = True

window = pygame.display.set_mode((WIDTH, HEIGHT))

time = pygame.time.Clock()

pygame.display.set_caption("PyCraft!")

cubeimg = pygame.image.load(os.path.join("./res/cube.png"))



while (isRunning):
    # TODO(sako):: make this a different file
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            cube.drawCube()
            if event.key == pygame.K_q:
                isRunning = False 
    window.fill("BLACK")

    time.tick(60) 

print("Pygame has exited sucessfully :)")
pygame.quit
sys.exit(0)



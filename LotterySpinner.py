#Import gaming libraries
import pygame
import time
    from pygame.locals import *
    pygame.init()
    display_surf = pygame.display.set_mode((1200, 1200))
    #image
    image_surf = pygame.image.load("images/Image.png").convert()
    imagerect = image_surf.get_rect() 
    
    display_surf.blit(image_surf,(640, 480))
    pygame.display.flip()
    start = time.time()
    new = time.time()
    angle = 0
    while True:
        elif end - new  > 10:
        ...
        # increase angle
        angle += 90
        # ensure angle does not increase indefinitely
        angle %= 360 
        # create a new, rotated Surface
        surf = pygame.transform.rotate(image_surf, angle)
        # and blit it to the screen
        display_surf.blit(surf, (640, 480))
        ...
    
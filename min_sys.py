import pygame

pygame.init()
window = pygame.display.set_mode((1280,720))
pygame.display.set_caption("BlueNotes",)
pygame.display.set_icon(pygame.image.load("assets/images/ui/icon.png").convert_alpha())

isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        pass

pygame.quit()
import pygame

pygame.init()
window = pygame.display.set_mode((1280,720))
pygame.display.set_caption("BlueNotes",)
pygame.display.set_icon(pygame.image.load("assets/images/ui/icon.png").convert_alpha())

window_w,window_h = window.get_size()

ini_bg = pygame.image.load("assets/images/ui/icon.png").convert_alpha()
ini_bg_w,ini_bg_h = ini_bg.get_size()
window.blit(ini_bg,(window_w/2-ini_bg_w/2,window_h/2-ini_bg_w/2))
pygame.display.flip()
isRunning = True
while isRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        pass

pygame.quit()
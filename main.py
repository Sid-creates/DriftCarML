import pygame

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.font.SysFont('Cascadia Code', 18)
pygame.display.set_caption("Drift Car ML")

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # if the window is closed, the game ends
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: # if the key is pressed print or game end
                run = False
            if event.key == pygame.K_w:
                print("W key pressed")
            if event.key == pygame.K_a:
                print("A key pressed")
            if event.key == pygame.K_s:
                print("S key pressed")
            if event.key == pygame.K_d:
                print("D key pressed")

    screen.fill((0, 0, 0)) # fill the screen with black

    pygame.display.flip()

pygame.quit()

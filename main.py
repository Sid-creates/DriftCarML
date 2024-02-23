import pygame

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.font.SysFont('Cascadia Code', 18)
pygame.display.set_caption("Drift Car ML")

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill((255, 255, 255))

    pygame.display.flip()

pygame.quit()

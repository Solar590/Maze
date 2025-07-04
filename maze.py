import pygame
pygame.init()

LENGTH = 900
HEIGHT = 600
display = pygame.display.set_mode((LENGTH, HEIGHT))

pygame.display.set_caption("Maze Runner")

FPS = 20
clock = pygame.time.Clock()

p_x = 20
p_y = 20

running = True

while running:

    wall_1 = pygame.draw.rect(display, "red", (60, 0, 15, 115))
    wall_2 = pygame.draw.rect(display, "orange", (60, 0, 900, 15))
    wall_3 = pygame.draw.rect(display, "yellow", (750, 450, 150, 15))
    wall_4 = pygame.draw.rect(display, "green", (300, 110, 15, 90))
    wall_5 = pygame.draw.rect(display, "green", (60, 110, 510, 15))
    wall_6 = pygame.draw.rect(display, "cyan", (885, 0, 15, 600))
    wall_7 = pygame.draw.rect(display, "blue", (75, 450, 510, 15))
    wall_8 = pygame.draw.rect(display, "violet", (0, 585, 810, 15))
    wall_9 = pygame.draw.rect(display, "purple", (660, 90, 15, 810))
    wall_10 = pygame.draw.rect(display, "magenta", (150, 285, 650, 15))
    wall_11 = pygame.draw.rect(display, "violet", (60, 0, 15, 300))
    wall_12 = pygame.draw.rect(display, "pink", (60, 450, 15, 300))
    
    p = pygame.draw.rect(display, "white", (p_x, p_y, 20, 20))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                 p_x -= 20
            if event.key == pygame.K_RIGHT:
                 p_x += 20
            if event.key == pygame.K_UP:
                 p_y -= 20
            if event.key == pygame.K_DOWN:
                 p_y += 20

    if p.colliderect(wall_1):
        display.fill("black")
        pygame.display.update()
        running = False
    if p.colliderect(wall_2):
        display.fill("black")
        pygame.display.update()
        running = False
    if p.colliderect(wall_3):
        display.fill("black")
        pygame.display.update()
        running = False
    if p.colliderect(wall_4):
        display.fill("black")
        pygame.display.update()
        running = False
    if p.colliderect(wall_5):
        display.fill("black")
        pygame.display.update()
        running = False
    if p.colliderect(wall_6):
        display.fill("black")
        pygame.display.update()
        running = False
    if p.colliderect(wall_7):
        display.fill("black")
        pygame.display.update()
        running = False
    if p.colliderect(wall_8):
        display.fill("black")
        pygame.display.update()
        running = False
    if p.colliderect(wall_9):
        display.fill("black")
        pygame.display.update()
        running = False
    if p.colliderect(wall_10):
        display.fill("black")
        pygame.display.update()
        running = False
    if p.colliderect(wall_11):
        display.fill("black")
        pygame.display.update()
        running = False
    if p.colliderect(wall_12):
        display.fill("black")
        pygame.display.update()
        running = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
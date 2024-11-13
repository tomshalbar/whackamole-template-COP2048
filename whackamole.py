import pygame
import random



from main import screen

mole_image = pygame.image.load("mole.png")


def draw_grid():
    for i in range(1, 20):
        pygame.draw.line(
            screen,
            (255, 255, 255),
            (i*32 ,0),
            (i*32 , 512),
            2
        )

    for i in range(1, 16):
        pygame.draw.line(
            screen,
            (255, 255, 255),
            (0, i*32),
            (640, i*32),
            2
        )

def moveMoleToRand():
    randx = random.randrange(0, 20)
    randy = random.randrange(0, 16)
    screen.fill("light green")
    draw_grid()
    screen.blit(mole_image, mole_image.get_rect(center = (16 + randx*32, 16 + randy*32)))
    pygame.display.update()
    return randx, randy


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        screen.fill("light green")
        draw_grid()
        screen.blit(mole_image, mole_image.get_rect(topleft = (0,0)))
        pygame.display.flip()
        clock.tick(60)
        moleXsqaure = 0
        moleYsqaure = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clickedX, clickedY = pygame.mouse.get_pos()
                    if clickedX//32 == moleXsqaure and clickedY//32 == moleYsqaure:
                        moleXsqaure, moleYsqaure = moveMoleToRand()


    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

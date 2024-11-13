import pygame
import random

def main():
    try:
        pygame.init()
        # Loads mole image and sets initial position
        mole_image = pygame.image.load("mole.png")
        mole_rect = mole_image.get_rect(topleft=(0, 0))
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            # Checks if quitting or clicking
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # If mole clicked, set random position
                    if mole_rect.collidepoint(event.pos):
                        mole_rect = mole_image.get_rect(topleft=(32 * random.randrange(0, 20), 32 * random.randrange(0, 16)))
            screen.fill("light green")
            # Draws lines
            for row in range(1, 17):
                pygame.draw.line(screen, (0, 0, 0), (0, 32 * row), (640, 32 * row))
            for col in range(1, 21):
                pygame.draw.line(screen, (0, 0, 0), (32 * col, 0), (32 * col, 512))
            # Draws mole
            screen.blit(mole_image, mole_rect)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()

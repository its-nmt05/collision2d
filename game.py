import pygame
import sys


class Game:

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR, PARTICLE_COLOR, FPS):
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT

        self.BG_COLOR = BG_COLOR
        self.PARTICLE_COLOR = PARTICLE_COLOR
        self.FPS = FPS

        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Collisions")

    def start(self, engine):
        # Main loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        self.exit()
                        
            # Fill the screen with bg color
            self.screen.fill(self.BG_COLOR)

            engine.update()
            for particle in engine.particles:
                pygame.draw.circle(
                    self.screen, self.PARTICLE_COLOR, particle.pos, engine.radius)

            # Update the display
            pygame.display.update()

            # cap the frame rate
            self.clock.tick(self.FPS)

    def exit(self):
        pygame.quit()
        sys.exit()

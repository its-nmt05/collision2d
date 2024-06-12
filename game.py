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
        pygame.font.init()

        self.font = pygame.font.SysFont("'Comic Sans MS", 30)

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
            self.draw(engine)

            # Update the display
            pygame.display.update()

            # cap the frame rate
            self.clock.tick(self.FPS)

    def draw(self, engine):
        for particle in engine.particles:
            pygame.draw.circle(
                self.screen, self.PARTICLE_COLOR, particle.pos, particle.radius)
            
        # if node.is_leaf():
        #     pygame.draw.rect(self.screen, self.PARTICLE_COLOR,
        #                      (node.min_bound, node.max_bound), 1)
        #     for particle in node.particles:
        #         pygame.draw.circle(
        #             self.screen, self.PARTICLE_COLOR, particle.pos, particle.radius)

        #     text_surface = self.font.render(
        #         str(node.num_particles()), False, self.PARTICLE_COLOR)
        #     self.screen.blit(text_surface, node.min_bound)
        # else:
        #     for child in node.children:
        #         self.draw(child)

    def exit(self):
        pygame.quit()
        sys.exit()

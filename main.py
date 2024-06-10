from game import Game
from engine import Engine

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500
BG_COLOR = (0, 0, 0)
PARTICLE_COLOR = (255, 255, 255)
FPS = 120

NUM_PARTICLES = 50
DIAG_ONE = (0, 0)
DIAG_TWO = (SCREEN_WIDTH, SCREEN_HEIGHT)
ELASTICITY = 1.0
ACCLN = (0, 0.000)

PARTICLE_MASS = 5.0
PARTICLE_RADIUS = 5.0
PARTICLE_MAX_VEL = (-1.0, 1.0)

T_COSNST = 1


def main():
    engine = Engine(NUM_PARTICLES, DIAG_ONE, DIAG_TWO, ELASTICITY, ACCLN,
                    PARTICLE_MASS, PARTICLE_RADIUS, PARTICLE_MAX_VEL, T_COSNST)
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, BG_COLOR, PARTICLE_COLOR, FPS)

    engine.create_particles()
    game.start(engine)


if __name__ == "__main__":
    main()

class Particle(object):

    def __init__(self, mass, radius, pos, vel):
        self.mass = mass
        self.radius = radius
        self.pos = pos
        self.vel = vel

    def update(self, dt):
        self.pos += self.vel * dt
    
import numpy as np


# check collision between particle
def is_collision(p1, p2):
    return np.linalg.norm(p2.pos - p1.pos) <= (p1.radius + p2.radius)


def resolve_collision(p1, p2, elasticity):
    normal = (p2.pos - p1.pos) / np.linalg.norm(p2.pos - p1.pos)
    massEff = (p1.mass * p2.mass) / (p1.mass + p2.mass)
    vImp = np.dot(normal, (p1.vel - p2.vel))

    J = (1 + elasticity) * massEff * vImp
    dv1 = -J / p1.mass * normal
    dv2 = -J / p2.mass * normal

    p1.vel += dv1
    p1.vel += dv2

    overlap = (p1.radius + p2.radius) - np.linalg.norm(p2.pos - p1.pos)
    if overlap > 0:
        d1 = normal * (overlap * (p1.radius / (p1.radius + p2.radius)))
        d2 = normal * (overlap * (p2.radius / (p1.radius + p2.radius)))
        p1.pos += -d1
        p2.pos += -d2


def particle_collide(engine):
    particles = engine.particles
    for i in range(len(particles)):
        for j in range(i + 1,  len(particles) - 1):
            if is_collision(particles[i], particles[j]):
                resolve_collision(
                    particles[i], particles[j], engine.particle_elasticity)


def wall_collide(engine):

    for particle in engine.particles:
        pos = particle.pos
        radius = particle.radius

        if pos[0] - radius < engine.diag_one[0]:
            pos[0] = engine.diag_one[0] + radius
            particle.vel[0] = -particle.vel[0] * engine.wall_elasticity
        if pos[0] + radius > engine.diag_two[0]:
            pos[0] = engine.diag_two[0] - radius
            particle.vel[0] = -particle.vel[0] * engine.wall_elasticity

        if pos[1] - radius < engine.diag_one[1]:
            pos[1] = engine.diag_one[1] + radius
            particle.vel[1] = -particle.vel[1] * engine.wall_elasticity
        if pos[1] + radius > engine.diag_two[1]:
            pos[1] = engine.diag_two[1] - radius
            particle.vel[1] = -particle.vel[1] * engine.wall_elasticity

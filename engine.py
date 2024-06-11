from octree_node import OctreeNode
from particle import Particle
from random import uniform
import numpy as np
from collision import particle_collide, wall_collide, is_collision


class Engine:

    def __init__(self, num_particles, diag_one, diag_two, wall_elasticity, particle_elasticity, accln, mass, radius, max_vel, t_const):
        self.num_particles = num_particles
        self.diag_one = diag_one
        self.diag_two = diag_two

        self.particles = []
        self.wall_elasticity = wall_elasticity
        self.particle_elasticity = particle_elasticity
        self.accln = accln

        self.mass = mass
        self.radius = radius
        self.max_vel = max_vel

        self.t_const = t_const

        self.root_node = OctreeNode(diag_one, diag_two)

    def create_particles(self):
        for _ in range(self.num_particles):
            self.create_particle()

    def create_particle(self):
        p = Particle(self.mass, self.radius,
                     self.gen_pos(), self.gen_vel())

        intersects = False
        for particle in self.particles:
            if is_collision(p, particle):
                intersects = True

        if intersects:
            self.create_particle()
        else:
            self.particles.append(p)
            self.root_node.insert_particle(p)

    def update(self):
        for particle in self.particles:
            particle.vel[0] += self.accln[0] * self.t_const
            particle.vel[1] += self.accln[1] * self.t_const

            particle.update(self.t_const)

        particle_collide(self)

        wall_collide(self)

        self.root_node.update(self.particles)

    def gen_pos(self):
        pos_x = uniform(self.diag_one[0] + self.radius,
                        self.diag_two[0] - self.radius)
        pos_y = uniform(self.diag_one[1] + self.radius,
                        self.diag_two[1] - self.radius)
        return np.array([pos_x, pos_y], dtype=np.float64)

    def gen_vel(self):
        vel_x = uniform(self.max_vel[0], self.max_vel[1])
        vel_y = uniform(self.max_vel[1], self.max_vel[1])
        return np.array([vel_x, vel_y], dtype=np.float64)

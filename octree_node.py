class OctreeNode:
    def __init__(self, min, max):
        self.min_bound = min
        self.max_bound = max
        self.particles = []
        self.children = []

        self.MAX_PARTICLE_PER_NODE = 5

    def subdivide(self):
        center = [(self.min_bound[0] + self.max_bound[0]) /
                  2, (self.min_bound[1] + self.max_bound[1]) / 2]
        for i in range(4):
            newMin = []
            newMax = []
            if i == 0:
                newMin = self.min_bound
                newMax = center
            if i == 1:
                newMin = [self.min_bound[0], center[1]]
                newMax = [center[0], self.max_bound[1]]
            if i == 2:
                newMin = center
                newMax = self.max_bound
            if i == 3:
                newMin = [center[0], self.min_bound[1]]
                newMax = [self.max_bound[0], center[1]]

            self.children.append(OctreeNode(newMin, newMax))

    def combine(self):
        particles = []

        if self.is_leaf():
            particles.extend(self.particles)
        else:
            for child in self.children:
                particles.extend(child.combine())
            self.children.clear()

        self.particles = particles
        return particles

    def insert_particle(self, particle):
        pos = particle.pos
        if (pos[0] < self.min_bound[0] or pos[0] > self.max_bound[0] or
                pos[1] < self.min_bound[1] or pos[1] > self.max_bound[1]):
            return

        if not self.is_leaf():
            for child in self.children:
                child.insert_particle(particle)
            return

        self.particles.append(particle)

        if len(self.particles) > self.MAX_PARTICLE_PER_NODE:
            self.subdivide()
            for particle in self.particles:
                for child in self.children:
                    child.insert_particle(particle)

            self.particles.clear()

        # if self.num_particles() <= self.MAX_PARTICLE_PER_NODE:
        #     self.combine()

    def remove_particle(self, particle):
        if not self.contains(particle):
            return

        if not self.is_leaf():
            for child in self.children:
                child.remove_particle(particle)
            return

        for p in self.particles:
            if p in self.particles:
                self.particles.remove(p)

    def contains(self, particle):
        pos = particle.pos
        radius = particle.radius
        return (pos[0] - radius < self.min_bound[0] or pos[0] + radius > self.max_bound[0]
                or pos[1] - radius < self.min_bound[1] or pos[1] + radius > self.max_bound[1])

    def is_leaf(self):
        return len(self.children) == 0

    def num_particles(self):
        len_particles = 0

        if self.is_leaf():
            len_particles += len(self.particles)
        else:
            for child in self.children:
                len_particles += child.num_particles()

        return len_particles

    def update(self, particles):
        self.combine()
        self.particles.clear()
        for particle in particles:
            self.insert_particle(particle)

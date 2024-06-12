from collections import defaultdict
from collision import is_collision, resolve_collision


class Grid():

    def __init__(self, min, max, cell_size):
        self.min = min
        self.max = max

        self.cell_size = cell_size
        self.grid = defaultdict(list)

    def get_cell_index(self, pos):
        return (pos[0] // self.cell_size, pos[1] // self.cell_size)

    def insert_particle(self, particle):
        index = self.get_cell_index(particle.pos)
        self.grid[index].append(particle)

    def get_neighbours(self, particle):
        cell_index = self.get_cell_index(particle.pos)
        neighbours = []

        for dx in range(-1, 2):
            for dy in range(-1, 2):
                neighbour_index = (
                    cell_index[0] + dx, cell_index[1] + dy)
                if neighbour_index in self.grid:
                    for neighbour in self.grid[neighbour_index]:
                        if neighbour != particle:
                            neighbours.append(neighbour)

        return neighbours

    def update(self, engine):
        self.grid.clear()
        n = 0
        for particle in engine.particles:
            self.insert_particle(particle)
            neighbours = self.get_neighbours(particle)

            for neighbour in neighbours:
                if is_collision(particle, neighbour):
                    resolve_collision(particle, neighbour,
                                      engine.particle_elasticity)

            n += len(neighbours)
        print(n)
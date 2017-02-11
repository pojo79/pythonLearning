import pygame
import random

pygame.init()

game_display = pygame.display.set_mode((600,400))

class particle_system(object):
    def __init__(self):
        self.particles = []
        self.particle_color = (random.uniform(0,255),random.uniform(0,255),random.uniform(0,255))
        self.num_particles = 500
        self.create_particles()
        self.weight = 1

    def create_particles(self):
        for num in range(self.num_particles):
            self.particles.append(particle(self.particle_color, 300,200))
    
    def update_particles(self):
        for particle in self.particles:
            if particle.kill == True:
                self.particles.remove(particle)
            else:
                particle.update(self.weight)

    def draw_particles(self, surface):
        for particle in self.particles:
            pygame.draw.rect(surface, particle.color, particle.rect)

    def has_particles(self):
        if len(self.particles) > 0:
            return True
        else:
            return False

class particle(object):
    def __init__(self, color, start_x, start_y):
        self.born = pygame.time.get_ticks()
        self.lifespan = random.uniform(2,800)
        self.color = (255,0,0)
        #self.color = (random.uniform(0,255),random.uniform(0,255),random.uniform(0,255))
        self.width = 2
        self.height = 2
        self.kill = False
        self.rect = pygame.Rect(start_x,start_y, self.width, self.height)

    def update(self, weight):
        self.rect.x += random.uniform(-1.0, 1.2) * weight
        self.rect.y += random.uniform(-1.0, 1.2) * weight
        #self.rect.x += random.uniform(-5,6)
        #self.rect.y += random.uniform(-5,6)

        if self.lifespan <=  pygame.time.get_ticks() - self.born:
            self.kill = True

system = particle_system()

ticks = pygame.time.get_ticks()
ticks_now = pygame.time.get_ticks()
while system.has_particles():
    game_display.fill((0,0,0))
    system.update_particles()
    system.draw_particles(game_display)
    pygame.display.update()
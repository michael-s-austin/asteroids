import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event 

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20, 50)
        new_velocity = self.velocity * 1.2
        vector_one = new_velocity.rotate(random_angle)
        vector_two = new_velocity.rotate(-random_angle)

        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_one.velocity = vector_one 
                
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two.velocity = vector_two
        

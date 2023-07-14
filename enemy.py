import pygame, math

class Enemy:
    def __init__(self, energy, power, x, y, radius):
        self.energy = energy
        self.power = power
        self.x = x
        self.y = y
        self.radius = radius
    
    def path_find(self, x, y):
        angle_radians = math.atan2(y - self.y, x - self.x)
        x_velocity = math.cos(angle_radians) * 4.3
        y_velocity = math.sin(angle_radians) * 4.3
        
        self.x += x_velocity
        self.y += y_velocity
    
    def draw(self, screen):
        pygame.draw.circle(screen, (150, 0, 0), (self.x, self.y), self.radius)
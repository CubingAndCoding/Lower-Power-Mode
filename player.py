import pygame, time

class Player:
    def __init__(self, energy, power, x, y, radius):
        self.max_energy = energy
        self.energy = energy
        self.power = power
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_boost = 0
        self.speed_start_time = -1
    
    def attack(self):
        if self.energy >= self.power * (3/5):
            self.energy -= self.power * (3/5)
            return self.power
        return 0

    def remove_speed(self):
        if self.speed_start_time > 0 and time.time() - self.speed_start_time > 3:
            self.speed_boost = 0
            self.speed_start_time = -1
    
    def add_speed(self):
        if self.energy > 600 and self.speed_boost == 0:
            self.speed_boost = 2
            self.energy -= 550
            self.speed_start_time = time.time()

    def damage(self, damage):
        self.energy -= damage
    
    def add_energy(self, energy):
        self.energy += energy
    
    def draw(self, screen):
        pygame.draw.circle(screen, (100, 200, 100), (self.x, self.y), self.radius)
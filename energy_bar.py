import pygame

class Energy_Bar:   
    def __init__(self, max_energy, energy, x, y, width, height, color1, color2, color3, color4):
        self.max_energy = max_energy
        self.energy = energy
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color1
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.color4 = color4
    
    def draw(self, screen):
        if self.energy / self.max_energy <= 1:
            self.color = self.color1
        if self.energy / self.max_energy <= .75:
            self.color = self.color2
        if self.energy / self.max_energy <= .5:
            self.color = self.color3
        if self.energy / self.max_energy <= .25:
            self.color = self.color4
        pygame.draw.rect(screen, (0, 0, 0), (self.x - 10, self.y - 10, self.width + 20, self.height + 20))
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width * (self.energy / self.max_energy), self.height))
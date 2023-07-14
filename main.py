import pygame, math, random, sys
from energy_bar import Energy_Bar
from player import Player
from enemy import Enemy
from energy_power_up import Energy_Power_Up
pygame.init()

WIDTH, HEIGHT = 800, 800

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Low Power Mode")
font = pygame.font.Font('font.ttf', 60)
clock = pygame.time.Clock()

boss_bar_width = 400
boss_bar_height = 30
boss_bar_x = WIDTH // 2 - boss_bar_width // 2
boss_bar_y = 20
boss_bar = Energy_Bar(10000, 10000, boss_bar_x, boss_bar_y, boss_bar_width, boss_bar_height, (140, 0, 0), (140, 0, 0), (140, 0, 0), (140, 0, 0))

boss = Enemy(10000, 5, WIDTH // 2, 100, 25)

player_bar_width = 200
player_bar_height = 10
player_bar_x = WIDTH // 2 - player_bar_width // 2
player_boss_y = HEIGHT - 50
player_bar = Energy_Bar(1000, 1000, player_bar_x, player_boss_y, player_bar_width, player_bar_height, (0, 140, 0), (255, 255, 0), (255, 140, 0), (100, 0, 0))

player = Player(1000, 500, WIDTH // 2, HEIGHT - 100, 20)

energy_power_ups = [Energy_Power_Up(200, random.randint(0 + 10, WIDTH - 10), random.randint(0 + 10, HEIGHT - 10), 10) for i in range(10)]

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

game_start = False
game_state = 'running'
action = False
running = True
while running:
    screen.fill(pygame.Color('DarkSlateGray'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if not game_start and (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            game_start = True
        
        if game_start:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and not action:
                    power = player.attack()
                    boss.energy -= power
                    action = True
                if event.button == 3 and not action:
                    player.add_speed()
                    action = True
            if event.type == pygame.MOUSEBUTTONUP:
                action = False
        
    boss_bar.draw(screen)
    player_bar.draw(screen)
    
    player.draw(screen)
    boss.draw(screen)
    
    for power_up in energy_power_ups:
            pygame.draw.circle(screen, (200, 180, 0), (power_up.x, power_up.y), power_up.radius)
            
            if game_start and get_distance(player.x, player.y, power_up.x, power_up.y) < player.radius + power_up.radius:
                player.energy += power_up.energy
                if player.energy > player.max_energy:
                    player.energy = player.max_energy
                energy_power_ups.remove(power_up)
                energy_power_ups.append(Energy_Power_Up(200, random.randint(0 + 10, WIDTH - 10), random.randint(0 + 10, HEIGHT - 10), 10))
    
    if game_start:
        boss.path_find(player.x, player.y)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and keys[pygame.K_a]:
            player.y -= ((4 + player.speed_boost) * math.sqrt(2))/2
            player.x -= ((4 + player.speed_boost) * math.sqrt(2))/2
        elif keys[pygame.K_w] and keys[pygame.K_d]:
            player.y -= ((4 + player.speed_boost) * math.sqrt(2))/2
            player.x += ((4 + player.speed_boost) * math.sqrt(2))/2
        elif keys[pygame.K_s] and keys[pygame.K_d]:
            player.y += ((4 + player.speed_boost) * math.sqrt(2))/2
            player.x += ((4 + player.speed_boost) * math.sqrt(2))/2
        elif keys[pygame.K_s] and keys[pygame.K_a]:
            player.y += ((4 + player.speed_boost) * math.sqrt(2))/2
            player.x -= ((4 + player.speed_boost) * math.sqrt(2))/2
            
        elif keys[pygame.K_w]:
            player.y -= 4 + player.speed_boost
        elif keys[pygame.K_s]:
            player.y += 4 + player.speed_boost
        elif keys[pygame.K_a]:
            player.x -= 4 + player.speed_boost
        elif keys[pygame.K_d]:
            player.x += 4 + player.speed_boost
        
        if player.x - player.radius < 0:
            player.x = player.radius
        if player.x + player.radius > WIDTH:
            player.x = WIDTH - player.radius
        if player.y - player.radius < 0:
            player.y = player.radius
        if player.y + player.radius > HEIGHT:
            player.y = HEIGHT - player.radius
            
        
        if get_distance(player.x, player.y, boss.x, boss.y) < player.radius + boss.radius:
            player.energy -= boss.power
            
        player.remove_speed()
        
        player.energy -= .5
        boss.energy -= 1
        
        if player.energy <= 0:
            player.energy = 0
        
        if player.energy <= 0:
            game_state = "lose"
            boss_bar = Energy_Bar(10000, 10000, boss_bar_x, boss_bar_y, boss_bar_width, boss_bar_height, (140, 0, 0), (140, 0, 0), (140, 0, 0), (140, 0, 0))
            boss = Enemy(10000, 5, WIDTH // 2, 100, 25)

            player_bar = Energy_Bar(1000, 1000, player_bar_x, player_boss_y, player_bar_width, player_bar_height, (0, 140, 0), (255, 255, 0), (255, 140, 0), (100, 0, 0))
            player = Player(1000, 500, WIDTH // 2, HEIGHT - 100, 20)

            energy_power_ups = [Energy_Power_Up(200, random.randint(0 + 10, WIDTH - 10), random.randint(0 + 10, HEIGHT - 10), 10) for i in range(10)]

            game_start = False
            action = False
        elif boss.energy <= 0:
            game_state = "win"
            boss_bar = Energy_Bar(10000, 10000, boss_bar_x, boss_bar_y, boss_bar_width, boss_bar_height, (140, 0, 0), (140, 0, 0), (140, 0, 0), (140, 0, 0))
            boss = Enemy(10000, 5, WIDTH // 2, 100, 25)

            player_bar = Energy_Bar(1000, 1000, player_bar_x, player_boss_y, player_bar_width, player_bar_height, (0, 140, 0), (255, 255, 0), (255, 140, 0), (100, 0, 0))
            player = Player(1000, 500, WIDTH // 2, HEIGHT - 100, 20)

            energy_power_ups = [Energy_Power_Up(200, random.randint(0 + 10, WIDTH - 10), random.randint(0 + 10, HEIGHT - 10), 10) for i in range(10)]

            game_start = False
            action = False            
        
        boss_bar.energy = boss.energy
        player_bar.energy = player.energy
    else:
        if game_state == 'lose':
            text = font.render("You Lose", True, (255, 255, 255))
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
        if game_state == 'win':
            text = font.render("You Win", True, (255, 255, 255))
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
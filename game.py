import pygame
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)
pygame.init()
pygame.font.init()
score = 0
score_increment = 10
isJump = False
jumpCount = 10
class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.image = pygame.image.load("images/cloud.png")
        self.rect = self.image.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, 100),
            )
        )
        self.speed = random.randint(0, 1)
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.image = pygame.image.load("images/turkey.png")
        self.rect = pygame.Rect(100, 450, 100, 300)
        
    
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
    
    def gravity(self):
        self.rect.top += 3.2
        if self.rect.top > 450:
            self.rect.top = 450
        if self.rect.top < 150:
            self.rect.top = 150
    
        
            
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20,10))
        self.image = pygame.image.load("images/Enemy.png")
        self.rect = self.surf.get_rect(
            center = (random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                      random.randint(450, 450),
                      )
        )
        self.speed = random.randint(0, 1)
        
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 750

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
surf = pygame.Surface((100, 100))
surf.fill((255, 127, 127))
rect = surf.get_rect()
ADDENEMY = pygame.USEREVENT + 1
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)
pygame.time.set_timer(ADDENEMY, 500)
player = Player()
clock = pygame.time.Clock()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
clouds = pygame.sprite.Group()


running = True
while running:
    for event in pygame.event.get():
        font = pygame.font.Font(None, 36)
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == ADDCLOUD:
            new_cloud = Cloud()
            clouds.add(new_cloud)
            all_sprites.add(new_cloud)
            
        
    
    screen.fill((255, 127, 127))
    pressed_keys = pygame.key.get_pressed()
    player.gravity()
    player.update(pressed_keys)
    enemies.update()
    clouds.update()
    
    
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill
        running = False
    if not pygame.sprite.spritecollideany(player, enemies):
        score += score_increment 
    #screen.blit(player.image, player.rect)
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))
    screen.blit(score_text, (850, 10))
    pygame.display.flip()
    clock.tick(750)
pygame.quit()
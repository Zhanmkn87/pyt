import pygame
import random

WIDTH = 1000
HEIGHT = 500
FPS = 30

sunx = random.randint(0,1000)
suny = random.randint(0,500)
eaglex = random.randint(0,1000)
eagley = random.randint(0,500)
ornamentx = random.randint(0,1000)
ornamenty = random.randint(0,500)
raysx = random.randint(0,1000)
raysy = random.randint(0,500)

BLUE = (0,0,255)

class sun(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sun.png")
        self.rect = self.image.get_rect()
        self.rect.center = (sunx, suny)
        self.speedx = 0
        self.speedy = 0
    def update(self):
        self.rect.x += self.speedx
        self.speedx = 0
        self.rect.y += self.speedy
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -1
        if keystate[pygame.K_RIGHT]:
            self.speedx = 1
        if keystate[pygame.K_UP]:
            self.speedy = -1
        if keystate[pygame.K_DOWN]:
            self.speedy = 1        
       
class eagle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("eagle.png")
        self.rect = self.image.get_rect()
        self.rect.center = (eaglex, eagley)
        self.speedx = 0
        self.speedy = 0
    def update(self):
        self.rect.x += self.speedx
        self.speedx = 0
        self.rect.y += self.speedy
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_q]:
            self.speedx = -1
        if keystate[pygame.K_r]:
            self.speedx = 1
        if keystate[pygame.K_w]:
            self.speedy = -1
        if keystate[pygame.K_e]:
            self.speedy = 1        
      
class ornament(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ornament.png")
        self.rect = self.image.get_rect()
        self.rect.center = (ornamentx, ornamenty)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.speedx = 0
        self.rect.y += self.speedy
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            self.speedx = -1
        if keystate[pygame.K_f]:
            self.speedx = 1
        if keystate[pygame.K_s]:
            self.speedy = -1
        if keystate[pygame.K_d]:
            self.speedy = 1        
       
class rays(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("rays.png")
        self.rect = self.image.get_rect()
        self.rect.center = (raysx, raysy)
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.rect.x += self.speedx
        self.speedx = 0
        self.rect.y += self.speedy
        self.speedy = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_z]:
            self.speedx = -1
        if keystate[pygame.K_v]:
            self.speedx = 1
        if keystate[pygame.K_x]:
            self.speedy = -1
        if keystate[pygame.K_c]:
            self.speedy = 1        
       

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

sun = sun()
eagle = eagle()
ornament = ornament()
rays = rays()

all_sprites.add(sun)
all_sprites.add(eagle)
all_sprites.add(ornament)
all_sprites.add(rays)


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    screen.fill(BLUE)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()

import pygame
import random

WIDTH = 1000
HEIGHT = 500
FPS = 30

headx = random.randint(0,1000)
heady = random.randint(0,500)
sozx = random.randint(0,1000)
sozy = random.randint(0,500)
astix = random.randint(0,1000)
astiy = random.randint(0,500)
nebox = random.randint(0,1000)
neboy = random.randint(0,500)

WHITE = (0,0,255)

class head(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("head.png")
        self.rect = self.image.get_rect()
        self.rect.center = (headx , heady)
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
       
class soz(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("soz.png")
        self.rect = self.image.get_rect()
        self.rect.center = (sozx, sozy)
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
      
class asti(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("asti.png")
        self.rect = self.image.get_rect()
        self.rect.center = (astix, astiy)
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
       
class nebo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("nebo.png")
        self.rect = self.image.get_rect()
        self.rect.center = (nebox, neboy)
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

head = head()
soz = soz()
asti = asti()
nebo = nebo()

all_sprites.add(head)
all_sprites.add(soz)
all_sprites.add(asti)
all_sprites.add(nebo)


running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    all_sprites.update()
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

pygame.quit()

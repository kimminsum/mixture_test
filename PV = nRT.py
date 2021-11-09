import pygame, sys, random

class Crosshair(pygame.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()
    def shoot(self):
        pygame.sprite.spritecollide(crosshair,target_group,True)
    
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def __init__(self,picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()     
        self.rect.center = [pos_x,pos_y]

    def update(self):
        
        speed = random.randrange(-20,20)
        speed2 = random.randrange(-20,20)
        self.rect.x += speed
        self.rect.y += speed2
        
pygame.init()
clock = pygame.time.Clock()

screen_width = 1600
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
backgound = pygame.image.load('back.png')
pygame.mouse.set_visible(False)

crosshair = Crosshair('cross.png')
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

target_group = pygame.sprite.Group()
for target in range(20):
    new_target = Target('target.png',random.randrange(0,screen_width),random.randrange(0, screen_height))
    target_group.add(new_target)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.shoot()

    pygame.display.flip()
    screen.blit(backgound, (0,0))
    target_group.draw(screen)
    target_group.update()
    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)
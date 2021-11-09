import pygame, random
from pygame.constants import KEYDOWN, K_SPACE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#WINDOW_SETTING
screen_width, screen_height = 1600, 800
screen = pygame.display.set_mode((screen_width, screen_height))
backgound = pygame.image.load('back.png')
a = 5
#DEF_CLASS_CELL
class Cell(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x , pos_y, vx, vy):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()     
        self.rect.center = [pos_x,pos_y]
        self.vx = vx    #x속도
        self.vy = vy    #y속도

    def update(self):
        #세포의 속도를 출력한다.
        font = pygame.font.SysFont(None, 24)
        img = font.render(str(a), True, BLACK)
        self.rect.x %= self.rect.x
        self.rect.y %= self.rect.y
        screen.blit(img, (self.rect.x, self.rect.y)) 

pygame.init()

#CLONE_CLASS_CELL
cell_group = pygame.sprite.Group()
for cell in range(1): #IF_YOU_WANT_TO_CHANGE_CELL's_NUMBER
    new_cell = Cell('target.png' ,screen_width/2 ,screen_height/2 , a, 0)
    cell_group.add(new_cell)

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:     
                pygame.quit()
    a += 1
    # food_group.update()
    cell_group.draw(screen)   
    cell_group.update() 
    pygame.display.flip()
    screen.blit(backgound, (0,0))
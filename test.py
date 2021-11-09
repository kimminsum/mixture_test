import pygame, random
from pygame.constants import KEYDOWN, K_SPACE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#WINDOW_SETTING
screen_width, screen_height = 1600, 800
screen = pygame.display.set_mode((screen_width, screen_height))
backgound = pygame.image.load('back.png')

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
        #x값만 튕기기
        if self.rect.x >= screen_width-30 or+self.rect.x <= 0: #그니까 대충 아래로 내려가면 속도 방향 반대 방향이다
            self.vx = -self.vx
        else:
            self.vx = self.vx
        #Y값만 튕기기
        if self.rect.y >= screen_height-30 or self.rect.y <= 0:
            self.vy = -self.vy
        else:
            self.vy = self.vy
        #실제 좌표 증감값     
        self.rect.x += self.vx
        self.rect.y += self.vy
        #세포의 속도를 출력한다.
        font = pygame.font.SysFont(None, 24)
        img = font.render(str(self.vx)+'  '+str(self.vy), True, BLACK)
        screen.blit(img, (self.rect.x, self.rect.y)) 

class Food(pygame.sprite.Sprite):
    def __init__(self, picture_path, pos_x , pos_y):
        super().__init__()
        self.image = pygame.image.load(picture_path)
        self.rect = self.image.get_rect()     
        self.rect.center = [pos_x,pos_y]

pygame.init()

#CLONE_CLASS_CELL
cell_group = pygame.sprite.Group()
for cell in range(20): #IF_YOU_WANT_TO_CHANGE_CELL's_NUMBER
    new_cell = Cell('target.png' ,random.randrange(30, screen_width-30) ,random.randrange(30, screen_height-30), random.randrange(-10,10), random.randrange(-10,10))
    cell_group.add(new_cell)

food_group = pygame.sprite.Group()
for food in range(20):
    new_food = Food('food.png',random.randrange(30, screen_width-30) ,random.randrange(30, screen_height-30))
    food_group.add(new_food)

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:     
                pygame.quit()
 
    #VISUALIZE
    food_group.draw(screen)
    # food_group.update()
    cell_group.draw(screen)   
    cell_group.update() 
    pygame.display.flip()
    screen.blit(backgound, (0,0))
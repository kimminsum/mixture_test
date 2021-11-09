import pygame, random
from pygame.constants import KEYDOWN, K_SPACE

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#WINDOW_SETTING
screen_width, screen_height = 1600, 800
screen = pygame.display.set_mode((screen_width, screen_height))
backgound = pygame.image.load('back.png')
temperature = 10 + 10000000/(screen_width*screen_height)
fire_temperature = temperature + 273
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
        if self.rect.x >= screen_width-70 or self.rect.x  <= 0: #그니까 대충 아래로 내려가면 속도 방향 반대 방향이다
            self.vx = -self.vx
        else:
            self.vx = self.vx
        #Y값만 튕기기
        if self.rect.y >= screen_height-70 or self.rect.y <= 0:
            self.vy = -self.vy
        else:
            self.vy = self.vy
        #실제 좌표 증감값     
        self.rect.x += self.vx
        self.rect.y += self.vy
        #세포의 속도를 출력한다.
        # font = pygame.font.SysFont(None, 24)
        # img = font.render(str(self.vx)+'  '+str(self.vy), True, BLACK)
        # screen.blit(img, (self.rect.x, self.rect.y)) 

pygame.init()

#CLONE_CLASS_CELL
cell_group = pygame.sprite.Group()
for cell in range(50): #IF_YOU_WANT_TO_CHANGE_CELL's_NUMBER
    new_cell = Cell('cell.png' ,screen_width/2, screen_height/2, random.randrange(-20,20), random.randrange(-20,20))
    cell_group.add(new_cell)

while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:     
                pygame.quit()

    font = pygame.font.SysFont(None, 40)
    img = font.render(str(round(temperature,2))+'°C     '+ str(round(fire_temperature, 2))+'K' , True, BLACK)
    screen.blit(img, (20, 20))

    cell_group.draw(screen)   
    cell_group.update() 
    pygame.display.flip()
    screen.blit(backgound, (0,0))
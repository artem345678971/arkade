import pygame
pygame.init()
window=pygame.display.set_mode((750,750))

window.fill((158, 213, 0))
clock=pygame.time.Clock()
class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=(255, 255, 255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.fill_color = color
        self.rect = pygame.Rect(x, y, width, height)
        
    def set_color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(window, self.fill_color, self.rect)

    def outline(self, frame_color, thickness):
        pygame.draw.rect(window, frame_color, self.rect, thickness)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)
class Picture(Area):
    def __init__(self,filename,x=0,y=0,width=10,height=10):
        Area.__init__(self,x=x,y=y,width=width,height=height,color=None)
        self.image=pygame.image.load(filename)
    def draw(self):
        window.blit(self.image(self.x,self,y))
platfom_x=200
platform_y=300
ball=Picture("pngimg.com - football_PNG52775.png",160,200,50,50)
platform=Picture("pngtree-red-beautiful-platform-image_1155572.jpg",platfom_x,platform_y,100,30)
start_x=5
start_y=5
count=4
monsters=[]
for i in range(10):
    y=start_y+(55*1)
    x=start_x+(25*i)
    for j in range(count):
        enemy=Picture("",x,y,50,50)
        monsters.append(enemy)
        x=x+55
speed_x=3
speed_y=3
game=True
while game:
    ball.fill()
    platform.fill()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                platform.rect_x+3
            if event.fey==pygame.K_LEFT:
                platform.rect_x-3
    for m in monsters:
        m.draw()
        
    platform.draw()
    ball.rect_x+=speed_x
    ball.rect_y+=speed_y
    if ball.rect_y<0:
        speed_y*=-1
    if ball.rect_x<0 or ball.rect_x>750:
        speed_x*=-1
    if ball.rect.collidepoint(platform.rect):
        speed_x*=-1
        speed_y*=-1
    clock.tick(40)
    pygame.display.update()
pygame.quit()
        
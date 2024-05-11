from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x,self.rect.y))

class Player (GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -=self.speed
        if keys[K_DOWN] and self.rect.y <420:
            self.rect.y +=self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >5:
            self.rect.y -=self.speed
        if keys[K_s] and self.rect.y <420:
            self.rect.y +=self.speed

bg =(199, 203, 238)
w=600
h= 500
win =display.set_mode((w,h))
win.fill(bg)
game = True
finish = False
clock = time.Clock()
FPS =60
r1  = Player('wall.jpg',30,200,50,150,4)
r2 = Player('wall.jpg',520,200,50,150,4)
ball = GameSprite('ball.png',200,200,50,50,4)


while game:
    for e in event.get():
        if e.type ==QUIT:
            game =False
    if finish !=True:
        win.fill(bg)
        r1.update_l()
        r2.update_r()

        r1.reset()
        r2.reset()
        ball.reset()
        

    display.update()
    clock.tick(FPS)
    
    
        
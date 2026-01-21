from pygame import *
from random import *
win = display.set_mode((720,480))

clock = time.Clock()

init()

image_gener = font.Font(None, 70)

class Player():
    def __init__(self,x,y,speed):
        self.hitbox = Rect(x,y,30,100)
        self.speed = speed
        self.score = 0
        self.score_img = image_gener.render(str(self.score), True, (0,0,0), (0,0,0))
        


    def move(self):
        key_list = key.get_pressed()
        if key_list[K_w]:
            self.hitbox.y -= self.speed
        if key_list[K_s]:
            self.hitbox.y += self.speed
        if self.hitbox.bottom > 480:
            self.hitbox.bottom = 480
        if self.hitbox.top < 0:
            self.hitbox.top = 0
        if self.hitbox.colliderect(ball.hitbox):
            ball.speed_x = ball.speed
            ball.randomx = randint(1,3)
            ball.randomy = randint(1,3)

    def autopilot(self):
        if ball.hitbox.centery < self.hitbox.centery:
            self.hitbox.y -= self.speed
        else:
            self.hitbox.y += self.speed
                
        if self.hitbox.colliderect(ball.hitbox):
            ball.speed_x = -ball.speed
            ball.randomx = randint(1,3)
            ball.randomy = randint(1,3)

class Ball():
    def __init__(self,x,y,speed):
        self.hitbox = Rect(x,y,34,34)
        self.speed = speed
        self.speed_x = speed
        self.speed_y = speed
        self.randomx = 1
        self.randomy = 1
    def move(self):
        self.hitbox.x += self.speed_x * self.randomx
        self.hitbox.y += self.speed_y * self.randomx
        if self.hitbox.top < 0:
            self.speed_y = self.speed
        if self.hitbox.bottom > 480:
            self.speed_y = -self.speed
            
        if self.hitbox.left < 0:
            self.speed_x = self.speed
            self.hitbox.center = (360, 240)
            player2.score += 1
            player2.score_img = image_gener.render(str(player2.score), True, (0,0,0), (90,35,40))
            time.wait(1000)
            self.randomx = 1
            self.randomy = 1

        if self.hitbox.right > 720:
            self.speed_x = -self.speed
            self.hitbox.center = (360, 240)
            player1.score += 1
            player1.score_img = image_gener.render(str(player1.score), True, (0,0,0), (90,159,190))
            time.wait(1000)
            self.randomx = 1
            self.randomy = 1

player1 = Player(50,240,7)
player2 = Player(620,240,4)
ball = Ball(360,240,4)

while True:
    win.fill((0,0,0))
    event_list = event.get()
    for e in event_list:
        if e.type == QUIT:
            exit()
    player1.move()
    draw.rect(win,(107,120,220),player1.hitbox)
    player2.autopilot()
    draw.rect(win,(100,33,55),player2.hitbox)
    ball.move()
    draw.rect(win,(55,160,55),ball.hitbox)
    win.blit(player1.score_img, (20, 20))

    win.blit(player2.score_img, (630, 20))
    display.update()
    clock.tick(60)
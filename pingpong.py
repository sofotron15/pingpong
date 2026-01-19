from pygame import *

win = display.set_mode((720,480))

clock = time.Clock()

class Player():
    def __init__(self,x,y,speed):
        self.hitbox = Rect(x,y,30,100)
        self.speed = speed

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

    def autopilot(self):
        if ball.hitbox.centery < self.hitbox.centery:
            self.hitbox.y -= self.speed
        else:
            self.hitbox.y += self.speed
                
        if self.hitbox.colliderect(ball.hitbox):
            ball.speed_x = -ball.speed


class Ball():
    def __init__(self,x,y,speed):
        self.hitbox = Rect(x,y,34,34)
        self.speed = speed
        self.speed_x = speed
        self.speed_y = speed
    def move(self):
        self.hitbox.x += self.speed_x
        self.hitbox.y += self.speed_y
        if self.hitbox.top < 0:
            self.speed_y = self.speed
        if self.hitbox.bottom > 480:
            self.speed_y = -self.speed
        if self.hitbox.left < 0:
            self.speed_x = self.speed
            self.hitbox.center = (360, 240)
            time.wait(1000)
        if self.hitbox.right > 720:
            self.speed_x = -self.speed
            self.hitbox.center = (360, 240)
            time.wait(1000)


player1 = Player(50,240,5)
player2 = Player(620,240,1)
ball = Ball(360,240,2)

while True:
    win.fill((255,255,255))
    event_list = event.get()
    for e in event_list:
        if e.type == QUIT:
            exit()
    player1.move()
    draw.rect(win,(255,0,0),player1.hitbox)
    player2.autopilot()
    draw.rect(win,(255,0,0),player2.hitbox)
    ball.move()
    draw.rect(win,(255,0,0),ball.hitbox)
    display.update()
    clock.tick(200)
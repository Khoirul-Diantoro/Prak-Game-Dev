# Part A
import pygame, sys
from pygame.locals import *

WIDTH, HEIGHT = 400, 400
TITLE = "smooth movement"

class Player :
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.rect = pygame.Rect(self.x, self.y, 32, 32)
        self.color = (250, 120, 60)
        self.velx = 0
        self.vely = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 4
# Akhir Part A

# Part B
    def update(self):
            self.velX = 0
            self.velY = 0
            if self.left_pressed and not self.right_pressed and self.x > 0 :
                self.velX = -self.speed
            if self.right_pressed and not self.left_pressed and self.x < 365 : 
                self.velX = self.speed
            if self.up_pressed and not self.down_pressed and self.y > 0 :
                self.velY = -self.speed
            if self.down_pressed and not self.up_pressed and self.y < 365 :
                self.velY = self.speed        
            
            self.x += self.velX
            self.y += self.velY
            
            self.rect = pygame.Rect(int(self.x), int(self.y), 32, 32)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
# Akhir Part B

#Part C
pygame.init()
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

font_color = (0, 150, 250)
font = pygame.font.Font(None, 48)
text = font.render("Khoirul Diantoro", True, font_color)

running = True

# Akhir Part C


# Part D
player = Player(WIDTH/2, HEIGHT/2)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.left_pressed = True
            if event.key == pygame.K_RIGHT:
                player.right_pressed = True
            if event.key == pygame.K_UP:
                player.up_pressed =True
            if event.key == pygame.K_DOWN:
                player.down_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.left_pressed = False
            if event.key == pygame.K_RIGHT:
                player.right_pressed = False
            if event.key == pygame.K_UP:
                player.up_pressed = False
            if event.key == pygame.K_DOWN:
                player.down_pressed = False
 # Akhir Part D           

 # Part E   
    win.fill((255, 255, 255))
    win.blit(text, (70,20))
    player.draw(win)

    player.update()
    pygame.display.flip()
    clock.tick(120)

# Akhir Part E

    


import pygame
import random
import math
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((1820,915))
pygame.display.set_caption('Shapes')
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
x=100
y=100
side1x=0
side1y=100
side2x=1795
side2y=100
ly=0
ry=0
player1=0
player2=0
SPEED_MIN = 1
SPEED_MAX = 5
ANGLE_RANGE = 45
BASE_SPEED = 2.0
SPEED_INCREMENT = 0.4
current_speed = BASE_SPEED


pygame.display.update()
xchange=random.randint(1,5)
ychange=random.randint(1,5)
while True:
   pygame.display.update()
   for event in pygame.event.get():
       if event.type==QUIT:
           pygame.quit()
           exit()
       elif event.type==KEYDOWN:
           if event.key==K_UP:
               ly=-10
               print('UP Key Pressed')
           elif event.key==K_DOWN:
               ly=10
               print('DOWN Key Pressed')
           elif event.key==K_w:
               ry=-10
               print('W Key Pressed')
           elif event.key==K_s:
               ry=10
               print('S Key Pressed')
       elif event.type==KEYUP:
           if event.key==K_UP:
               ly=0
               print('UP Key Released')
           elif event.key==K_DOWN:
               ly=0
               print('DOWN Key Released')
           elif event.key==K_w:
               ry=0
               print('W Key Released')
           elif event.key==K_s:
               ry=0
               print('S Key Released')

   
   screen.fill(black)

   # Build rects for collision (ball uses radius 50)
   ball_rect = pygame.Rect(int(x - 50), int(y - 50), 100, 100)
   left_paddle = pygame.Rect(side1x, side1y, 25, 200)
   right_paddle = pygame.Rect(side2x, side2y, 25, 200)

   if ball_rect.colliderect(right_paddle):
       current_speed = min(current_speed + SPEED_INCREMENT, SPEED_MAX)
       angle = random.uniform(-ANGLE_RANGE, ANGLE_RANGE)
       xchange = -abs(current_speed * math.cos(math.radians(angle)))
       ychange = current_speed * math.sin(math.radians(angle))

   if ball_rect.colliderect(left_paddle):
       current_speed = min(current_speed + SPEED_INCREMENT, SPEED_MAX)
       angle = random.uniform(-ANGLE_RANGE, ANGLE_RANGE)
       xchange = abs(current_speed * math.cos(math.radians(angle)))
       ychange = current_speed * math.sin(math.radians(angle))

   ball=pygame.draw.circle(screen,blue,(int(x),int(y)),50,50)

   
   
      
   side1y+=ry
   side2y+=ly
   x=x+xchange
   y=y+ychange
   if y>=865:
       ychange=-ychange
       
   if y<=50:
       ychange=-ychange
       
   if side1y < 0:
       side1y=0
   if side1y > 715:
       side1y=715
   if side2y < 0:
       side2y=0
   if side2y > 715:
       side2y=715


   if player1==20:
       def show_text3(msg,x,y,color):
           fontobj=pygame.font.SysFont('freesans',200)
           msgobj=fontobj.render(msg,False,color)
           screen.blit(msgobj,(370,300))
       show_text3('player 1 Wins',10,10,green)


   if player2==20:
       def show_text4(msg,x,y,color):
           fontobj=pygame.font.SysFont('freesans',200)
           msgobj=fontobj.render(msg,False,color)
           screen.blit(msgobj,(370,300))
       show_text4('player 2 Wins',10,10,red)
        
       
   if x > 1820:
       player1 = player1 + 1
       print(player1)
       if player1 == 21:
           print('player1 wins')
           exit()
       x=910
       y=450
       current_speed = BASE_SPEED
       xchange = -abs(current_speed)
       ychange = 0

   if x < 0:
       player2 = player2 + 1
       print(player2)
       if player2 == 21:
           print('player2 wins')
           exit()
       x=910
       y=450
       current_speed = BASE_SPEED
       xchange = abs(current_speed)
       ychange = 0





   if x in range(side2x,side2x+25) and y in range (side2y,side2y+200):
       angle = random.uniform(-ANGLE_RANGE, ANGLE_RANGE)
       speed = random.uniform(SPEED_MIN, SPEED_MAX)
       xchange = -abs(speed * math.cos(math.radians(angle)))
       ychange = speed * math.sin(math.radians(angle))

   if x in range(side1x,side1x+25) and y in range (side1y,side1y+200):
       angle = random.uniform(-ANGLE_RANGE, ANGLE_RANGE)
       speed = random.uniform(SPEED_MIN, SPEED_MAX)
       xchange = abs(speed * math.cos(math.radians(angle)))
       ychange = speed * math.sin(math.radians(angle))

   def show_text(msg,x,y,color):
            fontobj=pygame.font.SysFont('freesans',75)
            msgobj=fontobj.render(msg,False,color)
            screen.blit(msgobj,(250,10))

   show_text(('player 1: {}'.format(player1)),10,10,white)


   def show_text2(msg,x,y,color):
            fontobj=pygame.font.SysFont('freesans',75)
            msgobj=fontobj.render(msg,False,color)
            screen.blit(msgobj,(1000,10))
   
   show_text2(('player 2: {}'.format(player2)),10,10,white)

   
   pygame.draw.rect(screen,green,(side1x,side1y,25,200))
   pygame.draw.rect(screen,red,(side2x,side2y,25,200))
   pygame.display.update()

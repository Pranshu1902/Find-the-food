# Made by Pranshu Aggarwal

# Find the food game

import pygame
import random


# creating the list of random values for the food
a = []
b = []

for i in range(25,785,10):
    a.append(i)
for i in range(75,585,10):
    b.append(i)

# initialization

pygame.init()

dis = pygame.display.set_mode((800,600))

pygame.display.set_caption("Find The Food")

white = [255,255,255]

green = (0, 255, 0) 
blue = (0, 0, 128)


# text

font = pygame.font.Font('freesansbold.ttf', 20) 
text = font.render('Welcome! Use arrows to move. If you go out of the screen then you lose', True, green, blue) 

text2 = font.render('Press Q to quit and R to restart', True, green, blue)


textRect = text.get_rect()  
textRect.center = (350, 15)

textrect = text2.get_rect()
textrect.center = (150,50)



dis.fill(white)

x = 100
y = 100

# player

pygame.draw.rect(dis, [0, 255, 0], [x,y,10,10])

# food
pygame.draw.circle(dis, [255,0,0],[500,500], 5, 0)


pygame.display.update()

score = 0

pxx = 0
pyy = 0

px = 205
py = 205


# main gane loop


run = True





def mainloop(run, x, y, px, py):
    global score
    while run:
        pygame.time.delay(100)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        if keys[pygame.K_DOWN]:
            y+=10
        elif keys[pygame.K_UP] and y>70:
            y-=10
        elif keys[pygame.K_LEFT]:
            x-=10
        elif keys[pygame.K_RIGHT]:
            x+=10
        x1 = x+5 # x coordinate of center of rectangle
        y1 = y+5 # y coordinate of center of rectangle
        dis.fill(white)

    
        # stop the game if the player goes out of screen
        if x>790 or x<0 or y>590 or y<0 or keys[pygame.K_q]:
            run = False

        # restart after pressing "R"
        if keys[pygame.K_r]:
            score = 0
            mainloop(True, 100,100,205,205)
    

    
    # for the first default position of the food

        if x1 == 205 and y1 == 205:
            px = random.choice(a)
            py = random.choice(b)
            dis.fill(white)
            score+=1
            x+=10

        
    # general for all positions of the food

        if x1 == px and y1 == py:
            px = random.choice(a)
            py = random.choice(b)
            dis.fill(white)
            score+=1
            x+=10

        # displaying the score
        value = font.render("Your Score: " + str(score), True, green, blue)
        dis.blit(value, [650, 35])


    
        pygame.draw.circle(dis, [255,0,0],[px,py], 5, 0)
        pygame.draw.rect(dis, [0, 255, 0], [x,y, 10, 10])
        dis.blit(text, textRect)
        dis.blit(text2, textrect)
        pygame.display.update()



    pygame.quit()


mainloop(True, 100,100,205,205)

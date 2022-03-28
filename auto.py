import pygame
import time
import random
import queue


pygame.init()
clock = pygame.time.Clock()

w = 500
h = 500

screen = pygame.display.set_mode((500 , 500))

class snake:
    def __init__(self  , x  , y):    
        self.x = x 
        self.y = y 
x = 10
y = 0

x_direction = 1
y_direction = 1

head = snake(0 , 0)

snakeList = []

snakeList.append(head)
snakeList.append(snake(snakeList[0].x , snakeList[0].y))


# food_x , food_y = 100 , 100
color = (255 , 0 , 0)

done = False
score = 0

move = None
EAT = True

def food():
    food_x , food_y = round(random.randint(0, 49)*10) , round(random.randint(0, 49)*10)

    for i in snakeList:
        if food_x == i.x and food_y == i.y:
            food()
    else:
        return food_x , food_y

def go(head , food_x , food_y):

    # head.y is row and head.x is col  
    # food_y is row and food_x is col

#y is row 
    if head.x == food_x:
        if head.y < food_y:
            return 'DOWN'
        
        elif head.y > food_y:
            return 'UP'
# x is col
    if head.x < food_x:
        return 'RIGHT'

    elif head.x > food_x:
        return 'LEFT'
        
while not done:

    for event in pygame.event.get():            
        if event.type == pygame.QUIT:      
            done = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True
    
    if EAT:
        food_x , food_y = food()
        EAT = False


    move = go(head , food_x , food_y)
    
    if move == 'LEFT':
        x_direction = -1
        x = 10
        y = 0
    
    if move == 'RIGHT':
        x_direction = 1
        x = 10
        y = 0

    if move == 'UP':
        y_direction = -1
        x = 0
        y = 10
                
    if move == 'DOWN':
        y = 10
        x = 0
        y_direction = 1
    
    screen.fill(0)

    head.x += x * x_direction
    head.y += y * y_direction
    

    pygame.draw.rect(screen , (255 , 255 , 255) , (food_x , food_y , 10 , 10))
    

    if head.x == food_x and head.y == food_y:
        color = (0 , 0 , 255)
        snakeList.append(snake(snakeList[0].x , snakeList[0].y))
        score += 1
        print("EAT" , score)
        EAT = True

    for i in range(len(snakeList)-1 , -1 , -1):
        
        
        if i == 0:
            pygame.draw.rect(screen , (255, 0 , 0) , (head.x , head.y , 10 , 10))
            # pygame.draw.rect(screen , color , (head.x , head.y , 10 , 10))

        else:
            color = (0 , 255 , 0)
            snakeList[i].x = snakeList[i-1].x
            snakeList[i].y = snakeList[i-1].y
            current_x , current_y = snakeList[i].x , snakeList[i].y
            pygame.draw.rect(screen , color , (current_x , current_y, 10 , 10))


    pygame.display.update()
    # clock.tick(90)
    # clock.tick()
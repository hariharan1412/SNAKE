import secrets
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


food_x , food_y = 100 , 100
color = (255 , 0 , 0)

done = False
score = 0
# done = True
while not done:

    for event in pygame.event.get():            
        if event.type == pygame.QUIT:      
            done = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True

            if event.key == pygame.K_LEFT:
                x_direction = -1
                x = 10
                y = 0

                
            if event.key == pygame.K_RIGHT:
                x_direction = 1
                x = 10
                y = 0

            if event.key == pygame.K_UP:
                y_direction = -1
                x = 0
                y = 10
                
            if event.key == pygame.K_DOWN:
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

    for i in range(len(snakeList)-1 , -1 , -1):
        
        
        if i == 0:
            pygame.draw.rect(screen , color , (head.x , head.y , 10 , 10))

        else:
            color = (0 , 255 , 0)
            snakeList[i].x = snakeList[i-1].x
            snakeList[i].y = snakeList[i-1].y
            current_x , current_y = snakeList[i].x , snakeList[i].y
            pygame.draw.rect(screen , color , (current_x , current_y, 10 , 10))


        # print(len(snakeList) , i)
        # print(snakeList[i].x , snakeList[i].y)

    # print() 

    pygame.display.update()
    clock.tick(10)
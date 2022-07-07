import pygame, sys, random
from pygame.math import Vector2
from settings import *


screen = pygame.display.set_mode(DISPLAY)

class Apple():
    def __init__(self):
        self.x , self.y = random.randint(0 , CELL_NUMBER - 1) , random.randint(0 , CELL_NUMBER - 1)
        self.pos = Vector2(self.x , self.y)
        
    def draw_apple(self):
        apple_rect = pygame.Rect(int(self.pos.x * CELL_SIZE + 10) , int(self.pos.y * CELL_SIZE + 10) , CELL_SIZE - 20, CELL_SIZE - 20)
        pygame.draw.rect(screen , APPLE_COLOR , apple_rect)


class Snake():
    def __init__(self):
        self.body = [Vector2(5,10), Vector2(6,10)]
        self.direction = Vector2(1,0)

    def draw_snake(self):
        for position in self.body:
            x_pos = int(position.x * CELL_SIZE)
            y_pos = int(position.y * CELL_SIZE)
            snake_rect = pygame.Rect(x_pos , y_pos , CELL_SIZE -1, CELL_SIZE -1)
            pygame.draw.rect(screen , SNAKE_COLOR , snake_rect)

    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0 , body_copy[0] + self.direction)
        self.body = body_copy[:]

    def snake_keys(self, event):
        if event.key == pygame.K_UP and self.direction != Vector2(0,1):
            self.direction = Vector2(0,-1)
        if event.key == pygame.K_DOWN and self.direction != Vector2(0,-1):
            self.direction = Vector2(0,1)
        if event.key == pygame.K_LEFT and self.direction != Vector2(1,0):
            self.direction = Vector2(-1,0)
        if event.key == pygame.K_RIGHT and self.direction != Vector2(-1,0):
            self.direction = Vector2(1,0)
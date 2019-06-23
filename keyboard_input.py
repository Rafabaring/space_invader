import time


import pygame
from pygame.locals import *

pygame.init()

def user_input():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_LEFT:
                 move = 'left'
                 return move
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_RIGHT:
                 move = 'right'
                 return move
        if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_SPACE:
                 move = 'space'
                 return move


while True:

   print ("doing a function")
   time.sleep(0.3)
   move = user_input()
   print(move)
   # print(user_input)

   # for event in pygame.event.get():
   #     if event.type == pygame.KEYDOWN:
   #          if event.key == pygame.K_LEFT:
   #              move = 'left'
   #              print(move)
   #     if event.type == pygame.KEYDOWN:
   #          if event.key == pygame.K_RIGHT:
   #              move = 'right'
   #              print(move)
   #     if event.type == pygame.KEYDOWN:
   #          if event.key == pygame.K_SPACE:
   #              move = 'space'
   #              print(move)

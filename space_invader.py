# import keyboard
import time
import random

# Importing pygame for keyboard input handling
import pygame
from pygame.locals import *
pygame.init()


import os
os.system('clear')


class Ship():
    def __init__(self):
        self.ship = '_|_'
        self.ship_x_axis = 4 # ship start in the center
        self.ship_y_axis = 9 # last row of the matrix

class Laser(Ship):
    def __init__(self):
        Ship.__init__(self)
        self.laser = " * "

    def fire(self, ship_x_axis, key_input):
        if key_input == 'up': # "\033[A"
            shot_range = self.ship_y_axis - 1
            while shot_range != 0:
                # convert the cell in a laser " * "
                self.cells[shot_range][ship_x_axis] = self.laser
                self.refresh_screen()
                time.sleep(0.07)

                # clear the cell that had a laser
                self.cells[shot_range][ship_x_axis] = "   "
                self.refresh_screen()
                # time.sleep(0.1)
                shot_range -= 1

class Enemy(Laser):
    def __init__(self):
        Laser.__init__(self)
        self.enemy = '<*>'
        self.enemy_x_axis = 4
        self.enemy_y_axis = 5
        self.counter_enemy = 0


    def update_enemy_position(self, enemy_x_axis, enemy_y_axis):

        self.cells[enemy_x_axis][enemy_y_axis] = self.enemy
        self.refresh_screen()

        # A combination of counter_enemy and time.sleep will determine how fast the ship move - how challenging the game will be
        if self.counter_enemy <= 7:
            self.enemy_x_axis = enemy_x_axis
            self.enemy_y_axis = enemy_y_axis
            self.counter_enemy += 1
        else:
            temp_x_position = random.randint(1,3)
            temp_y_position = random.randint(1,9)
            self.enemy_x_axis = temp_x_position
            self.enemy_y_axis = temp_y_position
            self.counter_enemy = 0

        time.sleep(0.05)
        self.cells[enemy_x_axis][enemy_y_axis] = '   '


class Universe(Enemy):
    def __init__(self):# 0      1      2      3      4      5      6      7      8      9
        Enemy.__init__(self)
        self.cells = [["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]   # 0
                     ,["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]   # 1
                     ,["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]   # 2
                     ,["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]   # 3
                     ,["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]   # 4
                     ,["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]   # 5
                     ,["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]   # 6
                     ,["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]   # 7
                     ,["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]   # 8
                     ,["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]]  # 9

    def display(self):
        print("%s  %s  %s  %s  %s  %s  %s  %s  %s  %s" %(self.cells[0][0], self.cells[0][1], self.cells[0][2], self.cells[0][3], self.cells[0][4], self.cells[0][5], self.cells[0][6], self.cells[0][7], self.cells[0][8], self.cells[0][9]))
        print("%s  %s  %s  %s  %s  %s  %s  %s  %s  %s" %(self.cells[1][0], self.cells[1][1], self.cells[1][2], self.cells[1][3], self.cells[1][4], self.cells[1][5], self.cells[1][6], self.cells[1][7], self.cells[1][8], self.cells[1][9]))
        print("%s  %s  %s  %s  %s  %s  %s  %s  %s  %s" %(self.cells[2][0], self.cells[2][1], self.cells[2][2], self.cells[2][3], self.cells[2][4], self.cells[2][5], self.cells[2][6], self.cells[2][7], self.cells[2][8], self.cells[2][9]))
        print("%s  %s  %s  %s  %s  %s  %s  %s  %s  %s" %(self.cells[3][0], self.cells[3][1], self.cells[3][2], self.cells[3][3], self.cells[3][4], self.cells[3][5], self.cells[3][6], self.cells[3][7], self.cells[3][8], self.cells[3][9]))
        print("%s  %s  %s  %s  %s  %s  %s  %s  %s  %s" %(self.cells[4][0], self.cells[4][1], self.cells[4][2], self.cells[4][3], self.cells[4][4], self.cells[4][5], self.cells[4][6], self.cells[4][7], self.cells[4][8], self.cells[4][9]))
        print("%s  %s  %s  %s  %s  %s  %s  %s  %s  %s" %(self.cells[5][0], self.cells[5][1], self.cells[5][2], self.cells[5][3], self.cells[5][4], self.cells[5][5], self.cells[5][6], self.cells[5][7], self.cells[5][8], self.cells[5][9]))
        print("%s  %s  %s  %s  %s  %s  %s  %s  %s  %s" %(self.cells[6][0], self.cells[6][1], self.cells[6][2], self.cells[6][3], self.cells[6][4], self.cells[6][5], self.cells[6][6], self.cells[6][7], self.cells[6][8], self.cells[6][9]))
        print("%s  %s  %s  %s  %s  %s  %s  %s  %s  %s" %(self.cells[7][0], self.cells[7][1], self.cells[7][2], self.cells[7][3], self.cells[7][4], self.cells[7][5], self.cells[7][6], self.cells[7][7], self.cells[7][8], self.cells[7][9]))
        print("%s  %s  %s  %s  %s  %s  %s  %s  %s  %s" %(self.cells[8][0], self.cells[8][1], self.cells[8][2], self.cells[8][3], self.cells[8][4], self.cells[8][5], self.cells[8][6], self.cells[8][7], self.cells[8][8], self.cells[8][9]))
        print("%s  %s  %s  %s  %s  %s  %s  %s  %s  %s" %(self.cells[9][0], self.cells[9][1], self.cells[9][2], self.cells[9][3], self.cells[9][4], self.cells[9][5], self.cells[9][6], self.cells[9][7], self.cells[9][8], self.cells[9][9]))

    def refresh_screen(self):
        os.system('clear')
        print('ship_x_axis --> ', self.ship_x_axis)
        print('ship_y_axis --> ', self.ship_y_axis)
        self.display()

    # Arrows representation on keyboard
    # up - "\033[A"
    # down - "\033[B"
    # left - "\033[D"
    # right - "\033[C"

    def update_ship_x_axis_position(self, ship_x_axis, key_input):
        if key_input == 'left':
            self.ship_x_axis -= 1
            self.refresh_screen()
        elif key_input == 'right':
            self.ship_x_axis += 1
            self.refresh_screen()
        return self.ship_x_axis

    def update_ship_position(self, ship_x_axis):
        # Cleaning all possition the ship was prior
        for i in range(0, len(self.cells[9])):
            self.cells[9][i] = "   "
        # Assigning new ship_ship_x_axis_position
        self.cells[9][self.ship_x_axis] = self.ship



## ------------------------------------------------------------------------------------

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
             if event.key == pygame.K_UP:
                 move = 'up'
                 return move

universe = Universe()

counter = 0
while True:
    universe.refresh_screen()
    time.sleep(0.03)
    move = user_input()

    # counter += 1
    # print(counter)

    # Move ship
    universe.ship_x_axis = universe.update_ship_x_axis_position(universe.ship_x_axis, move)
    universe.update_ship_position(universe.ship_x_axis)

    # Fire
    universe.fire(universe.ship_x_axis, move)

    universe.update_enemy_position(universe.enemy_x_axis, universe.enemy_y_axis)

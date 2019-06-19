import keyboard
import time
# Controlling keyboard
from pynput.keyboard import Key, Controller
keyboard = Controller()

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
        if key_input == "\033[A":
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
        self.enemy_x_axis = 0
        self.enemy_y_axis = 5

    def update_enemy_position(self, enemy_x_axis, enemy_y_axis):
        self.cells[enemy_x_axis][enemy_y_axis] = self.enemy


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
    def keyboard_input(self):
        key_input = input()
        return key_input

    def update_ship_ship_x_axis_position(self, ship_x_axis, key_input):
        if key_input == "\033[D":
            self.ship_x_axis -= 1
        elif key_input == "\033[C":
            self.ship_x_axis += 1
        return self.ship_x_axis

    def update_ship_position(self, ship_x_axis):
        # Cleaning all possition the ship was prior
        for i in range(0, len(self.cells[9])):
            self.cells[9][i] = "   "
        # Assigning new ship_ship_x_axis_position
        self.cells[9][self.ship_x_axis] = self.ship




## ------------------------------------------------------------------------------------


universe = Universe()


while True:
    universe.refresh_screen()

    # Player command
    key_input = universe.keyboard_input()

    # Move ship
    universe.ship_x_axis = universe.update_ship_ship_x_axis_position(universe.ship_x_axis, key_input)
    universe.update_ship_position(universe.ship_x_axis)

    # Fire
    universe.fire(universe.ship_x_axis, key_input)

    universe.update_enemy_position(universe.enemy_x_axis, universe.enemy_y_axis)

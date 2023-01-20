import math
import pygame
import random
import tkinter as tk
from tkinter import messagebox


class cube(object):
    rows = 0
    w = 0

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass


class snake(object):
    def __init__(self, color, pos):
        pass

    def move(self):
        pass

    def reset(self, pos):
        pass

    def addCube(self):
        pass

    def draw(self, surface):
        pass


def drawGrid(w, rows, surface):
    sizeBtwn = w // rows    #	Floor division(nearest whole number)

    x = 0
    y = 0

    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255,255,255), (x,0), (x,w))  #to draw the white lines (surface,color,start_pos,end_pos)
        pygame.draw.line(surface, (255,255,255), (0,y), (w,y))


def reDrawWindow(surface):
    #first thing to to is we need to update the display
    global rows, width  #global keyword is used for to modify var inside any fun.
    surface.fill((0,0,0))
    drawGrid(width,rows,surface)   #draw the grid
    pygame.display.update()


def randomSnake(rows, items):
    pass


def message_box(subject, content):
    pass


def main():
    global width, rows
    width = 500
    rows = 20   # devide width evenly otherwise weird looking rows
    win = pygame.display.set_mode((width, width))
    s = snake((255, 0, 0), (10, 10))    #Object

    clock = pygame.time.Clock() #Object of the clock module of pygame

    flag = True
    while flag:
        pygame.time.delay(50)   #50 milisecond delay so program doesn't run to fast
        clock.tick(10)          #make sure that our game doesn't run more than 10 frames per sec. 

        reDrawWindow(win)

main()

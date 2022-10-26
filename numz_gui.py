# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 10:04:39 2022

@author: james
"""
#Created following https://www.geeksforgeeks.org/tic-tac-toe-gui-in-python-using-pygame/
import numz
import pygame as pg
import sys
import time
from pygame.locals import *
import os

#define board size
width = 400
height = 400
white = (255,255,255)
line_colour = (0,0,0)
board = [[None]*3, [None]*3, [None]*3]

#initialize window
pg.init()
#set fps
fps = 30
#set up a clock to track time

CLOCK = pg.time.Clock()

screen = pg.display.set_mode((width, height+100), 0, 32)

pg.display.set_caption("Play Numz")
images = []
image_names = []
image_dir = 'images'
for image in os.listdir(image_dir):
    image_names.append(image)
    pg_image = pg.image.load(os.path.join(image_dir, image))

    scaled_image = pg.transform.scale(pg_image, (80,80))
    images.append(scaled_image)
    
    
initiating_window = pg.image.load('numz_cover.png')
initiating_window = pg.transform.scale(initiating_window, (width, height + 100))
def game_initiating_window():
    screen.blit(initiating_window, (0, 0))
    pg.display.update()
    time.sleep(10)
    screen.fill(white)
    pg.draw.line(screen , line_colour, (width/3, 0), (width/3, height), 7)
    pg.draw.line(screen, line_colour, (2*width/3, 0), (2*width/3, height), 7)
    pg.draw.line(screen, line_colour, (0, height/3), (width,height/3),7)
    pg.draw.line(screen, line_colour, (0,2*height/3), (width,2*height/3), 7)
    
# game_initiating_window()

# def draw_piece():
    
game_board = numz.numz_game()

def get_image(piece):
    piece = piece + '.png'
    index = image_names.index(piece)
    return images[index]
    


# while(True):
#     for event in pg.event.get():

#         if event.type == QUIT:
#             pg.quit()
#             sys.exit()
#         # elif event.type == MOUSEBUTTONDOWN:
#         #     print(event)
#         #     user_click()
#         #     if(winner or draw):
#         #         reset_game()
#     pg.display.update()
#     CLOCK.tick(fps)

    



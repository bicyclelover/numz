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
import copy

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
computer_turn = False

CLOCK = pg.time.Clock()

screen = pg.display.set_mode((width, height+100), 0, 32)

pg.display.set_caption("Play Numz")
images = []
image_names = []
image_dir = 'images'
blank = pg.image.load('blank.png')
blank = pg.transform.scale(blank, (80,80))
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
    time.sleep(3)
    screen.fill(white)
    pg.draw.line(screen , line_colour, (width/3, 0), (width/3, height), 7)
    pg.draw.line(screen, line_colour, (2*width/3, 0), (2*width/3, height), 7)
    pg.draw.line(screen, line_colour, (0, height/3), (width,height/3),7)
    pg.draw.line(screen, line_colour, (0,2*height/3), (width,2*height/3), 7)
    
game_initiating_window()


    
game_board = numz.numz_game()

def get_image(piece):
    piece = piece + '.png'
    index = image_names.index(piece)
    return images[index]
    
def draw_piece(row, col):
    if game_board.move_number > 5:
        old_position = game_board.piece_positions[game_board.move_number %6]
        remove_piece(old_position[0], old_position[1])
        print(game_board.piece_positions)
    piece = game_board.pieces[game_board.move_number %6]
    print(game_board.move_number)
    piece_image = get_image(piece)
    global board
    
    # for the first row, the image
    # should be pasted at a x coordinate
    # of 30 from the left margin
    if row == 1:
        posx = 30
        
    # for the second row, the image
    # should be pasted at a x coordinate
    # of 30 from the game line    
    if row == 2:

        # margin or width / 3 + 30 from
        # the left margin of the window
        posx = width / 3 + 30
        
    if row == 3:
        posx = width / 3 * 2 + 30

    if col == 1:
        posy = 30
        
    if col == 2:
        posy = height / 3 + 30
    
    if col == 3:
        posy = height / 3 * 2 + 30
        
    # setting up the required board
    # value to display
    board[row-1][col-1] = piece
    

    screen.blit(piece_image, (posy, posx))
    pg.display.update()

  
def user_click():
    # get coordinates of mouse click
    x, y = pg.mouse.get_pos()
    print(x)

    # get column of mouse click (1-3)
    if(x<width / 3):
        col = 1
    
    elif (x<width / 3 * 2):
        col = 2
    
    elif(x<width):
        col = 3
    
    else:
        col = None

    # get row of mouse click (1-3)
    if(y<height / 3):
        row = 1
    
    elif (y<height / 3 * 2):
        row = 2
    
    elif(y<height):
        row = 3
    
    else:
        row = None
   
    
    # after getting the row and col,
    # we need to draw the images at
    # the desired positions
    if(game_board.board[row-1][col-1] ==0):
        draw_piece(row, col)
        game_board.play_piece(row-1, col-1)
        global computer_turn 
        computer_turn = True
        print(game_board.piece_positions)
        if game_board.check_winning():
            print(f"Player number{game_board.move_number%2} won!")
            
def remove_piece(row, col):
    left = col*width/3+30
    top = row*height/3+30
    # screen.blit(pg.Rect(), dest)
    pg.draw.rect(screen, (255,255,255), pg.Rect(left, top, 80,80))
    
    
    pass     



while(True):
    

    if computer_turn:
        time.sleep(.1)
        move = numz.winning_agent(game_board)
        draw_piece(move[0]+1, move[1]+1)
        game_board.play_piece(move[0], move[1])
        computer_turn = False
        if game_board.check_winning():
            print('winner')
            pg.quit()
            sys.exit()
            break
    else:
        time.sleep(.1)
        move = numz.losing_agent(game_board)
        draw_piece(move[0]+1, move[1]+1)
        game_board.play_piece(move[0], move[1])
        computer_turn = True
        if game_board.check_winning():
            print('loser won')
            pg.quit()
            sys.exit()
            break
            
    # else:    
    #     for event in pg.event.get():
    
    #         if event.type == QUIT:
    #             pg.quit()
    #             sys.exit()
    #         elif event.type == MOUSEBUTTONDOWN:
    #             print(event)
    #             user_click()
            # if(winner or draw):
                # reset_game()
    pg.display.update()
    CLOCK.tick(fps)
    


    



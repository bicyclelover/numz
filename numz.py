# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 14:48:35 2022

@author: james
"""

class numz_game:
    def __init__(self):
        self.pieces = ['r1','b1','r2','b2','r3','b3']
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        self.move_number = 0
        self.piece_positions = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        self.rows = self.board
        self.columns = [[self.board[i][x] for i in [0,1,2]] for x in [0,1,2]]
        self.diagonals = [[self.board[i][i] for i in [0,1,2]],
                          [self.board[i[0]][i[1]]
                           for i in [[2,0], [1,1], [0,2]]]]
        self.red_pieces = ['r1','r2', 'r3']
        self.blue_pieces = ['b1', 'b2', 'b3']
                          
        
    def __str__(self):
        piece = self.pieces[self.move_number % 6]
        return f"next piece to play is:  {piece} /n current configuration is: /n {self.board}"
        
    def play_piece(self,x,y):
        piece = self.pieces[self.move_number % 6]
        position = [x,y]
        self.board[x][y] = piece
        self.piece_positions[self.move_number % 6] = position
        self.move_number += 1
        self.check_winning()
        
        
    def check_winning(self):
        for i in self.rows:
            if i == self.red_pieces or i ==self.red_pieces.reverse():
                print("red wins!")
            if i == self.blue_pieces or i == self.blue_pieces.reverse():
                print("blue wins!")
        
        

        
        
        
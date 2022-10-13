# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 14:48:35 2022

@author: james
"""
import random
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
        if self.move_number > 5:
            self.board[self.piece_positions[self.move_number % 6][0]][self.piece_positions[self.move_number % 6][1]] = 0
        self.piece_positions[self.move_number % 6] = position
        self.move_number += 1

        
        
    def check_winning(self):
        #rows
        for i in self.board:
            if i == self.red_pieces or i ==self.red_pieces.reverse():
                return True
            if i == self.blue_pieces or i == self.blue_pieces.reverse():
                return True
        #columns
        for i in [0,1,2]:
            column = [row[i] for row in self.board]
            if column == self.red_pieces or self.red_pieces.reverse():
                return True
            if column == self.blue_pieces or self.blue_pieces.reverse():
                return True

        #diagonals
        diagonals =[[self.board[i][i] for i in [0,1,2]],
                          [self.board[i[0]][i[1]]
                           for i in [[2,0], [1,1], [0,2]]]]
        for i in diagonals:
            if i == self.blue_pieces or self.blue_pieces.reverse():
                return True
            if i == self.red_pieces or self.red_pieces.reverse():
                return True
        return False




    def valid_moves(self):
        return [[i,j] for i in [0,1,2] for j in [0,1,2] if [i,j] not in self.piece_positions]


        

def random_agent(game_board):
    return random.choice(game_board.valid_moves())

def winning_agent(game_board):
    game_copy = game_board
    for i in game_board.valid_moves():
        game_copy.play_piece(i[0],i[1])
        if game_copy.check_winning():
            return i
        else:
            game_copy = game_board
    return random.choice(game_board.valid_moves())

def losing_agent(game_board):
    game_copy = game_board
    for i in game_board.valid_moves():
        game_copy.play_piece(i[0],i[1])
        if not game_copy.check_winning():
            return i
        else:
            game_copy = game_board
    return random.choice(game_board.valid_moves())
    

        


def play_game(agent_1, agent_2):
    players = [agent_1, agent_2]
    move_number = 0
    game_board = numz_game()
    while  not game_board.check_winning():
        move = players[move_number%2](game_board)
        game_board.play_piece(move[0], move[1])
        move_number+=1
    return move_number%2
    print(f'player {move_number%2} lost')
    print (game_board.board)


def play_n_games(n, agent_0, agent_1):
    player_0_wins = 0
    counter = 0
    while counter < n:
        player_0_wins += play_game(agent_0,agent_1)
        counter += 1
    return player_0_wins

def return_game(agent_1, agent_2):
    players = [agent_1, agent_2]
    move_number = 0
    game_board = numz_game()
    while  not game_board.check_winning():
        move = players[move_number%2](game_board)
        game_board.play_piece(move[0], move[1])
        move_number+=1
    return game_board


if __name__ == "__main__":
    print(play_n_games(1000,losing_agent, winning_agent))
    


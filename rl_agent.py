# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 10:35:36 2022

@author: james
"""

#basing this off of https://github.com/genyrosk/gym-chess/blob/master/gym_chess/envs/chess_v0.py

import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

from copy import copyfrom

import gym
from gym import spaces, error, utils
from gym.utils import seeding



import torch as th
import torch.nn as nn

from stable_baselines3 import PPO

pieces_to_ids = {
    'R1': 1,
    'B1': 2,
    'R2': 3,
    'B2': -1,
    'R3': -2,
    'B3': -3,
}

def sign(x):
    return (1,-1)[x<0]

def make_random_policy(np_random):
    def random_policy(state):
        opp_player = -1
        moves = numz_game_rl.available_moves(state, opp_player)
        return np.random.choice(available_moves)
    return random_policy

class numz_game_rl(gym.Env):
    def __init__(self, player_colour = 1, opponent = 'random', log = True):
        self.moves_max = 100
        self.log = log
        #3x3 board * 6 pieces = 54 possible moves
        self.observation_space = spaces.Box(-3,3, (3,3))
        self.action_space = spaces.Discrete(3*3*6)
        self.player = player_colour
        self.opponent = opponent
        self.seed()
        self.reset()

    def seed(self, seed = None):
        self.np_random, seed = seeding.np_random(seed)



    def step(self, action):
        assert self.action_space.contains(action), "Action error{}".format(action)

    def reset(self):
        self.state = {}
        self.done = False
        self.state['board'] = [[0,0,0],[0,0,0],[0,0,0]]
        self.current_player = 1
        self.state['move_number'] = 0
        self.state['pieces'] = [1,-1,2,-2,3,-3]
        self.current_positions = []

    def available_moves(state, player)):




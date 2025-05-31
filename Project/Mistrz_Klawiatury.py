#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import system
import sys

def clear():
    if game.is_running_in_console:
        system("cls")
    else:
        print()
        print()

def print_red(*args, **kwargs):
    if game.is_running_in_console:
        print("\033[31m", end = '')
        print(*args, **kwargs, end = '')
        print("\033[0m")
    else:
        print("ERR: ", end = '')
        print(*args, **kwargs)

class Difficulty:
    easy = 1
    medium = 2
    hard = 3

class Game:
    def __init__(self):
        self.difficulty = Difficulty.easy
        self.is_running_in_console = sys.stdin.isatty()

    def choose_difficulty(self):
        in_loop = True
        player_input = ""
        clear()
        print("====== Choose difficulty ======")
        print("type 'easy', 'medium' or 'hard'")
        while in_loop:
            player_input = input(" => ")
            player_input = player_input.lower()
            if player_input == "easy":
                self.difficulty = Difficulty.easy
                in_loop = False
            elif player_input == "medium":
                self.difficulty = Difficulty.medium
                in_loop = False
            elif player_input == "hard":
                self.difficulty = Difficulty.hard
                in_loop = False
            else:
                clear()
                print("====== Choose difficulty ======")
                print("type 'easy', 'medium' or 'hard'")
                print()
                print_red(f"'{player_input}' not recognised as game difficulty")


game = Game()

def main():
    pass

if __name__ == "__main__":
    main()
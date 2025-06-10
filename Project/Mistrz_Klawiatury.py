#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import random
import time
import sys


def main():
    pass


HIGHSCORES_FILE = "highscores.txt"
STATS_FILE = "stats.txt"


def save_highscore(result: ResultOfCheck):
    if not result.correct:
        return
    try:
        with open(HIGHSCORES_FILE, "a") as f:
            f.write(f"{result.time_spent:.2f},{result.correct_word}\n")
    except Exception as e:
        print_red(f"Error saving highscore: {e}")

if __name__ == "__main__":
    main()

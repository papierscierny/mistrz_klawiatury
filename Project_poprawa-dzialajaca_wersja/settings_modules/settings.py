#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Optional

words_in_not_special_mode = 10
""" Ilość słów wpisywanych w trybach: nauka i na czas."""

class Difficulty:
    """ Klasa przedstawia różne trudności gry za pomocą formatu int.
    Difficulty.easy  =  1
    Difficulty.medium = 2
    Difficulty.hard  =  3"""
    easy = 1
    medium = 2
    hard = 3


class GameMode:
    """Klasa przedstawia różne tryby gry za pomocą formatu int.
    GameMode.nauka = 1
    GameMode.na_czas = 2
    GameMode.specjalny = 3"""
    nauka = 1
    na_czas = 2
    specjalny = 3

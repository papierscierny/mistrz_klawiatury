#!/usr/bin/python
# -*- coding: utf-8 -*-

class ResultOfCheck:
    ''' Klasa przechowyjąca dane dotyczące wpisanego i sprawdzonego słowa.

    Inicjalizowanie:
    1. ResultOfCheck(word: str, time_spent: float)
    - word oznacza słowo, które było wpisywane
    - time_spent oznacza czas wpisywania słowa
    2. ResultOfCheck(word: str)
    - word oznacza tekst z zakodowanym słowem i czasem identycznym do str(ResultOfCheck)

    str(ResultOfCheck):
    Zwraca zakodowane słowo i czas wprowaczania słowa jako napis: "word|time_spent"
    '''
    def __init__(self, word: str, time_spent: float = None):
        new_word = word
        new_time_spent = time_spent

        if time_spent is None:
            new_word = new_word.strip('\n')
            new_word = new_word.strip()
            elements = new_word.split(sep='|')
            if len(elements) == 2:
                new_word = elements[0]
                new_time_spent = float(elements[1])

        self.word = new_word
        self.word_count = len(word.split())
        self.time_spent = new_time_spent

    def __str__(self):
        """
        str(ResultOfCheck):
        Zwraca zakodowane słowo i czas wprowaczania słowa jako napis: "word|time_spent"
        """
        return f"{self.word}|{str(self.time_spent)}"

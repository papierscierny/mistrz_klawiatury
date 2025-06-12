#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import random
import time
import sys
from typing import Optional, Any, Tuple, List

is_running_in_console = sys.stdin.isatty()

class ResultOfCheck:
    ''' Klasa przechowyjąca dane dotyczące wpisanego i sprawdzonego słowa '''
    def __init__(self, correct: bool = False, correct_word: str = "", typed_word: str = "", time_spent: float = 0):
        self.correct = correct
        self.correct_word = correct_word
        self.typed_word = typed_word
        self.time_spent = time_spent

    def __str__(self):
        return f"{str(self.correct)},{str(self.correct_word)},{str(self.typed_word)},{str(self.time_spent)}"

def str_to_ResultOfCheck(string: str) -> Optional[ResultOfCheck]:
    string = string.strip('\n')
    string = string.strip()
    elements = string.split(sep=',')
    if len(elements) != 4:
        return None

    result = ResultOfCheck()
    result.correct = bool(elements[0])
    result.correct_word = elements[1]
    result.typed_word = elements[2]
    result.time_spent = float(elements[3])

    return result

#funkcja odpowiedzialna za środkowanie tekstu
def txtcenter(txt):
    # Pobierz szerokość terminala
    try:
        terminal_width = os.get_terminal_size().columns
    except:
        terminal_width = 80  # Domyślna szerokość jeśli nie uda się wykryć

    d = (terminal_width - len(txt)) // 2

    #sprawdzanie czy d nie jest ujemne
    if(d < 0):
        d = 0
    # Wyświetl linię z wyliczonym wcięciem i kolorem
    print(' ' * d + txt)

#funkcja ekranu startowego
def start():
    #czyszczenie konsoli na początek
    os.system('cls' if os.name == 'nt' else 'clear') 

    #NAPIS TYTUŁOWY
    #Tekst tytułowy
    ascii_art = """
        ███╗░░░███╗██╗░██████╗████████╗██████╗░███████╗   ██╗░░██╗██╗░░░░░░█████╗░░██╗░░░░░░░██╗██╗░█████╗░████████╗██╗░░░██╗██████╗░██╗░░░██╗
        ████╗░████║██║██╔════╝╚══██╔══╝██╔══██╗╚════██║   ██║░██╔╝██║░░░░░██╔══██╗░██║░░██╗░░██║██║██╔══██╗╚══██╔══╝██║░░░██║██╔══██╗╚██╗░██╔╝
        ██╔████╔██║██║╚█████╗░░░░██║░░░██████╔╝░░███╔═╝   █████═╝░██║░░░░░███████║░╚██╗████╗██╔╝██║███████║░░░██║░░░██║░░░██║██████╔╝░╚████╔╝░
        ██║╚██╔╝██║██║░╚═══██╗░░░██║░░░██╔══██╗██╔══╝░░   ██╔═██╗░██║░░░░░██╔══██║░░████╔═████║░██║██╔══██║░░░██║░░░██║░░░██║██╔══██╗░░╚██╔╝░░
        ██║░╚═╝░██║██║██████╔╝░░░██║░░░██║░░██║███████╗   ██║░╚██╗███████╗██║░░██║░░╚██╔╝░╚██╔╝░██║██║░░██║░░░██║░░░╚██████╔╝██║░░██║░░░██║░░░
        ╚═╝░░░░░╚═╝╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝   ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░
    """

    # Podziel tekst na linie i usuń puste linie na początku i na końcu
    lines = [line for line in ascii_art.split('\n') if line.strip() != '']



    # Wyświetl każdą linię wycentrowaną na zielono
    print("\033[32m")
    for i in lines:
        txtcenter(i)
    print("\033[0m")

    #NACIŚNIJ ENTER
    print("\n"*5)
    txtcenter("\033[31mNaciśnij [Enter] przycisk aby przejść dalej.\033[0m")

    #Sprawdzanie czy naciśnięto enter
    input("")

    #PRZEJŚCIE DALEJ
    #czyszczenie konsoli
    os.system('cls' if os.name == 'nt' else 'clear') 

def clear():
    ''' Funkcja służy do czyszczenia konsoli '''
    if is_running_in_console:
        os.system("cls")
    else:
        print()
        print()

def print_red(*args, **kwargs):
    ''' Funkcja wypisuje przekazany napis w kolorze czerwonym '''
    if is_running_in_console:
        print("\033[31m", end = '')
        print(*args, **kwargs, end = '')
        print("\033[0m")
    else:
        print("ERR: ", end = '')
        print(*args, **kwargs)

class Difficulty:
    ''' Klasa przedstawia różne trudności gry za pomocą formatu int '''
    easy = 1
    medium = 2
    hard = 3

def difficulty_to_str(difficulty: int) -> str:
    ''' Funkcja zamienia trudność [int] do napisu [str] '''
    if difficulty == Difficulty.easy:
        return "easy"
    if difficulty == Difficulty.medium:
        return "medium"
    if difficulty == Difficulty.easy:
        return "hard"
    return "None"


def str_to_difficulty(string: str) -> Optional[int]:
    ''' Funkcja zamienia napis [str] do trudności [int] '''
    string = string.strip('\n')
    string = string.strip()
    if string == "easy":
        return Difficulty.easy
    if string == "medium":
        return Difficulty.medium
    if string == "hard":
        return Difficulty.hard
    return None


def print_word_and_check(word: str) -> ResultOfCheck:
    ''' Funkcja wypisuje podane słowo, sprawdza poprawność i zwraca wynik '''
    print("Type:")
    print("     " + word)
    typed = input("   - ")
    typed = typed.strip('\n')
    typed = typed.strip()
    return ResultOfCheck(correct=(typed == word), correct_word=word, typed_word=typed)

def random_word_from_file(file_name: str) -> Optional[str]:
    ''' Funkcja wybiera przypadkowe słowo z pliku .txt o podanej nazwie. W przypadku błędu zwraca None '''
    try:
        lines = []
        with open(file_name, 'r') as file:
            lines = file.readlines()
        word = random.choice(lines)
        word = word.strip('\n')
        word = word.strip()
        return word
    except:
        return None




class Game:
    ''' Główna klasa zawierająca funkcjonalność gry '''
    def __init__(self):
        self.difficulty = Difficulty.easy

    def choose_difficulty(self):
        ''' Funkcja służąca do wyboru trudności rozgrywki '''
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
    start()

if __name__ == "__main__":
    main()

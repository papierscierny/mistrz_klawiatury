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

def txtcenter(txt):
    try:
        terminal_width = os.get_terminal_size().columns
    except:
        terminal_width = 80

    d = (terminal_width - len(txt)) // 2
    if (d < 0):
        d = 0
    print(' ' * d + txt)


def start():
    os.system('cls' if os.name == 'nt' else 'clear')

    ascii_art = """
        ███╗░░░███╗██╗░██████╗████████╗██████╗░███████╗   ██╗░░██╗██╗░░░░░░█████╗░░██╗░░░░░░░██╗██╗░█████╗░████████╗██╗░░░██╗██████╗░██╗░░░██╗
        ████╗░████║██║██╔════╝╚══██╔══╝██╔══██╗╚════██║   ██║░██╔╝██║░░░░░██╔══██╗░██║░░██╗░░██║██║██╔══██╗╚══██╔══╝██║░░░██║██╔══██╗╚██╗░██╔╝
        ██╔████╔██║██║╚█████╗░░░░██║░░░██████╔╝░░███╔═╝   █████═╝░██║░░░░░███████║░╚██╗████╗██╔╝██║███████║░░░██║░░░██║░░░██║██████╔╝░╚████╔╝░
        ██║╚██╔╝██║██║░╚═══██╗░░░██║░░░██╔══██╗██╔══╝░░   ██╔═██╗░██║░░░░░██╔══██║░░████╔═████║░██║██╔══██║░░░██║░░░██║░░░██║██╔══██╗░░╚██╔╝░░
        ██║░╚═╝░██║██║██████╔╝░░░██║░░░██║░░██║███████╗   ██║░╚██╗███████╗██║░░██║░░╚██╔╝░╚██╔╝░██║██║░░██║░░░██║░░░╚██████╔╝██║░░██║░░░██║░░░
        ╚═╝░░░░░╚═╝╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝╚══════╝   ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░
    """

    print("\033[32m")
    for i in [line for line in ascii_art.split('\n') if line.strip() != '']:
        txtcenter(i)
    print("\033[0m")

    print("\n" * 5)
    txtcenter("\033[31mNaciśnij [Enter] przycisk aby przejść dalej.\033[0m")
    input("")
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

    if game.is_running_in_console:
        print("\033[31m", end='')
        print(*args, **kwargs, end='')
        print("\033[0m")
    else:
        print("ERR: ", end='')
        print(*args, **kwargs)


class Difficulty:
    ''' Klasa przedstawia różne trudności gry za pomocą formatu int '''
    easy = 1
    medium = 2
    hard = 3


class GameMode:
    nauka = 1
    na_czas = 2


def difficulty_to_str(difficulty: int) -> str:
    ''' Funkcja zamienia trudność [int] do napisu [str] '''
    if difficulty == Difficulty.easy:
        return "easy"
    if difficulty == Difficulty.medium:
        return "medium"
    if difficulty == Difficulty.hard:
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


def game_mode_to_str(mode: int) -> str:
    if mode == GameMode.nauka:
        return "nauka"
    if mode == GameMode.na_czas:
        return "na czas"
    return "None"


def str_to_game_mode(string: str) -> Optional[int]:
    string = string.strip('\n')
    string = string.strip()
    if string == "nauka":
        return GameMode.nauka
    if string == "na czas":
        return GameMode.na_czas
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

def end(n, t):
    os.system('cls' if os.name == 'nt' else 'clear') 

    #NAPIS TYTUŁOWY
    #Tekst końca
    ascii_art = """
        ░▒█░▄▀░▒█▀▀▀█░▒█▄░▒█░▀█▀░▒█▀▀▀░▒█▀▀▄░░░▒█▀▀█░▒█▀▀▄░▒█░░▒█
        ░▒█▀▄░░▒█░░▒█░▒█▒█▒█░▒█░░▒█▀▀▀░▒█░░░░░░▒█░▄▄░▒█▄▄▀░▒▀▄▄▄▀
        ░▒█░▒█░▒█▄▄▄█░▒█░░▀█░▄█▄░▒█▄▄▄░▒█▄▄▀░░░▒█▄▄▀░▒█░▒█░░░▒█░░

    """

    # Podziel tekst na linie i usuń puste linie na początku i na końcu
    lines = [line for line in ascii_art.split('\n') if line.strip() != '']

    # Wyświetl każdą linię wycentrowaną na czerwono
    print("\033[31m")
    for i in lines:
        txtcenter(i)
    print("\033[0m")

    endtab = ["-----------------------------------------------------", 
    f"|   Przepisane słowa   |             {n:.0f}              |",
    "|---------------------------------------------------|",
    f"|    Czas całkowity    |           {t:.2f}s            |",
    "|---------------------------------------------------|",
    f"| Średni czas na słowo |           {t/n:.2f}s            |",
    "-----------------------------------------------------"]

    #ustaw kolor na czerwony
    print("\033[33m")

    for i in endtab:
        txtcenter(i)

    #reset koloru
    print("\033[0m")

    #NACIŚNIJ ENTER
    print("\n"*5)
    print("\033[31m")
    txtcenter("Naciśnij [Enter] aby rozpocząć od nowa.")
    print("\033[0m")

    #Sprawdzanie czy naciśnięto enter
    input("")

    #PRZEJŚCIE DALEJ
    #czyszczenie konsoli
    os.system('cls' if os.name == 'nt' else 'clear')


def write_to_history_file(result: ResultOfCheck):
    ''' Funkcja dopisuje jeden wynik do historii '''
    try:
        with open("History.txt", 'a') as file:
            file.write(str(result) + "\n")
    except:
        pass


def read_from_history_file() -> Optional[List[ResultOfCheck]]:
    ''' Funkcja odczytuje historię z pliku; zwraca None jeżeli nie ma pliku lub wystąpił błąd '''
    try:
        results_list = []
        with open("History.txt", 'r') as file:
            lines = file.readlines()
            if len(lines) < 2:
                return None
            for line in lines:
                result = str_to_ResultOfCheck(line)
                if result is not None:
                    results_list.append(result)
        return results_list
    except:
        return None


def clear_history_file():
    ''' Funkcja czyści plik historii jeżeli istnieje '''
    try:
        with open("History.txt", 'w'):
            pass
    except:
        pass




class Game:
    ''' Główna klasa zawierająca funkcjonalność gry '''
    def __init__(self):
        self.difficulty = None
        self.game_mode = None

    def choose_difficulty(self):
        ''' Funkcja służąca do wyboru trudności rozgrywki '''
        in_loop = True
        player_input = ""
        clear()
        print("====== Wybierz poziom trudności ======")
        print("Dostępne opcje: easy, medium, hard")
        while self.difficulty is None:
            choice = input("Twój wybór: ").lower()
            self.difficulty = str_to_difficulty(choice)
            if self.difficulty is None:
                print_red("Nieprawidłowy wybór! Spróbuj ponownie.")

    def choose_game_mode(self):
        clear()
        print("====== Wybierz tryb gry ======")
        print("Dostępne tryby: nauka, na czas")
        while self.game_mode is None:
            choice = input("Twój wybór: ").lower()
            self.game_mode = str_to_game_mode(choice)
            if self.game_mode is None:
                print_red("Nieprawidłowy wybór! Spróbuj ponownie.")

    def play(self):
        self.choose_game_mode()
        self.choose_difficulty()

        clear()
        print(f"Tryb gry: {game_mode_to_str(self.game_mode)}")
        print(f"Poziom trudności: {difficulty_to_str(self.difficulty)}")
        print("\nRozpoczynamy test...")
        time.sleep(2)

        words_to_test = 3
        correct = 0

        for i in range(words_to_test):
            clear()
            word = random_word_from_file("Test.txt") or "default"
            print(f"Słowo {i + 1}/{words_to_test}:")
            result = print_word_and_check(word)

            if result.correct:
                correct += 1
                print("\033[32mPoprawnie!\033[0m")
            else:
                print_red(f"Błąd! Powinno być: '{word}'")

            if i < words_to_test - 1:
                input("Naciśnij Enter, aby kontynuować...")

        clear()
        print("=== Podsumowanie ===")
        print(f"Poprawne odpowiedzi: {correct}/{words_to_test}")
        print(f"Tryb: {game_mode_to_str(self.game_mode)}")
        print(f"Poziom: {difficulty_to_str(self.difficulty)}")


game = Game()


def main():
    start()
    game.play()


if __name__ == "__main__":
    main()
    input("\nNaciśnij Enter, aby zakończyć...")

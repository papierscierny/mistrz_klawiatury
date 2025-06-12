#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import random
import time
import sys
from typing import Optional, Any, Tuple, List


class ResultOfCheck:
    def __init__(self, correct: bool = False, correct_word: str = "", typed_word: str = "", time_spent: float = 0):
        self.correct = correct
        self.correct_word = correct_word
        self.typed_word = typed_word
        self.time_spent = time_spent

    def __str__(self):
        return f"{str(self.correct)},{str(self.correct_word)},{str(self.typed_word)},{str(self.time_spent)}"

class BestScores:
    def __init__(self):
        self.best_time_per_letter_easy = -1.0
        self.best_time_per_letter_medium = -1.0
        self.best_time_per_letter_hard = -1.0

    def __add__(self, other):
        new_scores = BestScores()

        new_scores.best_time_per_letter_easy = min(self.best_time_per_letter_easy, other.best_time_per_letter_easy)
        new_scores.best_time_per_letter_medium = min(self.best_time_per_letter_medium,
                                                     other.best_time_per_letter_medium)
        new_scores.best_time_per_letter_hard = min(self.best_time_per_letter_hard, other.best_time_per_letter_hard)

        if new_scores.best_time_per_letter_easy == -1.0:
            new_scores.best_time_per_letter_easy = max(self.best_time_per_letter_easy, other.best_time_per_letter_easy)

        if new_scores.best_time_per_letter_medium == -1.0:
            new_scores.best_time_per_letter_medium = max(self.best_time_per_letter_medium,
                                                         other.best_time_per_letter_medium)

        if new_scores.best_time_per_letter_hard == -1.0:
            new_scores.best_time_per_letter_hard = max(self.best_time_per_letter_hard, other.best_time_per_letter_hard)

        return new_scores

    def read_best_scores_from_file() -> Optional[BestScores]:
    try:
        with open("BestScores.txt", 'r') as file:
            lines = file.readlines()
            if len(lines) < 3:
                return None

            easy_score = lines[0]
            easy_score = easy_score.strip('\n')
            easy_score = easy_score.strip()

            medium_score = lines[1]
            medium_score = medium_score.strip('\n')
            medium_score = medium_score.strip()

            hard_score = lines[2]
            hard_score = hard_score.strip('\n')
            hard_score = hard_score.strip()

            easy_score_f = float(easy_score)
            medium_score_f = float(medium_score)
            hard_score_f = float(hard_score)

            if easy_score_f is None or medium_score_f is None or hard_score_f is None:
                return None

            best_scores = BestScores()
            best_scores.best_time_per_letter_easy = easy_score_f
            best_scores.best_time_per_letter_medium = medium_score_f
            best_scores.best_time_per_letter_hard = hard_score_f
            return best_scores
    except:
        return None

    def update(self, result: ResultOfCheck, difficulty: int):
        best_time_per_letter = result.time_spent / len(result.typed_word)

        if difficulty == Difficulty.easy:
            if self.best_time_per_letter_easy == -1.0:
                self.best_time_per_letter_easy = best_time_per_letter

            if self.best_time_per_letter_easy > best_time_per_letter:
                self.best_time_per_letter_easy = best_time_per_letter

        if difficulty == Difficulty.medium:
            if self.best_time_per_letter_medium == -1.0:
                self.best_time_per_letter_medium = best_time_per_letter

            if self.best_time_per_letter_medium > best_time_per_letter:
                self.best_time_per_letter_medium = best_time_per_letter

        if difficulty == Difficulty.hard:
            if self.best_time_per_letter_hard == -1.0:
                self.best_time_per_letter_hard = best_time_per_letter

            if self.best_time_per_letter_hard > best_time_per_letter:
                self.best_time_per_letter_hard = best_time_per_letter



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
    if game.is_running_in_console:
        os.system("cls")
    else:
        print()
        print()


def print_red(*args, **kwargs):
    if game.is_running_in_console:
        print("\033[31m", end='')
        print(*args, **kwargs, end='')
        print("\033[0m")
    else:
        print("ERR: ", end='')
        print(*args, **kwargs)


class Difficulty:
    easy = 1
    medium = 2
    hard = 3


class GameMode:
    nauka = 1
    na_czas = 2


def difficulty_to_str(difficulty: int) -> str:
    if difficulty == Difficulty.easy:
        return "easy"
    if difficulty == Difficulty.medium:
        return "medium"
    if difficulty == Difficulty.hard:
        return "hard"
    return "None"


def str_to_difficulty(string: str) -> Optional[int]:
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
    print("Type:")
    print("     " + word)
    typed = input("   - ")
    typed = typed.strip('\n')
    typed = typed.strip()
    return ResultOfCheck(correct=(typed == word), correct_word=word, typed_word=typed)


def random_word_from_file(file_name: str) -> Optional[str]:
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
    try:
        with open("History.txt", 'a') as file:
            file.write(str(result) + "\n")
    except:
        pass


def read_from_history_file() -> Optional[List[ResultOfCheck]]:
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
    try:
        with open("History.txt", 'w'):
            pass
    except:
        pass


def write_to_settings_file(game_mode: int, difficulty: int):
    op = 'w'
    try:
        with open("Settings.txt", 'r'):
            pass
    except:
        op = 'x'

    with open("Settings.txt", op) as file:
        file.write(f"{game_mode_to_str(game_mode)}\n{difficulty_to_str(difficulty)}")


def read_from_settings_file() -> Optional[Tuple[int, int]]:
    try:
        with open("Settings.txt", 'r') as file:
            lines = file.readlines()
            game_mode = str_to_game_mode(lines[0])
            difficulty = str_to_difficulty(lines[1])
            if game_mode is None or difficulty is None:
                print(lines[0] + " - " + lines[1])
                print(str(difficulty) + " - " + str(game_mode))
                return None
            return game_mode, difficulty
    except:
        return None


def clear_settings_file():
    try:
        with open("Settings.txt", 'w'):
            pass
    except:
        pass

class Game:
    def __init__(self):
        self.difficulty = None
        self.game_mode = None
        self.is_running_in_console = sys.stdin.isatty()

    def choose_difficulty(self):
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


if _name_ == "_main_":
    main()
    input("\nNaciśnij Enter, aby zakończyć...")

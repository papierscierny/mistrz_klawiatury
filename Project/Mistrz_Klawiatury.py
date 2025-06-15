#!/usr/bin/python
# -*- coding: utf-8 -*-
import msvcrt
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

    if is_running_in_console:
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
    specjalny = 3  # Dodany nowy tryb specjalny


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

def write_best_scores_to_file(scores: BestScores):
    previous_scores = read_best_scores_from_file()

    open_operator = 'w'
    try:
        with open("BestScores.txt", 'w'):
            pass
    except:
        open_operator = 'x'

    if previous_scores is None:
        with open("BestScores.txt", open_operator) as file:
            file.write(
                f"{scores.best_time_per_letter_easy}\n{scores.best_time_per_letter_medium}\n{scores.best_time_per_letter_hard}")
    else:
        new_scores = scores + previous_scores
        with open("BestScores.txt", open_operator) as file:
            file.write(
                f"{new_scores.best_time_per_letter_easy}\n{new_scores.best_time_per_letter_medium}\n{new_scores.best_time_per_letter_hard}")

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
    if mode == GameMode.specjalny:  # Dodana obsługa nowego trybu 
        return "specjalny"          
    return "None"


def str_to_game_mode(string: str) -> Optional[int]:
    string = string.strip('\n')
    string = string.strip()
    if string == "nauka":
        return GameMode.nauka
    if string == "na czas":
        return GameMode.na_czas
    if string == "specjalny":        # Dodana obsługa nowego trybu 
        return GameMode.specjalny    
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

def write_best_scores_to_file(scores: BestScores):
    previous_scores = read_best_scores_from_file()

    open_operator = 'w'
    try:
        with open("BestScores.txt", 'w'):
            pass
    except:
        open_operator = 'x'

    if previous_scores is None:
        with open("BestScores.txt", open_operator) as file:
            file.write(
                f"{scores.best_time_per_letter_easy}\n{scores.best_time_per_letter_medium}\n{scores.best_time_per_letter_hard}")
    else:
        new_scores = scores + previous_scores
        with open("BestScores.txt", open_operator) as file:
            file.write(
                f"{new_scores.best_time_per_letter_easy}\n{new_scores.best_time_per_letter_medium}\n{new_scores.best_time_per_letter_hard}")

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


def measure_time(function, *args, **kwargs) -> Tuple[Any, float]:
    start_time = time.time()
    result = function(*args, **kwargs)
    end_time = time.time()
    return result, end_time - start_time

class Game:
    ''' Główna klasa zawierająca funkcjonalność gry '''
    def __init__(self):
        self.difficulty = None
        self.game_mode = None

    def begin(self) -> None:
        
        settings = read_from_settings_file()
        if settings is None:
            start()
            self.play()
            return

        history = read_from_history_file()
        if history is None:
            start()
            self.play()
            return

        best_scores = read_best_scores_from_file()
        if best_scores is None:
            best_scores = BestScores()

        game_mode, difficulty = settings
        self.game_mode = game_mode
        self.difficulty = difficulty

        if game_mode == GameMode.na_czas:
            self.play_game_mode_na_czas(len(history), history, best_scores)


    def choose_difficulty(self):
        if self.game_mode == GameMode.specjalny:                        ''' Tryb specjalny - pominięcie wyboru trudności oraz wyświetlenie zasad
            clear()
            print("\033[31mTRYB SPECJALNY\033[0m")
            print("Zasady:")
            print("- Wpisz jak najszybciej wyświetlony tekst")
            print("- Gdy popełnisz błąd, nie możesz kontynuować")
            print("- Musisz poprawić błąd zanim przejdziesz dalej")
            print("\n\033[33mPOWODZENIA!\033[0m")
            time.sleep(4)  # Wiadomość będzie widoczna przez 4 sekundy
            return                                                      '''
          
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
        print("Dostępne tryby: nauka, na czas, specjalny")    # Dodana opcja specjalny
        while self.game_mode is None:
            choice = input("Twój wybór: ").lower()
            self.game_mode = str_to_game_mode(choice)
            if self.game_mode is None:
                print_red("Nieprawidłowy wybór! Spróbuj ponownie.")
                
    def _special_game_mode(self):
        try:
            with open('teksty.txt', 'r', encoding='utf-8') as f:
                content = f.read()
                texts = [t.strip() for t in content.split('\n\n') if t.strip()]

            if texts:
                text = random.choice(texts)
                clear()
                print("Wylosowany tekst:\n")
                print(text)
                print("\n")

                current_position = 0
                start_time = time.time()  

                while current_position < len(text):
                    char = msvcrt.getch()                         #Odczyt klawisza i pomijanie klawiszy specjalnych

                    if char in (b'\x00', b'\xe0'):
                        msvcrt.getch()
                        continue

                    try:                                             #Konwersja bajtu na znak i ignorowanie błędów
                        char = char.decode('utf-8')
                    except UnicodeDecodeError:
                        continue

                    if char == '\r' or char == '\x08':                    #ignorowanie klawisza Enter i backspace
                        continue

                    expected_char = text[current_position]                        #sprawdzenie czy obecny znak jest zgodny
                    if char == expected_char:
                        print(f"\033[32m{char}\033[0m", end='', flush=True)
                        current_position += 1

                end_time = time.time()                                                    #wyświetlenie wyników
                duration = end_time - start_time  
                word_count = len(text.split())
                wpm = (word_count / duration) * 60
                print("\n")
                summary_title = "PODSUMOWANIE WYNIKU"
                print("\n" + summary_title.center(37))
                print("-" * 37)
                print("| {:^15} | {:^15} |".format("Czas [s]", "Słów na minutę"))
                print("|" + "-" * 17 + "+" + "-" * 17 + "|")
                print("| {:^15.2f} | {:^15.2f} |".format(duration, wpm))
                print("-" * 37 + "\n")

                input("Naciśnij Enter, aby kontynuować...")

            else:
                print_red("Brak tekstów w pliku")

        except Exception as e:
            print_red(f"Błąd wczytywania pliku: {str(e)}")

    def play_game_mode_na_czas(self, words_done: int = 0, results: List[ResultOfCheck] = None, scores: BestScores = None):
        best_scores = BestScores()

        if results is None:
            results = []
        if scores is not None:
            best_scores = scores

        file_name = ""
        if self.difficulty == Difficulty.easy:
            file_name = "latwe_slowa.txt"
        elif self.difficulty == Difficulty.medium:
            file_name = "medium_difficulty.txt"
        elif self.difficulty == Difficulty.hard:
            file_name = "Trudne słówka.txt"

        while words_done < 10:
            words_done += 1
            in_loop = True
            word = random_word_from_file(file_name)
            time_spent_on_word = 0.0
            while in_loop:
                clear()
                result, time_spent = measure_time(print_word_and_check, word)
                time_spent_on_word += time_spent + 0 if result.correct else 10  # czas na pisanie + ewentualna kara czasowa 10s
                if result.correct:
                    in_loop = False
                    result.time_spent = time_spent_on_word
                    results.append(result)
                    best_scores.update(result, self.difficulty)
                    write_to_history_file(result)

        previous_scores = read_best_scores_from_file()

        self.end_screen(best_scores)

        write_best_scores_to_file(best_scores)
        clear_history_file()
        clear_settings_file()
        

    def play(self):
        self.choose_game_mode()
        self.choose_difficulty()

        clear()
        print(f"Tryb gry: {game_mode_to_str(self.game_mode)}") 
        if self.game_mode != GameMode.specjalny:                                #pominięcie wyświetlania poziomu dla trybu specjalnego              
            print(f"Poziom trudności: {difficulty_to_str(self.difficulty)}")
        print("\nRozpoczynamy test...")
        time.sleep(2)
        if self.game_mode == GameMode.specjalny:
            self._special_game_mode()
            return
            
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
    game.begin()


if __name__ == "__main__":
    main()
    input("\nNaciśnij Enter, aby zakończyć...")

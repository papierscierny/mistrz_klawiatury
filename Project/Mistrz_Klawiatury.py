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
    specjalny = 3  # Dodany nowy tryb specjalny


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



class Game:
    def __init__(self):
        self.difficulty = None
        self.game_mode = None
        self.is_running_in_console = sys.stdin.isatty()

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

    def play(self):
        self.choose_game_mode()
        self.choose_difficulty()

        clear()
        print(f"Tryb gry: {game_mode_to_str(self.game_mode)}") 
        if self.game_mode != GameMode.specjalny:                                #pominięcie wyświetlania poziomu dla trybu specjalnego              
            print(f"Poziom trudności: {difficulty_to_str(self.difficulty)}")
        print("\nRozpoczynamy test...")
        time.sleep(2)
        
        if self.game_mode == GameMode.specjalny:                                  '''obsługa trybu specjalnego i wyświetlenie losowego tekstu 
            # MINIMALNA OBSŁUGA TRYBU SPECJALNEGO
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
                else:
                    print_red("Brak tekstów w pliku")
            except Exception as e:
                print_red(f"Błąd wczytywania pliku: {str(e)}")
            return                                                                    '''
    
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

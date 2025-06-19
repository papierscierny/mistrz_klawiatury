#!/usr/bin/python
# -*- coding: utf-8 -*-
import msvcrt
import os
import sys
import time

from checking_module.checking import ResultOfCheck
from settings_modules.settings import GameMode, Difficulty

is_running_in_console = sys.stdin.isatty()


def clear_screen():
    """ Funkcja służy do czyszczenia konsoli

    Funkcjonalność różni się w zależności od środowiska uruchomieniowego:
    - konsola windows - czyści konsolę
    - w przeciwnym wypadku wyświetla 2 puste linie"""
    if is_running_in_console:
        os.system("cls")
    else:
        print()
        print()


def txtcenter(txt):
    """Funkcja wypisyje przekazany napis na środku konsoli.
    W przypadku braku informacji o szerokości konsoli sakładana jest szerokość 80 znaków
    Środkowanie napisu dokonywane jest poprzez dodanie odpowiedniej ilości spacji przed przekazanym napisem"""
    try:
        terminal_width = os.get_terminal_size().columns
    except:
        terminal_width = 80

    d = (terminal_width - len(txt)) // 2
    if d < 0:
        d = 0
    print(' ' * d + txt)


def start_screen():
    """Funkcja wyświetla ekran powitalny gry.
    Wyjście z funkcji następuje po naciśnięciu klawisza enter"""

    clear_screen()

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
    clear_screen()


def choose_difficulty(game_mode: int) -> int:
    """Funkcja wyświetla ekran wyboru trudności rozgrywki.
    W przypadku gdy game_mode == GameMode.specjalny ekran jest pomijany.

    Funkcja wyświetla dostępne opcje i sprawdza, czy wpisany przez użytkownika mapis jest opcją trudności.
    Jeżeli napis nie jest opcją trudności ekran uruchamia się ponownie wraz z kominikatem o niepowidzeniu.
    Jeżeli napis jest opcją trudności: zwracany jest poziom trudności wybrany z klasy Difficulty
    """
    if game_mode == GameMode.specjalny:
        return Difficulty.easy

    clear_screen()
    print("====== Wybierz poziom trudności ======")
    print("Dostępne opcje: easy, medium, hard")

    while True:
        choice = input("Twój wybór: ").lower().strip('\n').strip()
        if choice == "easy":
            return Difficulty.easy
        elif choice == "medium":
            return Difficulty.medium
        elif choice == "hard":
            return Difficulty.hard

        clear_screen()
        print("====== Wybierz poziom trudności ======")
        print("Dostępne opcje: easy, medium, hard")
        print("\033[31m Nieprawidłowy wybór! Spróbuj ponownie. \033[0m")


def choose_game_mode() -> int:
    """Funkcja wyświetla ekran wyboru trybu rozgrywki.

        Funkcja wyświetla dostępne opcje i sprawdza, czy wpisany przez użytkownika mapis jest trybem rozgrywki.
        Jeżeli napis nie jest trybem rozgrywki ekran uruchamia się ponownie wraz z kominikatem o niepowidzeniu.
        Jeżeli napis jest trybem rozgrywki: zwracany jest tryb rozgrywki wybrany z klasy GameMode
        """
    clear_screen()
    print("====== Wybierz tryb gry ======")
    print("Dostępne tryby: nauka, na czas, specjalny")

    while True:
        choice = input("Twój wybór: ").lower().strip('\n').strip()
        if choice == "nauka":
            return GameMode.nauka
        elif choice == "na czas":
            return GameMode.na_czas
        elif choice == "specjalny":
            return GameMode.specjalny

        clear_screen()
        print("====== Wybierz tryb gry ======")
        print("Dostępne tryby: nauka, na czas, specjalny")
        print("\033[31m Nieprawidłowy wybór! Spróbuj ponownie. \033[0m")


def show_word_and_check(word: str) -> ResultOfCheck:
    """Funkcja wyświetla przekazany napis na ekran, następnie pozwala tylko na wprowadzanie znaków zgodnych z wyświetlonym słowem. Po wprowadzeniu całego słowa zwraca rezultat"""
    clear_screen()
    print("Wylosowany tekst:\n")
    print(word)
    print("\n")

    current_position = 0
    start_time = time.time()

    while current_position < len(word):
        
        char = msvcrt.getch()  #Odczyt klawisza i pomijanie klawiszy specjalnych

        if char in (b'\x00', b'\xe0'):
            msvcrt.getch()
            continue

        try:  #Konwersja bajtu na znak i ignorowanie błędów
            char = char.decode('utf-8')
        except UnicodeDecodeError:
            continue

        if char == '\r' or char == '\x08':  #ignorowanie klawisza Enter i backspace
            continue

        expected_char = word[current_position]  #sprawdzenie czy obecny znak jest zgodny
        if char == expected_char:
            print(f"\033[32m{char}\033[0m", end='', flush=True)
            current_position += 1

    end_time = time.time()
    duration = end_time - start_time

    return ResultOfCheck(word, duration)


def end_screen(n: int, t: float):
    """Funkcja wyświetla ekran końcowy.
    Argument n oznacza ilość przepisanych słów
    Argument t oznacza całkowity czas wpisywania wszystkich słów

    Funkcja kończy działanie po naciśnięciu klawisza enter
    """
    clear_screen()

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
              f"| Średni czas na słowo |           {t / n:.2f}s            |",
              "-----------------------------------------------------"]

    #ustaw kolor na czerwony
    print("\033[33m")

    for i in endtab:
        txtcenter(i)

    #reset koloru
    print("\033[0m")

    #NACIŚNIJ ENTER
    print("\n" * 5)
    print("\033[31m")
    txtcenter("Naciśnij [Enter] aby zakończyć.")
    print("\033[0m")

    #Sprawdzanie czy naciśnięto enter
    input("")

    #PRZEJŚCIE DALEJ
    #czyszczenie konsoli
    clear_screen()

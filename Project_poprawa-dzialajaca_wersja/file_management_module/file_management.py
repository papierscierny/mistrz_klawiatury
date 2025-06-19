#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from typing import Optional, List, Tuple

from checking_module.checking import ResultOfCheck
from settings_modules.settings import GameMode, Difficulty


class FileHandler:
    """Klasa bazowa zajmująca się komunikacją z plikami tekstowymi

    * Inicjalizacja:
    FileHandler(file_name: str)
    - file_name to nazwa pliku tekstowego np. "Dokument.txt"

    * Dostępne zmienne:
    started_empty: bool - True jeśli plik został utworzony w obecnej sesji lub podczas uruchamiania plik jest pusty

    * Dostępne funkcje:
    clear() - czyści plik tekstowy

    write_line(line: str) - dodaje nową linię do tekstu i wpisuje do niej napis przekazany w line

    write_lines(str_list: List[str]) - analogicznie do write_line, ale wpisuje kolejno napisy z listy

    read_lines() -> Optional[List[str]] - zawaca listę zawierającą kolejne linie tekstu w pliku, zwraca None jeżeli plik jest pusty
    """
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.started_empty = True

        try:
            with open(self.file_name, 'r') as file:
                self.started_empty = file.readlines() == []
        except:
            with open(self.file_name, 'x'):
                pass
            self.created_this_session = True

    def clear(self):
        """Funkcja czyści plik tekstowy"""
        with open(self.file_name, 'w'):
            pass

    def write_line(self, line: str):
        """Funkcja dodaje nową linię do tekstu i wpisuje do niej napis przekazany w line"""
        with open(self.file_name, 'a') as file:
            file.write(line + '\n')

    def write_lines(self, str_list: List[str]):
        """Funkcja dodaje wiele linii tekstu zgodnie z kolejnością napisów w liście"""
        with open(self.file_name, 'a') as file:
            file.writelines(str_list)

    def read_lines(self) -> Optional[List[str]]:
        """Funkcja odczytuje wszystkie linie z pliku i zwraca je jako lista napisów.
        Zwraca None jeśli plik jest pusty"""
        lines = []
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
        if not lines:
            return None
        return lines

class HistoryFile(FileHandler):
    """Klasa pochodna od FileHandler
    Tworzy i obsługuje plik o nazwie  "History.txt"

    * Inicjalizacja:
    HistoryFile()

    * Dostępne zmienne:
    started_empty: bool - True jeśli plik został utworzony w obecnej sesji lub podczas uruchamiania plik jest pusty

    * Polecane funkcje:
    clear() - czyści plik tekstowy

    add_result(result: ResultOfCheck) - dodaje rezultat do pliku tekstowego w nowej linii

    get_history() -> Optional[List[ResultOfCheck]] - odczytuje wszystkie zapisane rezultaty i zwraca jako lista. Zwraca None jeśli plik jest pusty
    """
    def __init__(self):
        super().__init__("History.txt")

    def add_result(self, result: ResultOfCheck):
        """Funkcja dodaje rezultat do pliku tekstowego w nowej linii"""
        self.write_line(str(result))

    def get_history(self) -> Optional[List[ResultOfCheck]]:
        """Funkcja odczytuje wszystkie zapisane rezultaty i zwraca jako lista.
        Zwraca None jeśli plik jest pusty"""
        lines = self.read_lines()
        if lines is None:
            return None

        results = []
        try:
            for line in lines:
                results.append(ResultOfCheck(line))

            return results
        except:
            return None


class SettingsFile(FileHandler):
    """Klasa pochodna od FileHandler
    Tworzy i obsługuje plik o nazwie  "Settings.txt"

    * Inicjalizacja:
    SettingsFile()

    * Dostępne zmienne:
    started_empty: bool - True jeśli plik został utworzony w obecnej sesji lub podczas uruchamiania plik jest pusty

    * Polecane funkcje:
    clear() - czyści plik tekstowy

    write_settings(difficulty: int, game_mode: int) - zapisuje trudność i tryb gry

    read_settings() -> Optional[Tuple[int, int]] - odczytuje trudność i tryb gry z pliku. Zwraca None jeśli plik jest pusty
    """
    def __init__(self):
        super().__init__("Settings.txt")

    def write_settings(self, difficulty: int, game_mode: int):
        """Funkcja zapisuje trudność i tryb gry"""
        self.clear()
        self.write_line(str(difficulty) + '|' + str(game_mode) + '\n')

    def read_settings(self) -> Optional[Tuple[int, int]]:
        """Funkcja odczytuje trudność i tryb gry z pliku.
        Zwraca None jeśli plik jest pusty"""
        lines = self.read_lines()
        if lines is None:
            return None

        line = lines[0]
        line = line.strip('\n')
        line = line.strip()
        elements = line.split('|')
        return int(elements[0]), int(elements[1])

class WordsFile(FileHandler):
    """Klasa pochodna od FileHandler
        Obsługuje pliki z listami słówek/tekstów

        * Inicjalizacja:
        WordsFile(difficulty, game_mode)
        - difficulty to obecny tryb gry wybrany z klasy Difficulty
        - game_mode to obecny tryb gry wybrany z klasy GameMode

        * Polecane funkcje:
        get_random_word() -> str - zwraca zawartość przypadkowo wybranego wiersza pliku tekstowego
    """
    def __init__(self, difficulty: int, game_mode: int):
        super().__init__("teksty.txt" if game_mode == GameMode.specjalny else ("latwe_slowa.txt" if difficulty == Difficulty.easy else ("medium_difficulty.txt" if difficulty == Difficulty.medium else "Trudne słówka.txt")))

    def get_random_word(self) -> str:
        """Funkcja zwraca zawartość przypadkowo wybranego wiersza pliku tekstowego"""
        lines = self.read_lines()
        if lines is None:
            return ""
        word: str = random.choice(lines)
        word = word.strip('\n').strip()

        return word


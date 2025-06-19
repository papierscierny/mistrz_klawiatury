#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

from file_management_module.file_management import HistoryFile, SettingsFile, WordsFile
from screens_module.screens import start_screen, choose_game_mode, choose_difficulty, clear_screen, end_screen, show_word_and_check
from settings_modules.settings import GameMode, words_in_not_special_mode


def main():
    history_file = HistoryFile()
    settings_file = SettingsFile()
    game_mode: int
    difficulty: int
    words_done = 0

    if history_file.started_empty or settings_file.started_empty:
        history_file.clear()
        settings_file.clear()

        start_screen()
        game_mode = choose_game_mode()
        difficulty = choose_difficulty(game_mode)

        settings_file.write_settings(difficulty, game_mode)
    else:
        difficulty, game_mode = settings_file.read_settings()
        words_done = len(history_file.get_history())


    words_file = WordsFile(difficulty, game_mode)

    word_amount = 1 if game_mode == GameMode.specjalny else words_in_not_special_mode - words_done

    clear_screen()
    print("\nRozpoczynamy test...")
    time.sleep(2)

    for _ in range(word_amount):
        word = words_file.get_random_word()
        result = show_word_and_check(word)
        history_file.add_result(result)

    results = history_file.get_history()

    overall_time = 0.0
    all_words = 0

    for elem in results:
        overall_time += elem.time_spent
        all_words += 1

    if len(results) == 1:
        all_words = len(str(results[0]).split(' '))

    history_file.clear()
    settings_file.clear()

    end_screen(all_words, overall_time)


if __name__ == "__main__":
    main()

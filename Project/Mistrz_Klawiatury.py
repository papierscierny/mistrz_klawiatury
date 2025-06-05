import sys
import os
#funkcja odpowiedzialna za środkowanie tekstu
def txtcenter(txt):
    # Pobierz szerokość terminala
    try:
        terminal_width = os.get_terminal_size().columns
    except:
        terminal_width = 140  # Domyślna szerokość jeśli nie uda się wykryć

    d = (terminal_width - len(txt)) // 2

    #sprawdzanie czy d nie jest ujemne
    if(d < 0):
        d = 0
    # Wyświetl linię z wyliczonym wcięciem i kolorem
    print(' ' * d + txt)

#funkcja ekranu startowego
def start():

    #------------------------------NAPIS TYTUŁOWY--------------------------
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
    for i in lines:
        txtcenter("\033[32m" + i + "\033[0m")

    #-------------------------------------KONIEC NAPISU TYTYŁOWEGO--------------------------

def main():
    start()

if __name__ == "__main__":
    main()

import sys
import os
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

def main():
    start()

if __name__ == "__main__":
    main()

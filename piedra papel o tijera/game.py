from random import choice
from play import *


def run_game():
    """
    Arranca el juego
    """
    display_game()
    while another_match:
        user_play  = get_user_play()
        machine_play = random_play()
        winner = get_winner(user_play, machine_play)
        display_match(user_play, machine_play)
        display_endgame(winner, user_play)
        another_match()


def another_match():
    a = False
    while a == False:
        w = input("Quiere continuar? S/N").upper()
        if w == "S" or w == "N":
            if w == "S":
                a = True
                return True
            else: 
                print(choice(["Eres un gallina McFly", "Pues vete, aquí no te necesitamos", "Cobarde!", "Cierra la puerta al salir"]))
                a = True 
                return False
        else:
            print("Intenta otra vez")
            

def display_match(play1,play2):
    print(f"{play1.description()} vs {play2.description()} FIGHT!\n")

def display_game():
    """
    Muestra el nombre del jugador
    """
    print("\n\n\t\tPiedra Papel o Tijeras\n\n")

def get_user_response():
    """
    presenta un menu de opciones y pide que selecciones una
    Devuelve una cadena qeue indica lo que ha elegido
    """
    while True:
        print("Ingrese elección: \n1. Rock\n2. Paper 🧾\n3. Scissors ✂\n4. Lizard \n5. Spock ")
        raw = input("Enter 1, 2, 3, 4, 5: ").strip()
        if raw == "1" or raw == "2" or raw == "3" or raw == "4" or raw == "5":
            break
    return int(raw)

def get_user_play():
    """
    Le pregunta al usuario que quiere jugar y lo devuelve
    """
    res = get_user_response()
    if res == 1:
        return Rock()
    elif res == 2:
        return Paper()
    elif res == 3:
        return Scissors()
    elif res == 4:
        return Lizard()
    else:
        return Spock()

def random_play():
    """
    Selecciona una jugada al azar para competir con el usuario
    """
    return choice([Rock(), Paper(), Scissors(), Lizard(), Spock()])

def get_winner(play1, play2):
    """
    Comparamos respuestas y devolvemos ganador
    """
    return play1.compare(play2)

def display_endgame(play1, play2):
    """
    Imprime si ha habido un empate o el ganador
    """
    if play1 == None:
        print(f"EMPATE ENTRE  DOS {play2.description()}")
    else:
        print(f"Ha ganado {play1.description()}")

#def display_victory(winner):
    """
    #Muestra que winner ha ganado
    """
    #print(f"Ha ganado {winner.description()}")

if __name__ == "__main__":
    run_game()
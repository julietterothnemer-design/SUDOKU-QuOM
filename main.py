import os
from game import SudokuGame
from data_loader import load_puzzles


######### programme principal ##########

def main(): # trouver automatiquemet chemin vers data/sudoku.csv
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "data", "sudoku.csv")

    print("Chargement de la base de données...")
    puzzles = load_puzzles(csv_path, limit=10000)
    print(f"{len(puzzles)} grilles chargées.\n")

    # creation jeu
    game = SudokuGame(puzzles)

    # choix gamer
    difficulty = input("Choisissez la difficulté (easy / medium / hard) : ").strip().lower()
    if difficulty not in ("easy", "medium", "hard"):
        print("Difficulté inconnue → easy par défaut.")
        difficulty = "easy"

    mode = input("Choisissez le mode (immediate / delayed) : ").strip().lower()
    if mode not in ("immediate", "delayed"):
        print("Mode inconnu → immediate par défaut.")
        mode = "immediate"

    game.start_new_game(difficulty, mode)

    print("\nCommandes :")
    print("  Jouer      : ligne,colonne,valeur   (ex: 1,3,9)")
    print("  Effacer    : erase ligne,colonne    (ex: erase 1,3)")
    print("  Solution   : show")
    print("  Quitter    : quit\n")

    # boucle de jeu console
    while True:
        game.grid.display()

        if game.is_finished():
            print("\n Grille terminée et correcte !")
            break

        cmd = input("\n> ").strip().lower()

        if cmd == "quit":
            break

        if cmd == "show":
            game.show_solution()
            continue

        if cmd.startswith("erase"):
            try:
                _, rc = cmd.split()
                r, c = rc.split(",")
                game.erase(int(r) - 1, int(c) - 1)
            except Exception:
                print("Commande invalide. Exemple : erase 1,3")
            continue

        try:
            r, c, v = cmd.split(",")
            result = game.play_move(int(r) - 1, int(c) - 1, int(v))

            if mode == "immediate":
                if result:
                    print(" Correct")
                else:
                    print(f" Incorrect (erreurs : {game.errors})")

        except Exception:
            print("Commande invalide. Exemple : 1,3,9")

    print("\nFin du jeu.")


if __name__ == "__main__":
    main()




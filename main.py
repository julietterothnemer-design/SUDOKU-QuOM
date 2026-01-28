import os
import pandas as pd

from game import SudokuGame


def string81_to_grid(s): # transforme chaîne de 81 chiffres en grille 9x9.

    s = str(s).strip()
    if len(s) != 81:
        raise ValueError("Une grille doit contenir exactement 81 chiffres.")
    return [[int(s[i * 9 + j]) for j in range(9)] for i in range(9)]


def infer_difficulty(puzzle_str): # deduit difficulte à partir du nbre de O (cases vides)
                                  # + y a de 0, + c dur  
    zeros = puzzle_str.count("0")

    if zeros <= 40:
        return "easy"
    elif zeros <= 50:
        return "medium"
    else:
        return "hard"


def load_puzzles_from_csv(csv_path, max_grids=None):
    import pandas as pd

    df = pd.read_csv(csv_path, usecols=["quizzes", "solutions"])

    # Limite éventuelle pour accélérer
    if max_grids is not None:
        df = df.sample(n=max_grids, random_state=0)

    puzzles_temp = []

    for _, row in df.iterrows():
        puzzle_str = row["quizzes"]
        solution_str = row["solutions"]

        puzzle_grid = string81_to_grid(puzzle_str)
        solution_grid = string81_to_grid(solution_str)
        zeros = puzzle_str.count("0")

        puzzles_temp.append({
            "puzzle": puzzle_grid,
            "solution": solution_grid,
            "zeros": zeros
        })

    # Tri par nombre de zéros
    puzzles_temp.sort(key=lambda p: p["zeros"])

    n = len(puzzles_temp)
    one_third = n // 3

    puzzles = []
    for i, p in enumerate(puzzles_temp):
        if i < one_third:
            difficulty = "easy"
        elif i < 2 * one_third:
            difficulty = "medium"
        else:
            difficulty = "hard"

        puzzles.append({
            "puzzle": p["puzzle"],
            "solution": p["solution"],
            "difficulty": difficulty
        })

    return puzzles



######### programme principal ##########

def main(): # trouver automatiquemet chemin vers data/sudoku.csv
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(base_dir, "data", "sudoku.csv")

    print("Chargement de la base de données...")
    puzzles = load_puzzles_from_csv(csv_path, max_grids=5000)
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
            print("\n🎉 Grille terminée et correcte !")
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
                    print("✔ Correct")
                else:
                    print(f"❌ Incorrect (erreurs : {game.errors})")

        except Exception:
            print("Commande invalide. Exemple : 1,3,9")

    print("\nFin du jeu.")


if __name__ == "__main__":
    main()


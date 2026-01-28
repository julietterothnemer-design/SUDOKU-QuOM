# src/run_ui.py
import os
import sys

# --- Permet d'importer ui/ et src/ même si on lance depuis src/ ---
THIS_DIR = os.path.dirname(os.path.abspath(__file__))          # .../SUDOKU/src
PROJECT_ROOT = os.path.dirname(THIS_DIR)                      # .../SUDOKU
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)
if THIS_DIR not in sys.path:
    sys.path.insert(0, THIS_DIR)

from game import SudokuGame
from data_loader import load_puzzles
from ui.interface_qt import run_qt_app


def main():
    csv_path = os.path.join(PROJECT_ROOT, "data", "sudoku.csv")

    puzzles = load_puzzles(csv_path, limit=5000)
    game = SudokuGame(puzzles)

    run_qt_app(game)


if __name__ == "__main__":
    main()


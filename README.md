# SUDOKU-QuOM
Jeu de Sudoku interactif en Python utilisant la programmation orientée objet.

## Présentation
Ce projet consiste à développer un jeu de Sudoku jouable sur ordinateur.
Le joueur peut sélectionner :
- un niveau de difficulté (easy, medium, hard)
- un mode de jeu :
  - validation immédiate des coups
  - validation différée (correction à la fin)

Les grilles sont extraites d’une base de données externe (Kaggle).

## Fonctionnalités
- Sélection de la difficulté
- Deux modes de jeu (immédiat / différé)
- Possibilité de corriger ou d’effacer une case
- Affichage de la solution à tout moment
- Grilles tirées aléatoirement depuis une base de données

## Base de données
Le projet utilise le dataset Sudoku disponible sur Kaggle :
https://www.kaggle.com/datasets/bryanpark/sudoku

Le fichier `sudoku.csv` n’est pas inclus dans ce dépôt en raison de sa taille.

### Installation de la base de données
1. Télécharger le dataset depuis Kaggle
2. Extraire le fichier `sudoku.csv`
3. Créer un dossier `data/` à la racine du projet
4. Placer `sudoku.csv` dans ce dossier

## Structure du projet
QuOM---Sudoku/
├─ src/
│ ├─ main.py
│ ├─ grid.py
│ ├─ game.py
│ └─ player.py (optionnel)
├─ ui/ (interface graphique à venir)
├─ README.md

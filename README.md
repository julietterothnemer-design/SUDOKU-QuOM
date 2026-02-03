# Jeu de Sudoku – QuOM

Ce projet consiste à développer un **jeu de Sudoku interactif en Python**, en utilisant la **programmation orientée objet** et une **interface graphique Qt (PySide6)**.

---

## Objectifs du projet

- Concevoir un jeu de Sudoku jouable sur ordinateur
- Mettre en œuvre une architecture orientée objet claire et modulaire
- Séparer la logique métier du jeu et l’interface graphique
- Proposer une interface ergonomique, jouable uniquement à la souris
- Exploiter une base de données externe de grilles de Sudoku

---

## Fonctionnalités

- Sélection du niveau de difficulté : `easy`, `medium`, `hard`
- Deux modes de jeu :
  - **Immediate** : chaque coup est validé immédiatement
  - **Delayed** : les erreurs sont visibles uniquement à la fin
- Interface graphique avec :
  - grille Sudoku 9×9
  - séparation visuelle des blocs 3×3
  - sélection des cases à la souris
  - pavé de chiffres (1 à 9)
  - bouton pour effacer une case
- Bouton **« Voir la solution »** accessible à tout moment
- Possibilité de recommencer une nouvelle grille
- Détection automatique de la fin correcte du Sudoku

---

## Architecture du projet

Le projet est organisé de manière modulaire afin de faciliter la compréhension, la maintenance et les évolutions futures (nouvelle interface, changement de dataset, etc.).

SUDOKU/
│
├─ data/
│ └─ sudoku.csv # Base de données Kaggle (non incluse dans le dépôt)
│
├─ src/
│ ├─ grid.py # Classe SudokuGrid : gestion de la grille
│ ├─ game.py # Classe SudokuGame : logique du jeu
│ ├─ data_loader.py # Chargement des grilles depuis le CSV
│ └─ run_ui.py # Point d’entrée de l’interface graphique
│
│
├─ ui/
│ └─ interface_qt.py # Interface graphique Qt (PySide6)
│
└─ README.md


---

## Base de données

Le projet utilise le dataset Kaggle suivant :

**Sudoku Dataset**  
https://www.kaggle.com/datasets/bryanpark/sudoku

Chaque entrée du dataset contient :
- une grille initiale (`quizzes`) avec des zéros pour les cases vides
- la solution complète correspondante (`solutions`)

### Gestion de la difficulté

Le dataset ne fournit pas directement de niveau de difficulté.  
Une heuristique simple est utilisée :

- les grilles sont triées selon le nombre de cases vides
- elles sont ensuite réparties en trois groupes de taille équivalente :
  - `easy`
  - `medium`
  - `hard`

Ce système de classification est perfectible et pourra par exemple être remplacé ultérieurement par un dataset fournissant une notation explicite de la difficulté.

---

## Interface graphique

L’interface est développée avec **Qt via PySide6**.

Choix justifiés :
- Qt est une bibliothèque graphique robuste et largement utilisée
- PySide6 est l’interface Python officielle de Qt
- L’ergonomie permet de jouer exclusivement à la souris

L’interface comprend :
- une grille Sudoku 9×9 avec blocs 3×3 clairement identifiés
- un panneau latéral pour le choix du mode et de la difficulté
- un pavé de sélection des chiffres
- des messages de retour utilisateur

---

## Lancer le projet

### 1️. Prérequis

- Python ≥ 3.10
- Anaconda (recommandé)
- PySide6
- pandas

### 2️. Création de l’environnement (recommandé)

conda create -n sudoku-qt python=3.11
conda activate sudoku-qt
conda install -c conda-forge pyside6 pandas spyder

### 3. Installation de la base de données

- Télécharger sudoku.csv depuis Kaggle
- Créer le dossier data/ à la racine du projet
- Placer sudoku.csv dans ce dossier

### 4. Lancer l’interface graphique

Depuis la racine du projet :
python src/run_ui.py

Si vous utilisez Spyder, celui-ci doit être lancé depuis l’environnement sudoku-qt :
conda activate sudoku-qt
spyder

---

### Inspirations et ressources

Documentation officielle Qt for Python / PySide6
Dataset Kaggle – Bryan Park (Sudoku)
Projets Sudoku en Qt utilisés comme inspiration pour l’interface (sans réutilisation directe du code)
L’architecture logicielle et le moteur de jeu sont entièrement personnels.

# Connect4 CLI Game

This is a command-line implementation of the classic Connect4 game, written in Python. It supports a two-player mode where players take turns dropping their colored discs into a 7-column, 6-row vertically suspended grid.

## Features

- Two-player gameplay
- Command-line interface
- 7x6 game board
- Win detection (horizontal, vertical, and diagonal)
- Draw detection
- Input validation

## Requirements

- Python 3.x

## How to Play

1. Clone this repository or download the Python script.
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script using Python:
5. Follow the on-screen instructions to play the game.
- Players take turns entering a column number (1-7) to drop their disc.
- The game ends when a player connects four discs in a row (horizontally, vertically, or diagonally) or when the board is full (a draw).

## Game Rules

1. The game is played on a 7x6 grid.
2. Players take turns dropping their colored discs into any of the seven columns.
3. The disc will occupy the lowest available space in the chosen column.
4. The first player to form a horizontal, vertical, or diagonal line of four of their own discs wins.
5. If the entire board fills up before a player wins, the game is a draw.

## Future Improvements

- Add an AI opponent for single-player mode.
- Implement a graphical user interface (GUI).

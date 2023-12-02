# Battleship-Game-Python
A simple Battleship game implemented in Python using classes and 2D arrays. Test-driven development (TDD) approach with unit tests included

## Overview

This is a simple implementation of the classic Battleship game in Python. The game is designed as a class-based structure, providing functions for setting up the game board, playing the game, and checking game-over conditions.

## How to Play

1. Clone this repository to your local machine.
2. Run the `Battleship.py` script to start the game.
3. Follow the prompts to input row and column coordinates for your shots.
4. The game board will display hits, misses, and the location of sunk ships.
5. The game ends when all ships are sunk or when you run out of chances.
6. By default, the game has the grid size set to 10 with 5 ships
7. The user has 15 chances by default and ships are hidden.

```bash
python Battleship.py
```
## Game Legend

- `.`: Water
- `S`: Ship position
- `O`: Water that was shot with a bullet (a miss)
- `X`: Ship sunk!

## Customization

You can customize the game settings by adjusting parameters when creating a `BattleshipGame` object, such as grid size, the number of ships, and the maximum number of chances.

## Unit Tests

The project includes a set of unit tests to ensure the correctness of game logic. You can run the tests using the `unittest` module.

```bash
python test_Battleship.py

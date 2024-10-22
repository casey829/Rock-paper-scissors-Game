# Rock, Paper, Scissors Game

This is a simple command-line implementation of the classic "Rock, Paper, Scissors" game in Python. The player competes against the computer, and the game keeps track of how many rounds each has won.

## How to Play

1. The player is prompted to choose between Rock, Paper, or Scissors by typing their choice.
2. The computer randomly selects one of the three options.
3. The winner of the round is determined by the classic rules:
 . Rock beats Scissors
 . Scissors beats Paper
 . Paper beats Rock
4. The game continues until the player types Q to quit.
5. When the game ends, the total wins for both the player and the computer are displayed.

## Prerequisites
. Python 3.x

## How to Run

1. Clone or download this repository.

2. Open a terminal/command prompt.

3. Navigate to the folder where the rock_paper_scissors.py script is located.

4. Run the script with the following command:
  bash

  python rock_paper_scissors.py

5. Follow the prompts in the terminal to play the game.

## Features

1. Random computer choice: The computer's choice is randomly selected for each round.
2. User-friendly input: The player can choose between Rock, Paper, Scissors, or type "Q" to quit the game.
3. Score tracking: The game keeps track of how many rounds the player and computer have won.
4. Input validation: If the player enters an invalid choice, the game will prompt them to try again.


## Sample Gameplay

vbnet
Type Rock/ Paper/ Scissors or Q to exit the game: rock
Computer picked paper.
You lost!

Type Rock/ Paper/ Scissors or Q to exit the game: paper
Computer picked rock.
You won!

Type Rock/ Paper/ Scissors or Q to exit the game: q

You won 1 times.
The Computer won 1 times.
Goodbye!


## Game Rules
. Rock beats Scissors
. Scissors beats Paper
. Paper beats Rock

## Edge Cases
. If an invalid input is provided (e.g., misspelled "roc"), the game will prompt the user to try again without counting it as a loss.
. The game is not case-sensitive; it will accept "rock", "Rock", or "ROCK" as valid inputs.

## License
This project is open-source and free to use for educational purposes.

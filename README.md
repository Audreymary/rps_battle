# Rock, Paper, Scissors Game

Welcome to the **Rock, Paper, Scissors** game! This is a simple, yet fun, command-line game where you can challenge the computer to a series of rounds of Rock, Paper, Scissors. The game supports a **Best of 3** format, where the first player to win two out of three rounds wins the game. This project is a Python-based implementation designed to practice the use of functions, loops, conditional statements, and randomization.

## Features

- **Single-player mode**: Play against the computer.
- **Best of 3**: The game follows a "Best of 3" format. The first player to win two rounds wins the game.
- **Randomized Computer Choices**: The computer makes its move randomly.
- **Replayability**: After a game ends, you can choose to play another round.
- **Simple Interface**: The game is run through the command line and interacts with you via text-based input/output.

---

## Table of Contents

- [Introduction](#introduction)
- [Game Flow](#game-flow)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Logic](#game-logic)
- [Code Structure](#code-structure)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## Introduction

Rock, Paper, Scissors is a classic hand game usually played between two people. In this implementation, you will compete against the computer, which makes random selections of "Rock," "Paper," or "Scissors." The winner is determined by the standard rules of the game:

- **Rock** crushes **Scissors**.
- **Scissors** cuts **Paper**.
- **Paper** covers **Rock**.

The game continues until either the player or the computer wins 2 out of 3 rounds. After that, you’ll be asked if you want to play another set of rounds.

---

## Game Flow

1. **Start the Game**: You’ll start by running the game via the command line interface (CLI).
2. **Make a Move**: You will be prompted to choose between "rock", "paper", or "scissors". Simply type your choice and hit Enter.
3. **Computer Makes a Move**: The computer will randomly pick one of the three choices.
4. **Result of Round**: The game will announce the winner of the round.
5. **Best of 3**: The game is played in a "Best of 3" format. The first player to win 2 rounds wins the overall game.
6. **End of Game**: After the game ends, you will be asked if you'd like to play again.
7. **Replay or Exit**: If you decide to play again, the game will restart. If you choose to exit, the game will terminate.

---

## Installation

To run the Rock, Paper, Scissors game, follow these instructions:

### 1. Clone the Repository

Begin by cloning this repository to your local machine:

```bash
git clone https://github.com/yourusername/rock-paper-scissors.git

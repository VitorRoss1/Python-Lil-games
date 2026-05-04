# Python Mini Games Collection

A collection of terminal-based mini games developed in Python.  
This repository focuses on fundamental programming concepts, clean structure, and logical problem-solving.

---

## Overview

This project contains small standalone games implemented in Python 3. Each game is designed to reinforce core programming concepts such as:

- OOP (classes, inheritance, abstract methods, encapsulation)
- Control flow
- Input validation
- error handling
- Loops and conditionals
- Basic game logic

---

## Project Structure
Python-Lil-games/

├── A-blackJack.py

├── B-warGame.py

├── C-tictactoe.py

├── D-guessing.py

└── README.md


---

## Implemented Games

###  A) Blackjack

**File:** `S-blackjack.py`

Player vs. automated dealer with a full betting system and balance tracking across rounds.
Built around an OOP hierarchy using abstract base classes <code> Game </code> as the base, with <code> Player </code> and <code> Computer </code> as concrete implementations sharing common logic like sum calculation, card management, and result checking.

#### Key Features
- Betting system with balance validation and bust-out detection
- Hit / Stand input loop
- Automatic ace adjustment (11 → 1 to avoid bust)
- Dealer automation: hits on ≤ 17, stands on > 17
- Blackjack and bust detection with immediate payout/deduction
- Win / lose / tie / dealer bust result messages
- Full round reset and play-again prompt

#### Concepts Used
- OOP hierarchy (ABC → Game → Player/Computer)
- abstract methods as interface contracts
- @staticmethod for class-level utilities
- super().__init__() for parent state inheritance
- encapsulation of shared logic in the base class (calculate_sum, hit, clear_cards)
- method overriding,
- ace adjustment logic,
- input validation with try/except
- boolean return values as game state signals.

##### Planned for v2:
- Double Down
- Card Split
- Multiple players

###  B) War Card Game

**File:** `B-warGame.py`

A simulation of the classic card game **War**, played automatically between two players (P1 vs P2). A full 52-card deck is shuffled and split evenly. Each round, both players flip their top card — highest value wins both cards. In case of a tie, **WAR** is triggered and each player puts down 5 extra cards, with the last one deciding the outcome.

#### Key Features

- Object-oriented design with `Card`, `Deck`, and `Playaa` classes
- Full 52-card deck with suit and rank mapping to integer values
- Automatic round-by-round simulation with console output
- War mechanic: tie triggers a 5-card war sequence
- Edge case handling: player eliminated if they have fewer than 5 cards during war
- Win condition detection for both players
- Shuffle round winner cards.
- Additional Information on The Statistics of War (card game) https://www.wimpyprogrammer.com/the-statistics-of-war-the-card-game

#### Concepts Used

- OOP (classes, `__init__`, `__str__`, encapsulation)
- Dictionaries for rank-to-value mapping
- List manipulation (`.pop()`, `.append()`, `.extend()`)
- Nested `while` loops for game and war logic

---

###  C) Tic Tac Toe

**File:** `A-tictactoe.py`

A two-player command-line implementation of the classic Tic Tac Toe game.

#### Key Features

- Two-player turn-based system
- Board state management
- Win condition detection
- Draw detection
- Input validation

---

### D) Guessing Game

**File:** `B-guessing.py`

A number guessing game where the player attempts to guess a randomly generated number within a defined range.

#### Key Features

- Random number generation
- Attempt counter
- Feedback system (higher/lower hints)
- Input validation

---

## How to Run

Ensure Python 3 is installed on your system.

Navigate to the project directory and run a game:

```bash
python A-blackjack.py
python B-warGame.py
python C-tictactoe.py
python D-guessing.py
```

---

## Requirements

- Python 3.x
- No external dependencies

---

## Author

**Vítor Rossi**

Developed as part of an ongoing Python learning journey focused on strengthening programming fundamentals and practical implementation skills.


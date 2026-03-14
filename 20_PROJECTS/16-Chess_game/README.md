# Console Chess Game

A simple, object-oriented, command-line Chess game written in Python.

## Overview

This project provides the foundational structure for a functional chess game. It features a complete `Board` setup and an interactive command-line loop that takes user input to move pieces. The pieces and board are built using an Object-Oriented approach.

## Code Structure

- **`Piece` Class & Subclasses**: Contains the base `Piece` class and derived classes representing each specific piece: `King`, `Queen`, `Rook`, `Bishop`, `Knight`, and `Pawn`.
- **`Board` Class**: Initializes the standard 8x8 chess board, handles piece placement, and contains the logic for rendering the board to the console.
- **Game Loop (`main`)**: Continuously prompts the user for moves via standard notation coordinate inputs (e.g., `e2 e4`) and updates the board.

## How to Run

### Prerequisites
- Python 3.x installed on your machine.

### Execution
Navigate to the project directory in your terminal and run the main script:

```bash
python main.py
```

### Making a Move
When prompted, enter your move using the starting square and the destination square separated by a space. 
For example, to move a piece from `e2` to `e4`, type:
```
Enter your move (e.g., e2 e4): e2 e4
```

*Note: White pieces are represented by uppercase letters (e.g., `P` for Pawn, `K` for King) and Black pieces are represented by lowercase letters (e.g., `p`, `k`). Empty squares are represented by `.`.*

## Current Status & Next Steps

Currently, the project acts as a structural starting point.

**Future Enhancements / Work in Progress:**
- **Move Validation**: The `is_valid_move()` method in the base `Piece` class currently defaults to returning `False`. Each piece subclass (e.g., `Pawn`, `Knight`) needs to implement its own rule-specific validation for pieces to successfully move on the board.
- **Game State**: Functionality for detecting turns, captures, check, checkmate, castling, and en passant.
- **Input Error Validation**: Adding robust error handling for invalid input formats or out-of-bounds coordinates.

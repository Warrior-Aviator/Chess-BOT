# Chess Engine and Game

This repository contains two main components:
1. **Chess_BOT.ipynb**: A Python notebook implementing a chess engine.
2. **Chess_Game.ipynb**: A Python notebook to play a game of chess using the implemented engine.

## Chess_BOT.ipynb

This notebook includes the implementation of a chess engine that can evaluate and make moves on a chessboard. It uses the `python-chess` library and implements the following features:

- **Engine Class**: Contains methods for evaluating the board, generating moves, and deciding on the best move.
- **Evaluation Functions**: Evaluates the board based on piece values, position, and game phase.
- **Move Generation**: Generates and evaluates legal moves to find the best move for the given position.

### Key Functions and Classes

- **Engine Class**: The core of the chess engine, handling move generation and evaluation.
  - `__init__(self, board, maxDepth, color)`: Initializes the engine with the board, search depth, and color.
  - `getBestMove(self)`: Determines the best move to play.
  - `evalFunt(self)`: Evaluates the board state.
  - `openning(self)`: Evaluates the opening phase.
  - `mate(self)`: Checks for checkmate or stalemate conditions.
  - `sqResPoint(self, square)`: Evaluates the value of a piece on a given square.
  - `engine(self, candidate, depth)`: Recursively evaluates moves to a given depth.

## Chess_Game.ipynb

This notebook provides an interface to play a game of chess using the engine implemented in `Chess_BOT.ipynb`. It supports playing as either white or black against the engine.

### Key Functions and Classes

- **Main Class**: Manages the game flow and interaction between the player and the engine.
  - `__init__(self, board)`: Initializes the game with a given board state.
  - `playHumanMove(self)`: Handles moves made by the human player.
  - `playEngineMove(self, maxDepth, color)`: Executes the engine's move.
  - `startGame(self)`: Starts a new game and manages the game loop.

### How to Play

1. **Start a Game**:
   - Run the `Chess_Game.ipynb` notebook.
   - Choose your color (`b` for black, `w` for white) and set the search depth for the engine.

2. **Make Your Move**:
   - Enter your move in standard algebraic notation.
   - The engine will respond with its move.

3. **Continue Playing**:
   - The game continues until checkmate, stalemate, or draw.

4. **Reset and Start Again**:
   - The board will reset after the game ends, and you can start a new game.

## Requirements

- Python 3.x
- `python-chess` library
- Jupyter Notebook

Install the required library using pip:

```sh
pip install chess

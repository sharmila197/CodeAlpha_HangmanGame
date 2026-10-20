# 🎮 Hangman Game – Python & Streamlit

## About the Project
Hangman Game is an interactive word-guessing game developed using Python and Streamlit.

The computer randomly selects a word from a predefined list of five words. The player must guess the hidden word by selecting one letter at a time.

The player has a maximum of six incorrect guesses to find the correct word.

## Features
- Interactive web-based game interface using Streamlit.
- Random word selection from five predefined words.
- Letter selection using interactive buttons.
- Displays hidden and correctly guessed letters.
- Tracks incorrect guesses and remaining lives.
- Displays winning and losing messages.
- Play Again option to start a new game.

## Technologies Used
- Python
- Streamlit
- Random module
- Session State
- Conditional statements
- Loops and lists

## Installation

Install the required Python library:

```bash
python -m pip install streamlit
```

## How to Run

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python -m streamlit run hangamon.py
```

5. Open the local URL displayed in the terminal to play the game in your browser.

## Game Rules
1. The computer randomly selects a hidden word.
2. Select one letter at a time using the buttons.
3. Correct guesses reveal the letters in the word.
4. Incorrect guesses reduce the remaining lives.
5. Guess the complete word before losing all six lives to win the game.

## Project Structure

```text
CodeAlpha_HangmanGame/
│
├── hangamon.py
└── README.md
```

## Internship Project
This project is developed as part of the CodeAlpha Python Programming Internship.

**Author:** Sharmila Rani

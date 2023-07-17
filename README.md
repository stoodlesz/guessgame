# CLI Encryption Guessing Game

This is a simple command-line interface (CLI) program that allows you to play an encryption guessing game. You will be presented with an encrypted message, and you have to guess the encryption type used to encrypt the message.

## Prerequisites

- Python 3.x

## How to Run

1. Clone this repository to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the following command to start the game:

```bash
python guess_encryption.py
```

4. Follow the on-screen instructions to play the game.

## How to Play

1. The program will ask you to enter a message.
2. The message will be encrypted using one of the encryption types (Base64, Hexadecimal, or any other supported encryption).
3. The encrypted message will be displayed on the screen.
4. You need to guess the encryption type that was used to encrypt the message.
5. Enter your guess by selecting the corresponding number from the available options.
6. If your guess is correct, you will receive a congratulatory message.
7. If your guess is incorrect, you will see a "Game Over" message.

## Supported Encryption Types

- Base64
- Hexadecimal

## Example

```bash
Welcome to the Encryption Game!
I will encrypt a message, and you have to guess the encryption type.
Enter your message: Hello, World!
Encrypted message: SGVsbG8sIFdvcmxkIQ==
Choose from the following encryption types:

1. Base64
2. Hexadecimal
What encryption has been used here? (1-2): 1
Congratulations! You guessed it correctly.
```

Note: it will display an ascii design of "game over" if it is wrong. It should look like this:

```bash
   _____                         ____
  / ____|                       / __ \
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|

    GAME OVER! Better luck next time!
```

# guessgame

# guessgame

# guessgame
# guessgame

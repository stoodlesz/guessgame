import base64
import binascii
import random


def display_game_over():
    print(
        """
   _____                         ____                
  / ____|                       / __ \               
 | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   
                                                    
    GAME OVER! Better luck next time!                 
    """
    )


def encrypt_message(message):
    # Randomly select an encryption type
    encryption_type = random.choice(["Base64", "Hexadecimal"])

    if encryption_type == "Base64":
        encrypted_message = base64.b64encode(message.encode()).decode()
    elif encryption_type == "Hexadecimal":
        encrypted_message = binascii.hexlify(message.encode()).decode()

    return encrypted_message, encryption_type


def play_game():
    print("Welcome to the Encryption Game!")
    print("I will encrypt a message, and you have to guess the encryption type.")

    message = input("Enter your message: ")

    encrypted_message, encryption_type = encrypt_message(message)

    print("Encrypted message: {}".format(encrypted_message))

    print("Choose from the following encryption types:")
    print("1. Base64")
    print("2. Hexadecimal")

    user_guess = input("What encryption has been used here? (1-2): ")

    if user_guess == "1" and encryption_type == "Base64":
        print("Congratulations! You guessed it correctly.")
    elif user_guess == "2" and encryption_type == "Hexadecimal":
        print("Congratulations! You guessed it correctly.")
    else:
        display_game_over()


play_game()

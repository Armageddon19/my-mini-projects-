# I had many problems with this game about hangman so it's not completed by ARMAGEDDON

import random

def play_hangman():
    welcome()
    secret_word = load_secret_word()
    result = start_results(secret_word)
    number_of_letters = len(secret_word)
    number_of_chances = 7
    print(" ".join(result))
    print('The word has {} letters.'.format(number_of_letters))
    print('You have {} chances, good luck!'.format(number_of_chances))

    hanged = False
    hits = False
    errors = 0

    while not hanged and not hits:
        print('Playing')

        trying = call_for_try()

        if trying in secret_word:
            result = register_correct_try(secret_word, result, trying)
        else:
            errors += 1
            print('You made a mistake! You have {} more tries left.'.format(number_of_chances - errors))
            draw_hang(errors)

        hanged = errors == number_of_chances
        hits = "_" not in result
        print(" ".join(result))

    if hits:
        print_winner()
    else:
        print_loser(secret_word)

    print('Game over!')

def welcome():
    print('********************************')
    print('Welcome to the Hangman game! ****')
    print('********************************')

def load_secret_word():
    with open("words.txt") as file:
        words = [line.strip().upper() for line in file]

    return random.choice(words)

def start_results(word):
    return ['_' for _ in word]

def call_for_try():
    while True:
        trying = input('What is the letter? ').strip().upper()
        if len(trying) == 1 and trying.isalpha():
            return trying
        else:
            print("Invalid input. Please enter a single letter.")

def register_correct_try(secret_word, result, trying):
    for index, letter in enumerate(secret_word):
        if trying == letter:
            result[index] = trying
    return result

def print_loser(secret_word):
    print("You lose!!!")
    print("The secret word was {}".format(secret_word))
    print("""
    _______________
   /               \\
  /                 \\
//                   \\/
\|   XXXX     XXXX   | /
 |   XXXX     XXXX   |/
 |   XXX       XXX   |
 |                   |
 \__      XXX      __/
   |\     XXX     /|
   | |           | |
   | I I I I I I I |
   |  I I I I I I  |
   \_             _/
     \_         _/
       \_______/
    """)

def print_winner():
    print("Congratulations, you win!")
    print("""
       ___________
      '._==_==_=_.'
      .-\\:      /-.
     | (|:.     |) |
      '-|:.     |-'
        \\::.    /
         '::. .'
           ) (
         _.' '._
        '-------'
    """)

def draw_hang(errors):
    stages = ["""
        _______
       |/      |
       |      (_)
       |            
       |            
       |           
      _|___        
    """,
    """
        _______
       |/      |
       |      (_)
       |      \   
       |            
       |           
      _|___        
    """,
    """
        _______
       |/      |
       |      (_)
       |      \|   
       |            
       |           
      _|___        
    """,
    """
        _______
       |/      |
       |      (_)
       |      \|/   
       |            
       |           
      _|___        
    """,
    """
        _______
       |/      |
       |      (_)
       |      \|/   
       |       |    
       |           
      _|___        
    """,
    """
        _______
       |/      |
       |      (_)
       |      \|/   
       |       |    
       |      /     
      _|___        
    """,
    """
        _______
       |/      |
       |      (_)
       |      \|/   
       |       |    
       |      / \   
      _|___        
    """]
    print(stages[errors])

if __name__ == '__main__':
    play_hangman()

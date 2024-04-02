    
# # Jai Strbik
# # Connections Clone v1.0 

import random 
from time import sleep
from sys import stdout

def create_word_grid(): 
    '''
    Create a 4x4 grid with a word as a placeholder in each cell
    '''
    grid_size = 4 # Define the size of the grid
    word_grid = []
    
    for _ in range(grid_size):
        row = ["Word"] * grid_size # Fill out each row with 4 placeholder words from connections
        word_grid.append(row)
    return word_grid

# Define connections from dictionary
connections = [
    {"Category": "Cars", "Words": ["Ferrari", "Porsche", "Ford", "Jeep"]},
    {"Category": "Crazy", "Words": ["mad", "passionate", "nuts", "bananas"]},
    {"Category": "Evil", "Words": ["devious", "wicked", "ungodly", "naughty"]},
    {"Category": "Alpha", "Words": ["leader", "drive", "dominant", "confident"]},
    {"Category": "Beta", "Words": ["weak", "submissive", "lone_wolf", "passive"]},
    {"Category": "Camera_Brands", "Words": ["fujifilm", "hassleblad", "olympus", "polaroid"]},
    {"Category": "Falsify", "Words": ["fabricate", "fake", "fix", "forge"]},
    {"Category": "Nato_Alphabet", "Words": ["Tango", "Alpha", "Papa", "Oscar"]}
]

def fill_word_grid(grid, connections):   
    '''
    Fill the word grid with words from connections
    '''
    random_connections = random.sample(connections, 4) # Randomly select 4 connections
    
    row = 0 
    for connection in random_connections: #Randomise it
        random.shuffle(connection["Words"]) # Shuffle words in each connection
        col = 0
        for word in connection["Words"]: #within the lists, get each word.
            grid[row][col] = word #put the words into the grid reference
            col += 1 #moves to next column
        row += 1  #move into next row

def print_word_grid(grid, guessed_words):
    '''
    Print the word grid with outlines
    '''
    print("----" * 13 + "-") # Length of top line
    for row in grid:
        print("|", end=" ")  #Printing the outline
        for cell in row:
            if cell.lower() in guessed_words:
                print("\033[92m" + cell.center(10) + "\033[0m", end=" | ")  #Printing the sides in green for correctly guessed words
            else:
                print(cell.center(10), end=" | ")  #Printing the sides
        print()
        print("----" * 13 + "-") # Horizontal lines

def get_guess():
    guessed_words = input("Guess 4 connected words from any category separated by commas: ").lower().split(',') #Guess 4 words each with commas inbetween
    return guessed_words

def check_guess(guessed_words, connections, lives):
    for connection in connections: 
        if set(guessed_words) == set(connection["Words"]): #If your guess equals a connection
            print(f"Good job! You guessed a category. The link for the category is: {connection['Category']}") #You are right
            return True, lives 
    print("WRONG, That's not a category!")
    remaining_lives = lives - 1  #If you incorrectly guess a connection, lives - 1 
    print(f"You have {remaining_lives} guesses remaining.") #Print Remaining lives
    if lives == 0:
        print("You are out of guesses, YOU LOSE in Pythonic Connect - The correct connections were:")
        for connection in connections:
            print(connection['Category'], connection['Words'])

    return False, lives

def typewriter_effect(text): #Adds an effect to printed text
    for character in text:
        stdout.write(character)
        stdout.flush()
        sleep(0.02)

# Main
typewriter_effect("\033[1;37m Welcome To Connections\033[0m") 
print() # So grid doesn't interfere with typewriter
typewriter_effect("\033[1;37m You have four guesses to match four words to a connection\033[0m") 
print() # So grid doesn't interfere with typewriter
typewriter_effect("\033[1;37m Good luck!\033[0m")
print() # So grid doesn't interfere with typewriter

grid = create_word_grid()
fill_word_grid(grid, connections)

lives = 4
guessed_words = []

while lives > 0:
    print_word_grid(grid, guessed_words)
    guessed_words = get_guess()
    guess_correct, lives = check_guess(guessed_words, connections, lives)

    #HOw do i make it so the grid stops looping
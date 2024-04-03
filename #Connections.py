    
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
    
    # before you feed them into the grid, you need to make them into a long list, then put them into the grid

    row_one = random_connections[0]["Words"]
    row_two = random_connections[1]["Words"]
    row_three = random_connections[2]["Words"]
    row_four = random_connections[3]["Words"]
    combined = row_one+row_two+row_three+row_four
    random.shuffle(combined)
    # print(combined)

    grid = [[],
            [],
            [],
            []]
    
    grid[0].append(combined[0])
    grid[0].append(combined[1])
    grid[0].append(combined[2])
    grid[0].append(combined[3])
    grid[1].append(combined[4])
    grid[1].append(combined[5])
    grid[1].append(combined[6])
    grid[1].append(combined[7])
    grid[2].append(combined[8])
    grid[2].append(combined[9])
    grid[2].append(combined[10])
    grid[2].append(combined[11])
    grid[3].append(combined[12])
    grid[3].append(combined[13])
    grid[3].append(combined[14])
    grid[3].append(combined[15])


    return grid


def print_word_grid(grid, guessed_words):
    '''
    Print the word grid with outlines
    '''
    print("----" * 13 + "-") # Length of top line
    for row in grid:
        print("|", end=" ")  #Printing the outline
        for cell in row:
            if cell in guessed_words:
                print("\033[92m" + cell.center(10) + "\033[0m", end=" | ")  #Printing the sides in green for correctly guessed words
            else:
                print(cell.center(10), end=" | ")  #Printing the sides
        print()
        print("----" * 13 + "-") # Horizontal lines

def get_guess():
    guessed_words = input("Guess 4 connected words from any category separated by commas: EG: fake,forge... ").split(',') #Guess 4 words each with commas inbetween
    return guessed_words

def check_guess(guessed_words, connections, lives, guessed_count):
    correct = False
    print(guessed_words)
    for connection in connections: 
        if set(guessed_words) == set(connection["Words"]): #If your guess equals a connection
            correct = True
            print(f"Good job! You guessed a category. The link for the category is: {connection['Category']}") #You are right
            guessed_count += 1
            print(f"You have guessed {guessed_count} categories out of 4")
            
            return True, lives, guessed_count 
            
    if correct == False:
    
        print("Incorrect, That's not a category!")
        lives = lives - 1  #If you incorrectly guess a connection, lives - 1      
        
        print(f"You have {lives} guesses remaining.") #Print Remaining lives
    if lives == 0:
        print("You are out of guesses, YOU LOSE in Pythonic Connect - The correct connections were:")
        for connection in connections:
            print(connection['Category'], connection['Words'])   #ALL THE CONNECTIONS PRINT NOT WORDS IN THE GRID

    return False, lives, guessed_count

def typewriter_effect(text): #Adds an effect to printed text
    for character in text:
        stdout.write(character)
        stdout.flush()
        sleep(0.02)

#Main
typewriter_effect("\033[1;37m Welcome To Connections\033[0m") 
print() # So grid doesn't interfere with typewriter
typewriter_effect("\033[1;37m You have four guesses to match four words to a connection\033[0m") 
print() # So grid doesn't interfere with typewriter
typewriter_effect("\033[1;37m Good luck!\033[0m")
print() # So grid doesn't interfere with typewriter

grid = create_word_grid()
grid = fill_word_grid(grid, connections)




guessed_count = 0
lives = 4
guessed_words = []
won = False

while lives > 0 and won == False:
    print_word_grid(grid, guessed_words)
    guessed_words = get_guess()
    guess_correct, lives, guessed_count = check_guess(guessed_words, connections, lives, guessed_count)
    if guessed_count == 4:
        won = True
    

if won == True:
    print("CONGRATIONLATION!! YOU BEAT PYTHONIC CONNECT!!")
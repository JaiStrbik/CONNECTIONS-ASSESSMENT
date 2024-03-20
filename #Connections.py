




#Connections

import random 
def create_word_grid(): 
    '''
    Create a 4x4 grid with a word as a placeholder in each cell
    '''
    grid_size = 4  # Define the size of the grid
    word_grid = []
    
    for _ in range(grid_size):
        row = ["Word"] * grid_size  # Fill out each row with 4 placeholder words from connections
        word_grid.append(row)
    return word_grid

# Define connections from dictionary
connections =  [
    {"Category": "Cars", "Words": ["Ferrari", "Porsche", "Ford", "Jeep"]},
    {"Category": "Crazy", "Words": ["mad", "passionate", "nuts", "bananas"]},
    {"Category": "Evil", "Words": ["devious", "wicked", "ungodly", "naughty"]},
    {"Category": "Alpha", "Words": ["leader", "drive", "dominant", "confident"]},
    {"Category": "Beta", "Words": ["weak", "submissive", "lone_wolf", "passive"]},
    {"Category": "Camera_Brands", "Words": ["FUJIFILM", "HASSELBLAD", "OLYMPUS", "POLAROID"]},
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
        random.shuffle(connection["Words"])  # Shuffle words in each connection
        col = 0
        for word in connection["Words"]: #within the lists, get each word.
            grid[row][col] = word #put the words into the grid reference
            col += 1 #moves to next column
        row += 1  #move into next row

def print_word_grid(grid): #print the word grid
    '''
    Print the word grid
    '''
    for row in grid:  #Print rows
        print(row)

# Test the functions
word_grid = create_word_grid()
fill_word_grid(word_grid, connections)
print_word_grid(word_grid)












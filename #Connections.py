




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
    {"Category": "Cars", "Words": ["Ferrari1", "Porsche1", "Ford1", "Jeep1"]},
    {"Category": "Crazy", "Words": ["mad2", "passionate2", "nuts2", "bananas2"]},
    {"Category": "Evil", "Words": ["devious3", "wicked3", "ungodly3", "naughty3"]},
    {"Category": "Alpha", "Words": ["leader4", "drive4", "dominant4", "confident4"]},
    {"Category": "Beta", "Words": ["weak5", "submissive5", "lone_wolf5", "passive5"]},
    {"Category": "Camera_Brands", "Words": ["fujifilm6", "hassleblad6", "olympus6", "polaroid6"]},
    {"Category": "Falsify", "Words": ["fabricate7", "fake7", "fix7", "forge7"]},
    {"Category": "Nato_Alphabet", "Words": ["Tango8", "Alpha8", "Papa8", "Oscar8"]}
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

def print_word_grid(grid):
    '''
    Print the word grid with outlines
    '''
    print("----" * 13 + "-")  # Length of top line
    for row in grid:
        print("|", end=" ")  #Printing the outline
        for cell in row:
            print(cell.center(10), end=" | ") #Printing the sides
        print()
        print("----" * 13 + "-")  # Horizontal line



# Test the functions
word_grid = create_word_grid()
fill_word_grid(word_grid, connections)
print_word_grid(word_grid)



def get_user_guesses():
    """Prompt the user for four guesses and return these as a list."""
    print("Getting user guesses...")
    return ["word1", "word2", "word3", "word4"]
#guess = []
#for i in range

#def Play_Again():
    #if Play_Again = True 
    #else: 
        #print("Hope youy enjoyed Pythonic Connect game please play agian in the future")


def check_guesses(guesses, connections):
    """Check if the user's guesses form a valid group."""
    for category, word in zip(connections, guesses): #Zip = part of the whole word list of connnections
        if word not in category['Words']: #If it's wrong
            return False  #Lose a Life
    return True # Keep on guessing connections
    
def main():
    Lives_Remaining = 4 

    ##while Lives_Remaining > 0:
        #guesses = get_user_guesses 
        #if check_guesses(guesses, connections): True
        #print("Correct Connection") 
    #else:
            #Lives_Remaining - 1 
            #print("You have int(Lives_Remaining)")
    #else: print("Game Over you suck at Pythonic Connect"), print("Do you want to play again")
    #if True 
    #else:
        #print("Hope you enjoyed my game Pythonic Connection, please play agina soon")
         

print("Welcome To Connctions")
print("You have four guesses to match four words to a connection")
print("Goodluck!")



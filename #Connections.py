#Connection


#Outer loop designed to loop through rows
def create_word_grid(): 
    '''
    #Create a 4x4 grid with a word as a placeholder in each cell
    '''
    grid_size = [
    ["Word", "Word", "Word", "Word"],    #Building the structure of the grid
    ["Word", "Word", "Word", "Word"],
    ["Word", "Word", "Word", "Word"],
    ["Word", "Word", "Word", "Word"],
    ]
    word_grid = []
    
    for _ in range(grid_size):
        row = ["Word"] * 4  #Fill out each row with 4 placeholder words
        word_grid.append(row)
    return word_grid

# Need to work on getting the words into the grid
#Define connections 
connections = [
    {"Connecting Word": "Crazy", "Words": ["mad","passionate", "nuts", "bananas"]},   
    {"Connecting Word": "Evil", "Words": ["devious", "wicked", "ungodly", "naughty"]},
    {"Connecting Word": "Alpha", "Words": ["leader", "drive", "dominant", "Confident"]},
    {"Connecting Word": "Beta", "Words": ["weak", "submissive", "lone_wolf", "passive"]},
]


def fill_word_grid(grid, connections):   
    '''
    #Fill the word grid with the connections from above
    '''
    row = 0 

    for connection in connections: 
        col=0
        for word in connection["Words"]: #within th dictionary, get each word
            grid[row][col] = word      #put the word into the grid reference
            col += 1 #moves to next column
        row += 1 #move into next row


def print_word_grid(grid):    #Print the word grid
    
    '''
    Print the word grid
    '''

    for row in grid:
        print(row)















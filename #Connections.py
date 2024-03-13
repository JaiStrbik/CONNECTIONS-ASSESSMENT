#Connections


#Word Categories and for future Dictionary

def print_words_from_categories(word_categories):
    """
    Loop through each category to print its words
    """
    for category in word_categories:
        for word in category['words']:
            print(word)
def setup_word_categories():
    """
    Initialize a list to store different categories of words and define each category with a descriptive name and a list of related words.
    """
    word_categories = []
    

    crazy_category = {
    "Linking_word" : "crazy",
    "words" : ["mad", "passionate", "nuts", "bananas"]
    }
    evil_category = {
    "Linking_word" : "evil",
    "words" : ["devious", "wicked", "ungodly", "naughty"]
    }
    alpha_category = {
    "Linking_word" : "alpha",
    "words" : ["leader", "drive", "dominant", "Confident"]
    }
    beta_category = {
    "Linking_word" : "beta",
    "words" : ["weak", "submissive", "lone_wolf", "passive"]
    }

    word_categories.append(crazy_category)
    word_categories.append(evil_category)
    word_categories.append(alpha_category)
    word_categories.append(beta_category)

    return word_categories



#WORD GRID

def create_word_grid():
    """
    Create a 4x4 grid with a placeholder word in each cell.
    """
    grid_size = 4
    word_grid = []

    for _ in range(grid_size):
        row = []
        for _ in range(grid_size):
            row.append('word')
        word_grid.append(row)
    return word_grid

def fill_word_grid():
    """
    Placeholder function to later populate the grid with words from categories. This could include random selection and placemnt of words.
    """
    pass

#Create the word grid and setup word categories

word_grid = create_word_grid()
word_categories = setup_word_categories()

#Print words from each category
print_words_from_categories(word_categories)

#Making the GRid


grid = [
    ["Word", "Word", "Word", "Word"],    #Building the structure of the grid
    ["Word", "Word", "Word", "Word"],
    ["Word", "Word", "Word", "Word"],
    ["Word", "Word", "Word", "Word"],
]
connections = [
    {"Connecting Word": "Crazy", "Words": ["mad","passionate", "nuts", "bananas"]},   
    {"Connecting Word": "Evil", "Words": ["devious", "wicked", "ungodly", "naughty"]},
    {"Connecting Word": "Alpha", "Words": ["leader", "drive", "dominant", "Confident"]},
    {"Connecting Word": "Beta", "Words": ["weak", "submissive", "lone_wolf", "passive"]},
]

#Outer loop designed to loop through rows




row = 0 

for connection in connections: # for each of the connections, access the dictinary
    col=0
    for word in connection["Words"]: #within th dictionary, get each word
        grid[row][col] = word #put the word into the grid reference
        col = col + 1 #moves to next column
    row = row + 1 #move into next row
print(grid)

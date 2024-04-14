################################
# Chimi Dorji
# 1. Electrical
# 02230059
################################
# REFERENCES
# @DQ-Logo
# @Blackbox.ai
################################
# SOLUTION
# Your Solution Score:47075
# CSF101_CAP/input_9_cap1.txt
################################# Examine the file input.txt.
def read_input(Input_your_file_name): # We ought to define the "read_input" function.
    a = [] # We must make a blank list.
    with open(Input_your_file_name, 'r') as files: # For each line in the document
        for b in files: # Using whitespace as the delimiter, divide the lines into two halves.
            opposition_picked, outcome = b.split() # The next step is to combine the two components into a tuple and add it to the list above.
            a.append((opposition_picked, outcome)) # and add a tuple to the list that contains the values of "opposition picked" and "outcome."
    return a # return the list with "opposition_picked" and "outcome" after that.
# figuring out the points for every round or game
def calculate_score(Overall_Games_Played): # "Overall_Games_Played" should be the basis for scoring calculations.
    Point = 0 # Let the beginning position for each round be zero.
    for opposition_picked, outcome in Overall_Games_Played: #  Iterate each game in "Overall_Games_Played"
#revealing the values of "opposition_picked" and "outcome"
        if outcome == 'X':  # We must Experience Loss
            if opposition_picked == 'A': # When the Defendant selected Rock
                Point += 3 #  If Rock wins over the Scissor
            elif opposition_picked == 'B': #When the Defendant selected paper
                Point += 1  #Should paper vanquish the Rock
            elif opposition_picked == 'C': # When the Rival Selected Scissors
                Point += 2 # In the event that scissors defeat paper
        elif outcome == 'Y':  # We must create a draw.
            if opposition_picked == 'A': # someone selected Rock
                Point += 4  # When the Rock concedes a draw to the Rock
            elif opposition_picked == 'B': # when the individual selects Paper
                Point += 5  # As soon as the paper draws against itself
            elif opposition_picked == 'C': # Someone selected scissors
                Point += 6  # When Scissors declare a draw with Scissors
        elif outcome == 'Z':  # We must prevail.
            if opposition_picked == 'A': # when the Individual Selects Rock
                Point += 8  # When Rock is defeated by the Paper
            elif opposition_picked == 'B': # when the individual selects Paper
                Point+= 9 # when Scissors triumph over Paper
            elif opposition_picked == 'C': # When an individual choose scissors
                Point += 7 # when Scissor loses to Rock
    print(f"The final accumulation of points is:{Point}") # When publishing the input file's total sum of the points
# Upon launching the software
Input_your_file_name = "input_9_cap1.txt"  # assign the pupils a distinct, well-respected Index Number
calculate_score(read_input(Input_your_file_name)) # Using the information gleaned from reading the input file, we now calculate the score

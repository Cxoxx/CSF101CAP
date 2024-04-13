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
################################# Read the input.txt file
def read_input(Input_your_file_name): # We should define a fucntion "read_input"
    a = [] # We have to create an empty list
    with open(Input_your_file_name, 'r') as files: # For every line in the file
        for b in files: # Split the lines into two parts using whitespace as the delimiter
            opposition_picked, outcome = b.split() # Now we have to Create a tuple containing the two parts and append it to the above list
            a.append((opposition_picked, outcome)) # and create a tuple containing the values of 'opposition_picked' and 'outcome', and append it to the list
    return a # after that return the list containing 'opposition_picked' and 'outcome'

# Calculating the point for each game/round
def calculate_score(Overall_Games_Played): # scores should be calculated based on "Overall_Games_Played"
    Point = 0 # let the starting point  for each round be 0
    for opposition_picked, outcome in Overall_Games_Played: # Iterate through each game in "Overall_Games_Played" 
# and reveal the values of "opposition_picked" and "outcome"
        if outcome == 'X':  # We need to "LOSE"
            if opposition_picked == 'A': # When the Opponent chose Rock
                Point += 3 #  If the Scissor is defeated by Rock
            elif opposition_picked == 'B': #When the Opponent chose Paper
                Point += 1  #If the Rock is defeated by paper
            elif opposition_picked == 'C': # when the Opponent chose Scissors
                Point += 2 #If Paper is defeated by Scissors
        elif outcome == 'Y':  # We need to produce a "DRAW"
            if opposition_picked == 'A': # person choose Rock
                Point += 4  #When the Rock gives draw against Rock
            elif opposition_picked == 'B': # when the person choose Paper
                Point += 5  #When the Paper gives draw against Paper
            elif opposition_picked == 'C': # Person choose Scissors
                Point += 6  # When the Scissors gives draw against Scissors
        elif outcome == 'Z':  # We need to "WIN"
            if opposition_picked == 'A': # when the Person choose Rock
                Point += 8  # When the Paper wins against Rock
            elif opposition_picked == 'B': # when the person choose Paper
                Point+= 9 # when the Scissors wins against Paper
            elif opposition_picked == 'C': #When the Person choose Scissors
                Point += 7 # when Rock wins against Scissor
    print(f"The final accumulation of points is:{Point}") #when printing out the total sum of the points from the input file

# when we run the program
Input_your_file_name = "CSF101CAP/input_9_cap1.txt"  # give the unique respected Index Number for the students
calculate_score(read_input(Input_your_file_name)) #now we Calculate the score using the data obtained from reading the input file

#########################################################################
# name: Brandon Fortes
# date: October 18, 2023
# description:
#########################################################################

# A function to prompt the user for the number of levels that their
# pyramid will have and return it to the calling statement.
def getPyramidLayers():
    return int(input("How many levels will your pyramid have? "))

# A function that receives the number of pyramid levels and the number
# of blocks as arguments, and prints the appropriate results to the
# screen.
def displayResults(numOfLayers, numOfBlocks):
    print(f"For {numOfLayers} levels, you will need {numOfBlocks} blocks")

# A recursive function that receives the number of the level, calculates
# the number of blocks required, and returns the result to the calling
# statement.
def calculateRequiredBlocks(numOfLayers):
    blocks = 0
    if (numOfLayers > 0):
        blocks = (numOfLayers ** 2) + calculateRequiredBlocks(numOfLayers - 1)
    return blocks

################################ MAIN ################################
# using the function(s) defined above, ask the user for the number of
# pyramid levels

# using the function(s) defined above, calculate and display the final results
layers = getPyramidLayers()
displayResults(layers, calculateRequiredBlocks(layers))
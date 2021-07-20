# This file is for displaying the set of the Mahjon tiles which the users have!
TILES_NUMBER = 17
ADDIT_NUMBER = 8
def display_board(arr, addition):
    """ This function is directly draw the board.

    Args:
        arr ([string]): An array that the user has.
    """
    # Firstly, we want to check if the passing arrays are in correct numbers. 
    if len(arr) != TILES_NUMBER or len(addition) > ADDIT_NUMBER:
        print("FALSE INPUT")
        return 

    # Print the additional tiles first
    print("-----  " * len(addition))
    upp_string = ""
    low_string = ""
    for i in range(len(addition)):
        upp_string += "| " + addition[i][0] + " | "
        low_string += "|    | "
    print(upp_string)
    print(low_string)
    print("-----  " * len(addition))

    # Print the actual set of tiles
    print("-----  " * TILES_NUMBER)
    upp_string = ""
    low_string = ""
    for i in range(len(arr)):
        upp_string += "| " + arr[i][0] + " | "
        low_string += "| " + arr[i][1] + " | "
    print(upp_string)
    print(low_string)
    print("-----  " * TILES_NUMBER)
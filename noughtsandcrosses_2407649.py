"""
Name: Bikash Shrestha
University ID: 2407649
"""

import random
import os.path
import json
random.seed()

def draw_board(board):
    """
    Draw the Noughts and Crosses board.

    Parameters:
    - board (list): A 2D list representing the Noughts and Crosses board.
                    It should have exactly 3 rows,
                    and each row should have the same length of 3.

    Raises:
    - ValueError: If the board is empty, has an invalid format,
                  or doesn't meet the size requirements.
                  
    - NameError: If the 'draw_board' function is called without a valid 'board' parameter.

    Returns:
    None

    """
    try:
        # Check if the board is not empty
        if not board:
            raise ValueError("Invalid board format")
        if len(board)!= 3:
            raise ValueError("Invalid board format: It should have exactly 3 rows.")
        # Check if all row have the same length of 3
        row_length = 3
        for row in board:
            if len(row) != row_length:
                raise ValueError("Invalid board format: All row should have same length of 3.")
        # Draw the board
        for row in board:
            print("\t"+" " + "-" * 11)
            print("\t"+"| " + " | ".join(row) + " |")
        print("\t"+" " + "-" * 11)

    except ValueError as e:
        print(f"Error: {e}")
        print("Unable to draw the board due to invalid format.")
    except NameError as e:
        print(f"Error: {e}")

def welcome(board):
    """
    Display the welcome message and game instructions.

    Prints the welcome message for the "Unbeatable Noughts and Crosses" game.
    It also displays the initial game board and provides instructions to the player.

    Parameters:
    - board (list): A 2D list representing the Noughts and Crosses board.
                    It should have exactly 3 rows,
                    and each row should have the same length of 3.

    Raises:
    - NameError: If the 'draw_board' function is not defined.

    Returns:
    None

    """
    try:
        # Prints the Welcome Message
        print('Welcome to the "Unbeatable Noughts and Crosses" game.')
        print("The board layout is shown below:")
        # Display the board
        draw_board(board)
        print("When prompted, enter the number corresponding to the square you want.")

    except NameError as e:
        print(f"Error: {e}")

def initialise_board(board):
    """
    Initialize the Nought and Crosses board by setting all elements to one space " ".

    Parameters:
    - board (list): A 2D list representing the Noughts and Crosses board.
                    It should have exactly 3 rows,
                    and each row should have the same length of 3.

    Raises:
    - NameError: If 'board' is not defined in the current scope.
    - IndexError: If there is an issue accessing elements in 'board'.

    Returns:
    - board (list): A 2D list representing the initialized Noughts and Crosses board.
                    Returns None if there is an error (NameError or IndexError).
    
    """
    try:
        #Set all elements of the board to one space " "
        for row in range(3):
            for col in range(3):
                board[row][col] = " "
        return board

    except (NameError, IndexError) as e:
        print(f"Error: {e}")
        return None

def get_player_move(board):
    """
    Prompt the user to select a cell on the Noughts and Crosses board for their move.

    Parameters:
    - board (list): A 2D list representing the Noughts and Crosses board.
                    It should have exactly 3 rows,
                    and each row should have the same length of 3.
    
    Raises:
    - ValueError: If the user inputs a number outside the range 1 to 9 or a non-integer value.
    - NameError: If there is an issue with the variable 'board'.
    - TypeError: If there is a type mismatch during the input processing.

    Returns:
    - tuple: A tuple (row, col) representing the selected cell.

    """
    while True:
        try:
            #Prompt the user to select the cell to put 'X' from 1 to 9
            print(" "*20,end="")
            print("1 2 3")
            print(" "*20,end="")
            print("4 5 6")
            cell = int(input("Choose your square: 7 8 9 : "))
            if 1 <= cell <= 9:
                row = (cell - 1) //3
                col = (cell - 1) % 3
                # Check if the cell is empty or already selected
                if board[row][col] == " ":
                    return row, col

                print("Error: The choosen cell is already filled. Please choose an empty cell.")
            else:
                print("Error: Invalid Input. Please choose a number from 1 to 9.")

        except ValueError:
            print("Error: Invalid Input. Please choose a number from 1 to 9.")

        except (NameError, TypeError) as e:
            print(f"Error: {e}")

def choose_computer_move(board):
    """
    Choose a random empty cell on the Noughts and Crosses board.

    Parameters:
    - board (list): A 2D list representing the Noughts and Crosses board.
                    It should have exactly 3 rows,
                    and each row should have the same length of 3.
    Raises:
    - NameError: If there is an issue with the variable 'board'.
    - TypeError: If there is a type mismatch during the input processing.
    - IndexError: If there is an issue accessing elements in 'board'.
    
    Returns:
    - tuple: A tuple (row, col) representing the indices of the randomly chosen empty cell.
             Returns None if there are no empty cells on the board or if there is an error.

    """
    try:
        # Initialize an empty cell to append all the empty cell available
        empty_cell = []
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    empty_cell.append((row,col))

        # Check whether there is empty cell or not,if empty cell then choose randomly
        if empty_cell:
            row, col = random.choice(empty_cell)
            return row, col

        raise ValueError("There are no empty cells on the board")

    except (NameError, TypeError, IndexError, ValueError) as e:
        print(f"Error: {e}")
        return None

def check_for_win(board, mark):
    """
    Check if either the player or the computer has won in the Noughts and Crosses game.

    Parameters:
    - board (list): A 2D list representing the Noughts and Crosses board.
                    It should have exactly 3 rows,
                    and each row should have the same length of 3.
    - mark (str): The player or computer's mark ('X' or 'O') to check for a win.
    
    Raises:
    - NameError: If there is an issue with the variable 'board' or 'mark'.
    - TypeError: If there is a type mismatch during the input processing.
    - IndexError: If there is an issue accessing elements in 'board'.
    
    Returns:
    - bool: True if either the player or the computer has won, False otherwise.

    """
    try:
        # Check if either the player or the computer has won

        # Check rows if either the player or the computer has won
        if any(all(cell == mark for cell in row) for row in board):
            return True

        # Check columns if either the player or the computer has won

        if any(all(row[col] == mark for row in board) for col in range(3)):
            return True

        # Check both diagonals if either the player or the computer has won

        if all(board[i][i] == mark for i in range(3)):
            return True

        if all(board[i][2-i] == mark for i in range(3)):
            return True

        return False

    except (NameError, TypeError, IndexError) as e:
        print(f"Error: {e}")
        return None

def check_for_draw(board):
    """
    Check if the Noughts and Crosses game has ended in a draw.

    Parameters:
    - board (list): A 2D list representing the Noughts and Crosses board.
                    It should have exactly 3 rows,
                    and each row should have the same length of 3.
    
    Raises:
    - NameError: If there is an issue with the variable 'board'.
    - TypeError: If there is a type mismatch during the input processing.
    - IndexError: If there is an issue accessing elements in 'board'.
    
    Returns:
    - bool: True if the game has ended in a draw (all cells occupied), False otherwise.

    """
    # Check if all cells are occupied to check for draw
    try:
        for row in range(3):
            for col in range(3):
                if board[row][col] == " ":
                    return False
        return True

    except (NameError, TypeError, IndexError) as e:
        print(f"Error: {e}")
        return None

def play_game(board):
    """
    Play the Noughts and Crosses game.

    Parameters:
    - board (list): A 2D list representing the Noughts and Crosses board.
                    It should have exactly 3 rows,
                    and each row should have the same length of 3.
 
    Raises:
    - NameError: If there is an issue with the variable 'board'.
    - IndexError: If there is an issue accessing elements in 'board'.
    - ValueError: If there is an invalid value encountered during the game.
    - TypeError: If there is a type mismatch during the input processing.

    Returns:
    - int: 1 if the player wins, -1 if the computer wins, 0 if the game ends in a draw.
    
    """
    try:
        # Call initialise_board(board) functioin to set the board cell to single spaces " "
        # then, draw the board
        initialise_board(board)
        draw_board(board)

        while True:
            # Prompt the player to move, then update and draw the board again.
            row, col = get_player_move(board)
            board[row][col] = "X"
            draw_board(board)

            # Check if the player has won or not
            result = check_for_win(board,"X")
            if result:
                print("Congratulations! You won!")
                return 1

            # Check if the game has drawn or not
            result = check_for_draw(board)
            if result:
                print("The game is a draw! It's a tie.")
                return 0

            # Prompt the computer to move, then update and draw the board again
            row, col = choose_computer_move(board)
            cell = row * 3 + col + 1
            board[row][col] = "O"
            draw_board(board)
            print(f"The computer has choosen the cell {cell}")

            # Check if the computer has won or not
            result = check_for_win(board, "O")
            if result:
                print("Sorry, the computer won. Better luck next time!")
                return -1

            #Check if the game has drawn or not
            result = check_for_draw(board)
            if result:
                return 0

    except (NameError, IndexError, ValueError, TypeError) as e:
        print(f"Error: {e}")
        return None


def menu():
    """
    Display a menu for the Noughts and Crosses game.

    Parameters:
    None

    Raises:
    - NameError: If there is an issue with the variable 'choice'.
    - ValueError: If the user enters an invalid choice.

    Returns:
    - str: The user's choice, which can be '1', '2', '3', or 'q'.

    """
    while True:
        try:
            # Prompt the user to pick either '1', '2', '3' or 'q'
            print("Enter one of following options: ")
            print("        1 - Play the game")
            print("        2 - Save your score in the leaderboard")
            print("        3 - Load and display the leaderboard")
            print("        q - End the program")
            choice = input("1, 2, 3 or q? ")
            # Check either the user pick from the following options or not
            if choice not in ["1", "2", "3", "q"]:
                raise ValueError("Invalid choice. Please enter 1, 2, 3, or q")
            return choice
        except (NameError, ValueError) as e:
            print(f"Error: {e}")

def load_scores():
    """
    Load scores from the leaderboard file.

    Parameters:
    None

    Raises:
    - FileNotFoundError: If the leaderboard file is not found.
    - NameError: If there is an issue with the variable 'leaders'.
    - json.decoder.JSONDecodeError: If there is an invalid JSON format in the leaderboard file.

    Returns:
    - dict: A dictionary containing the leaderboard scores.

    """
    try:
        # Initialize an empty dictionary to store leaderboard scores
        leaders = {}
        filename = "leaderboard.txt"
        if os.path.exists(filename):
            with open(filename, "r", encoding = "utf-8") as file:
                # Convert JSON format to Python Dictionary and update empty dictionary
                leaderboard_data = json.load(file)
                leaders.update(leaderboard_data)
        return leaders

    except (FileNotFoundError, NameError) as e:
        print(f"Error: {e}")
        return None
    except json.decoder.JSONDecodeError as e:
        print("Error: Invalid JSON format in the leaderboard file.")
        print(f"Error: {e}")
        return None

def save_score(score):
    """
    Save a player's score with player's name to the leaderboard file.

    Parameters:
    - score (int): The player's score to be saved.

    Raises:
    - NameError: If there is an issue with the variable 'player_name' or 'leaders'.
    - IOError: If there is an issue saving the score to the file.
    - json.JSONDecodeError: If there is an issue decoding JSON data.

    Returns:
    None

    """
    try:
        # Prompt the user to enter their name
        player_name = input("Enter your name: ")

        # Load existing leaderboard socres
        leaders = load_scores()

        # Update the leaderboard with new score
        leaders[player_name] = score

        # Save the updated leaderboard to leaderboard.txt
        with open("leaderboard.txt", "w", encoding="utf-8") as file:
            # Convert Python Dictonary into JSON format and writing into file
            json.dump(leaders,file)
            print("Score saved successfully.")
            return

    except NameError as e:
        print(f"Error: {e}")

    except IOError as e:
        print(f"Error saving the score to the file: {e}")

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

def display_leaderboard(leaders):
    """
    Display the leaderboard with player names and scores in a formatted table.

    Parameters:
    - leaders (dict): A dictionary containing player names as keys
                      and their corresponding scores as values.

    Raises:
    - NameError: If there is an issue with the variable 'leaders' or if 'leaders' is not defined.
    - KeyError: If there is an issue accessing keys in the 'leaders' dictionary.

    Returns:
    None
    
    """
    try:
        # Check whether the leaders is empty or not, if empty return
        if not leaders:
            print("Leaderboard is empty.")
            return
        # If not show leaders data in a table with heading player and score
        print("Leaderboard:")
        print("-"*44)
        print("| Player",end="")
        print(" "*25, end="|")
        print(" Score   |")
        print("-"*44)

        for player,score in leaders.items():
            print(f"| {player:<30} | {score:^7} |")
        print("-"*44)

    except (NameError, KeyError) as e:
        print(f"Error: {e}")

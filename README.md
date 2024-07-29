# TIC-TAC-TOE

The game is very popular and fairly simple by itself. It is a 2-player game. Here, there is a board with 3×3 squares. The goal of the game is for players to position their marks so that they make continuous lines either vertically, horizontally or diagonally. An opponent can prevent a win by blocking the completion of the opponent's line.

INPUT AND OUTPUT :

Initially, each cell in the board is numbered like the keyboard’s number pad. And thus, a player can make their move in the game board by entering the number from the keyboard number pad.

At any instant of time, the two crucial information required are: ➔ Status of the grid – We must have a data structure that stores each cell’s state, that is, whether it is occupied or vacant.It is managed by a list ofcharacters, which can have three possible values,

' ' – A vacant cell
'X' – A cell occupied by player X
'O' – A cell occupied by player O
➔ Each player’s moves – We must somehow have the knowledge of each player’s past and present moves, that is, the positions occupied by 'X' and 'O'. In the main function: Player 1 is requested to input the cell number and then the interpreter checks if the input is a valid move or not. If the cell that player requests to move to is valid, the cell will be filled else the user would be requested to choose another cell. Similarly, then player 2 is requested to input the cell number. To Check The Winning Condition: The total of 8 conditions will be checked, and the player who has made the last move will be declared as the winner of the game. And if no one wins, the game will be declared ‘tie’.

FUNCTIONS AND FEATURES OF THE PROPOSED SYSTEM:

- This project will be able to take user-inputs and fill in the different blocks based on what input the user gives. Once the whole board gets filled, the program can check for the winning condition; and if no one wins, the game can declare that it was a tie.

- This project will be implementing quite a few features that Python provides. For creating the game board, a dictionary will be used. In Python, dictionaries are mutable, unordered collections which store elements in the form of key:value pairs, which associate keys to values.
- Multiple if-else statements will also be used for checking whether theplayer has entered a valid input, for filling the blocks themselves, and so on.
- It includes
    - computer vs player
    - player vs player.
The user has to choose accordingly.

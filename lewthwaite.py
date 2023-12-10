def newBoard(n):
    """
    :param n: int, nombre de lignes et de colonnes de "board"
    :return: list[list[int]], plateau de jeu
    """
    board = []
    pion = 2

    for i in range(n):
        row = []
        for j in range(n):
            row.append(pion)
            pion = (pion%2)+1
        board.append(row)

    center = n//2
    board[center][center] = 0

    return board

def displayBoard(board, n):
    """
    :param board: list[list[int]], plateau de jeu
    :param n: int, nombre de lignes et de colonnes de "board"
    """
    # Determine the spacing according to the board size
    graph_space = " " if n > 9 else ""

    # Print the row numbers
    for row in range(1, n + 1):
        row_space = "" if row > 9 else " "
        print(f"{row_space}{row} | ", end="")
        
        # Print the symbols
        for element in board[row - 1]:
            symbol = "." if element == 0 else "x" if element == 1 else "o"
            print(f"{graph_space}{symbol}", end=" ")
        
        print("")

    # Print enough "-" according to the board size
    mult_factor = 3 if n > 9 else 2
    add = -1 if n > 9 else 0
    print(" " * mult_factor + "-" * (mult_factor * (n + 1) + add) + "\n" + " " * 4, end="")


    # Print columns numbers
    row_space = " " if n <= 9 else "  "

    for column in range(1, n + 1):
        if column == 10:
            row_space = " "
        print(f"{row_space}{column}", end="")



def possiblePawn(board, n, player, i, j):
    """
    :param board: list[list[int]], plateau de jeu
    :param n: int, nombre de lignes et de colonnes de "board"
    :param player: int, numéro du joueur (1: croix/blanc, 2: rond/noir)
    :param i: int, coordonnées du pion sur l'axe des abscisses
    :param j: int, coordonnées du pion sur l'axe des ordonnées
    :return: bool, True si le pion de coordonnées i, j peut être déplacer False sinon 
    """
    if 1 <= i <= n and 1 <= j <= n:
        x_coords = i-1
        y_coords = j-1
        if board[y_coords][x_coords] == player:
            if not i==1:
                if board[y_coords][x_coords-1] == 0:
                    return True
            if not i==n:
                if board[y_coords][x_coords+1] == 0:
                    return True
            if not j == 1:
                if board[y_coords-1][x_coords] == 0:
                    return True
            if not j==n:
                if board[y_coords+1][x_coords] == 0:
                    return True
    return False

def selectPawn(board, n, player):
    """
    :param board: list[list[int]], plateau de jeu
    :param n: int, nombre de lignes et de colonnes de "board"
    :param player: int, numéro du joueur (1: croix/blanc, 2: rond/noir)
    :return: tuple(int), coordonnées du pion pouvant être déplacé    
    """
    while True:
        player_choice_i = int(input("Choose the coordinates in the x-axis of the pawn you want to move : "))
        player_choice_j = int(input("Choose the coordinates in the y-axis of the pawn you want to move : "))
        if possiblePawn(board, n, player, player_choice_i, player_choice_j):
            return player_choice_i, player_choice_j
        print("The coords of this pawn do not exist or it is not a valid pawn to move, please try again\n")

def updateBoard(board, n, i, j):
    """
    :param board: list[list[int]], plateau de jeu
    :param n: int, nombre de lignes et de colonnes de "board"
    :param i: int, coordonnées du pion sur l'axe des abscisses
    :param j: int, coordonnées du pion sur l'axe des ordonnées
    """
    x_coords = i-1
    y_coords = j-1

    if not i==1:
        if board[y_coords][x_coords-1] == 0:
            board[y_coords][x_coords-1] = board[y_coords][x_coords]
            board[y_coords][x_coords] = 0
    if not i==n:
        if board[y_coords][x_coords+1] == 0:
            board[y_coords][x_coords+1] = board[y_coords][x_coords]
            board[y_coords][x_coords] = 0
    if not j == 1:
        if board[y_coords-1][x_coords] == 0:
            board[y_coords-1][x_coords] = board[y_coords][x_coords]
            board[y_coords][x_coords] = 0
    if not j==n:
        if board[y_coords+1][x_coords] == 0:
            board[y_coords+1][x_coords] = board[y_coords][x_coords]
            board[y_coords][x_coords] = 0

def again(board, n, player):
    """
    :param board: list[list[int]], plateau de jeu
    :param n: int, nombre de lignes et de colonnes de "board"
    :param player: int, numéro du joueur (1: croix/blanc, 2: rond/noir)
    :return: bool, True si le joueur peut bouger un pion False sinon
    """
    for rows in range(n):
        for element in range(n):
            if board[rows][element] == 0:
                if not element-1 < 0 and board[rows][element-1] == player:
                    return True
                if not element+1 >= n and board[rows][element+1] == player:
                    return True
                if not rows-1 < 0 and board[rows-1][element] == player:
                    return True
                if not rows+1 >= n and board[rows+1][element] == player:
                    return True
                return False

def lewthwaite(n):
    """
    :param n: int, nombre de lignes et de colonnes de "board"
    """
    if n%4 != 1:
        n = 9
    
    board = newBoard(n)
    player = 1
    displayBoard(board, n)

    while again(board, n, player):

        print(f"\n\nPlayer {player}")
        player_move = selectPawn(board, n, player)
        updateBoard(board, n, player_move[0], player_move[1])
        displayBoard(board, n)

        player = player%2+1
    
    
    print("\n\nWinner :", player%2+1)

lewthwaite(57)

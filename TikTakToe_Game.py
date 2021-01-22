game_active = True
active_player = "X"

field = [" ", 
        "1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"]
        
            
def gameStatus():
    print(field[1] + "|" + field[2] + "|" + field[3])
    print(field[4] + "|" + field[5] + "|" + field[6])
    print(field[7] + "|" + field[8] + "|" + field[9])

def playerInput():
    global game_active 

    while True:
        play_move = input("Please select your field: ")

        if play_move == "exit" or play_move == "leave":
            game_active = False
            return "You left the game" 

        try: 
            play_move = int(play_move)
        except ValueError:
            print("Please type in a number!")
        else:
            if play_move in range(1,10):
                return play_move
            else:
                print("Please choose a number between 1 and 9!")

def switchPlayer():
    global active_player
    if active_player == "X":
        active_player = "O"
    else: 
        active_player = "X"

def checkWinner():
    if field[1] == field[2] == field[3]:
        return field[1]
    if field[4] == field[5] == field[6]:
        return field[4]
    if field[7] == field[8] == field[9]:
        return field[7]
    if field[1] == field[4] == field[7]:
        return field[1]
    if field[2] == field[5] == field[8]:
        return field[2]
    if field[3] == field[6] == field[9]:
        return field[3]
    if field[1] == field[5] == field[9]:
        return field[1]
    if field[3] == field[5] == field[7]:
        return field[3]

def checkDraw():
    conter = 0
    for x in range(0,10):
        if x == "X" or x == "O":
            counter += 1
            if counter == 9:
                return True



while game_active:
    print("Player " + active_player + " is now playing")
    gameStatus()

    move = playerInput()
    print(move)

    if not move == "You left the game":
        if field[move] == "X" or field[move] == "O":
            print("This field is already used, please select another field.")
            continue
        if active_player == "X":
            field[move] = "X"
        else:
            field[move] = "O"

        winner = checkWinner()
        if winner:
            print("Player " + winner + " has won the game, congratulations!")
            game_active = False
            break

        draw = checkDraw()
        if draw:
            print("It's a draw! Try it again.")
            game_active = False
        switchPlayer()


        
        
        


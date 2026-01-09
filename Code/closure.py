def parent_function(person,coins):
    # coins=3
    def play_game():
        nonlocal coins
        coins -=1
        if coins >1:
            print(person+ str(coins)+" coins left to play")
        elif coins ==1:
            print(person+ str(coins)+" coin left to play")
        else:
            print(person +"You have no coins left to play")
    return play_game
tommy=parent_function("Tommy",5)
tommy=parent_function("Tommy",3)
jenny=parent_function("Jenny",2)
tommy()
tommy()
jenny()
tommy()
import random
ply_deck = []
ai_deck = []
dominoes = [[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [1, 1], [1, 2], [1, 3], [1.4], [1, 5], [1, 6],
            [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [3, 3], [3, 4], [3, 5], [3, 6], [4, 4], [4, 5], [4, 6], [5, 5],
            [5, 6], [6, 6]]
doubles = [[1, 1], [2, 2],[3,3],[4,4],[5,5],[6,6],[0, 0]]

# creating random decks
for i in range(0, 7):
    temp = random.choice(dominoes)
    ply_deck.append(temp)
    dominoes.remove(temp)
    temp = random.choice(dominoes)
    ai_deck.append(temp)
    dominoes.remove(temp)


# getting domino from stock
def stock():
    if len(dominoes)!=0:
        temporary = random.choice(dominoes)
        return temporary
    else:
        print("There are no dominoes in stock.")


# 1 means player's turn 2 means AI's turn
game=[]
turn = 0
for double in doubles:
    if double in ply_deck:
        turn = 2
        game.append(double)
        ply_deck.remove(double)
        zad=double
        break
    if double in ai_deck:
        turn = 1
        game.append(double)
        ai_deck.remove(double)
        break
if turn == 0:
    exit("No one has doubles, start the game again.")
print("Game has started!!!")
if turn == 1:
    print("AI made first move.")
# game
while len(ply_deck) != 0 or len(ai_deck) != 0:
    left_side=(game[0])[0]
    right_side=(game[-1])[1]
    print('""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')
    if turn == 2:
        print(f'You have played {zad}')
    print("Dominoes on table:")
    print(game)
    print(f'Dominoes\' count in stock:{len(dominoes)}')
    print("Your deck:")
    for i in range(0,len(ply_deck)):  # printing player's deck
        print(f'{i+1}.{ply_deck[i]}')
    if turn == 1:  # player's move
        print(f"Dominoes in stock: {len(dominoes)}")
        if len(game) != 0:
            stk = input("It is your turn. Do you want domino from stock?(yes or no)")
            if "yes" == stk.lower():
                if len(dominoes) == 0:
                    choice = input("There is no domino in stock.Do you want to pass?(If you want, then write pass)")
                    if choice.lower() == "pass":
                        k = 2
                        continue
                ply_temp_dom = stock()
                dominoes.remove(ply_temp_dom)
                ply_deck.append(ply_temp_dom)
                print('""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')
                print("Dominoes on table:")
                print(game)
                print("Your deck:")
                for i in range(0, len(ply_deck)):
                    print(f'{i + 1}.{ply_deck[i]}')  # printing player's deck
            elif stk.lower() != "no":
                print("Enter valid answer.")
                continue
            index = int(input("Write index of domino to play:"))
            ply_dom = ply_deck[index - 1]
            side = input("From which side you want to play?(l for left,r for right)")
            left_dom = game[0]
            right_dom = game[-1]
            l_side = left_dom[0]
            r_side = right_dom[-1]
            if side.lower() == "l":
                if l_side == ply_dom[0] or l_side == ply_dom[1]:
                    if l_side == ply_dom[1]:
                        game.insert(0, ply_dom)
                    else:
                        game.insert(0, ply_dom[::-1])
                else:
                    print("This move is illegal.(Domino is not matching)")
                    continue
            else:
                if r_side == ply_dom[0] or r_side == ply_dom[1]:
                    if r_side == ply_dom[0]:
                        game.insert(-1, ply_dom)
                    else:
                        game.insert(-1, ply_dom[::-1])
                else:
                    print("This move is illegal.(Domino is not matching)")
                    continue
        turn = 2
    else:  # AI's turn
        game_dom = len(game)
        left_dom = game[0]
        right_dom = game[-1]
        left_side = left_dom[0]
        right_side = right_dom[1]
        for ai_dom in ai_deck:
            if ai_dom[1] == left_side or ai_dom[0] == left_side:
                if ai_dom[1] == left_side:
                    game.insert(0, ai_dom)
                    ai_deck.remove(ai_dom)
                    break
                elif ai_dom[0] == left_side:
                    game.insert(0, ai_dom[::-1])
                    ai_deck.remove(ai_dom)
                    break
            elif ai_dom[0] == right_side or ai_dom[1] == right_side:
                if ai_dom[1] == right_side:
                    game.insert(-1, ai_dom[::-1])
                    ai_deck.remove(ai_dom)
                    break
                elif ai_dom[0] == left_side:
                    game.insert(-1, ai_dom)
                    ai_deck.remove(ai_dom)
                    break
            else:
                while True:
                    if len(dominoes) != 0:
                        ai_temp_dom = stock()
                        ai_deck.append(ai_temp_dom)
                        ai_dom = ai_temp_dom
                        if ai_dom[1] == left_side or ai_dom[0] == left_side:
                            if ai_dom[1] == left_side:
                                game.insert(0, ai_dom)
                                ai_deck.remove(ai_dom)
                                break
                            elif ai_dom[0] == left_side:
                                game.insert(0, ai_dom[::-1])
                                ai_deck.remove(ai_dom)
                                break
                        elif ai_dom[0] == right_side or ai_dom[1] == right_side:
                            if ai_dom[1] == right_side:
                                game.insert(-1, ai_dom[::-1])
                                ai_deck.remove(ai_dom)
                                break
                            elif ai_dom[0] == left_side:
                                game.insert(-1, ai_dom)
                                ai_deck.remove(ai_dom)
                                break
                    else:
                        print("AI said pass")
                        turn = 1
                        break
        input("AI have played. Press ENTER to continue.")
        turn = 1

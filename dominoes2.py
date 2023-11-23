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
    if turn==1:
        while len(dominoes)!=1:
            choice=input("Do you want a domino from stock?(yes or no)").lower()
            print(choice)
            if choice=="yes" or choice=="no":
                if choice=="yes":
                    stk_domino=stock()
                    ply_deck.append(stk_domino)
                    dominoes.remove(stk_domino)
                    print('""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')
                    print("Dominoes on table:")
                    print(game)
                    print(f'Dominoes\' count in stock:{len(dominoes)}')
                    print("Your deck:")
                    for i in range(0, len(ply_deck)):  # printing player's deck
                        print(f'{i + 1}.{ply_deck[i]}')
                else:
                    break
            else:
                print("You must write yes or no.Try again")
                continue
    else:
        playable_dominoes = 0
        for i in ai_deck:
            if i[0] == left_side or i[1] == right_side or i[0] == right_side or i[1] == left_side:
                playable_dominoes += 1
        while len(dominoes) != 1 and playable_dominoes==0:
            stk_domino=stock()
            dominoes.remove(stk_domino)

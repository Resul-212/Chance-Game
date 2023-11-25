
import random
dominoes=[]
ply_deck = []
ai_deck = []
ai_domino=""
doubles=[]
game=""
side=[]

for i in range(0,7):  # Creating domino lists
    for j in range(0,7):
        if f'{str(i)}|{str(j)}' not in dominoes and f'{str(j)}|{str(i)}' not in dominoes:
            dominoes.append(f'{str(i)}|{str(j)}')
            if j==i:
                doubles.append(f'{str(i)}|{str(j)}')
        else:
            continue
doubles.remove("0|0")
doubles.append("0|0")


# Giving dominoes to players.
for i in range(0, 7):
    temp = random.choice(dominoes)
    ply_deck.append(temp)
    dominoes.remove(temp)
    temp = random.choice(dominoes)
    ai_deck.append(temp)
    dominoes.remove(temp)


# Printing game
def interface():
    print('""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""')
    print("Dominoes on table:")
    print(f"[{game}]")
    print(f'Dominoes\' count in stock:{len(dominoes)}')
    print(f'AI\'s dominoes\' count:{len(ai_deck)}')
    print("Your deck:")
    for g in range(0, len(ply_deck)):  # printing player's deck
        print(f'{g + 1}.[{ply_deck[g]}]')


# Getting a domino from stock
def stock():
    if len(dominoes) != 1:
        temporary = random.choice(dominoes)
        dominoes.remove(temporary)
        return temporary
    """"""


# AI's move
def ai():
    for h in ai_deck:
        if left_side==h[0] or left_side==h[2] or right_side==h[2] or right_side==h[2]:
            if left_side == h[0]:
                side.append("l")
                ai_deck.remove(h)
                return h[::-1]
            elif left_side == h[2]:
                ai_deck.remove(h)
                side.append("l")
                return h
            elif right_side == h[0]:
                ai_deck.remove(h)
                side.append("r")
                return h
            elif right_side == h[2]:
                ai_deck.remove(h)
                side.append("r")
                return h[::-1]
    while True:
        if len(dominoes)!=1:
            temp_dom=stock()
            input("AI got a domino from stock.Press ENTER to continue.")
            if left_side==temp_dom[0] or left_side==temp_dom[2] or right_side==temp_dom[0] or right_side==temp_dom[2]:
                if left_side==temp_dom[0]:
                    side.append("l")
                    return temp_dom[::-1]
                elif left_side==temp_dom[2]:
                    side.append("l")
                    return temp_dom
                elif right_side==temp_dom[0]:
                    side.append("r")
                    return temp_dom
                elif right_side==temp_dom[2]:
                    side.append("r")
                    return temp_dom[::-1]
            else:
                ai_deck.append(temp_dom)
        else:
            return "pass"


# Deciding who will start first
turn=0
for double in doubles:
    if double in ply_deck:
        turn = 2
        game+=double
        ply_deck.remove(double)
        input(f"You have played [{double}].Press ENTER to continue.")
        break
    if double in ai_deck:
        turn = 1
        game+=double
        ai_deck.remove(double)
        input(f"AI has played [{double}].Press ENTER to continue.")
        break


if turn==0:
    exit("No one has doubles. Start again")


# Game
ai_choice=""
player_choice=""
while len(ply_deck)!=0 and len(ai_deck)!=0:
    interface()
    if ai_choice=="pass" and player_choice=="pass":
        print(f'AI hand {ai_deck}')
        print(f'Player\' hand {ply_deck}')
        exit("It is a tie.")
    left_side=game[0]
    right_side=game[len(game)-1]
    if turn==1:  # Player's turn
        player_choice=""
        choice = ""
        side_choice = ""
        while len(dominoes)!=1:
            if choice=="":
                choice=input("Do you want a domino from stock?(yes or no)").lower()
            else:
                choice = input("Do you want another domino again from stock?(yes or no)").lower()
            if choice=="yes":
                stock_domino=stock()
                print(f"You picked up [{stock_domino}]")
                input("Press ENTER to continue.")
                ply_deck.append(stock_domino)
                interface()
            elif choice=="no":
                break
            else:
                choice=""
                print("Enter valid answer.(yes or no)")
                input("Press ENTER to continue.")
                continue
        if len(dominoes)==1:
            player_choice=input("There are no dominoes left in stock. If you don't have any dominoes to play,then write pass.If you don't just press ENTER.")
            if player_choice=="pass":
                player_choice=input("It is your second chance do you want to say pass?(If you dont want press ENTER)")
                if player_choice!="pass":
                    player_choice=""
                else:
                    turn=2
                    continue
        index=-1
        while index==-1:
            try:
                index=int(input("Write the index of domino you want to play:"))-1
            except ValueError:
                print("Enter only integer type.")
        if 0>=(index+1) or (index+1)>len(ply_deck):
            print("Enter a valid index.")
            input("Press ENTER to continue.")
            continue
        ply_domino=ply_deck[index]
        if left_side==right_side:
            if left_side==ply_domino[2]:
                game=ply_domino+"]["+game
                turn=2
                ply_deck.remove(ply_domino)
                continue
            elif left_side==ply_domino[0]:
                game = game+ "][" +ply_domino
                turn=2
                ply_deck.remove(ply_domino)
                continue
        elif (ply_domino[0]==left_side or ply_domino[2]==left_side) and (ply_domino[0]==right_side or ply_domino[2]==right_side):
            side_choice = input("From which side you want to play?(l for left, r for right)").lower()
            if side_choice=="l":
                if ply_domino[2]==left_side:
                    game=ply_domino+"]["+game
                    turn=2
                    ply_deck.remove(ply_domino)
                    continue
                elif ply_domino[0]==left_side:
                    game=ply_domino[::-1]+"]["+game
                    turn=2
                    ply_deck.remove(ply_domino)
                    continue
            elif side_choice=="r":
                if ply_domino[0]==right_side:
                    game=game+"]["+ply_domino
                    turn=2
                    ply_deck.remove(ply_domino)
                    continue
                elif ply_domino[2]==right_side:
                    game = game +"]["+ ply_domino[::-1]
                    turn=2
                    ply_deck.remove(ply_domino)
                    continue
            else:
                print("Enter a valid answer.(l or r)")
                input("Press ENTER to continue.")
                continue
        elif ply_domino[0]==left_side or ply_domino[2]==left_side or ply_domino[0]==right_side or ply_domino[2]==right_side:
            if ply_domino[0]==left_side:
                game = ply_domino[::-1] + "][" + game
                turn = 2
                ply_deck.remove(ply_domino)
                continue
            elif ply_domino[2]==left_side:
                game = ply_domino + "][" + game
                turn = 2
                ply_deck.remove(ply_domino)
                continue
            elif ply_domino[0]==right_side:
                game=game+"]["+ply_domino
                turn = 2
                ply_deck.remove(ply_domino)
                continue
            elif ply_domino[2]==right_side:
                game = game + "][" + ply_domino[::-1]
                turn = 2
                ply_deck.remove(ply_domino)
                continue
        else:
            input("Domino is not matching select another one or get a one from stock.Press ENTER to continue")
            continue
    elif turn==2:  # AI's turn
        ai_choice=""
        side = []
        ai_domino=ai()
        if ai_domino=="pass":
            input("AI said pass.Press ENTER to continue")
            ai_choice='pass'
            turn=1
            continue
        else:
            if side==["l"]:
                game=ai_domino+"]["+game
                turn=1
                input(f"AI has played [{ai_domino}] ,press ENTER to continue.")
                continue
            elif side==["r"]:
                game=game+"]["+ai_domino
                input(f"AI has played [{ai_domino}] ,press ENTER to continue.")
                turn=1
                continue
if len(ply_deck)==0:
    print("Congratulations!!! You won.")
elif len(ai_deck)==0:
    print("You lost. AI has won")

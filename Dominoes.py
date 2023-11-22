import random
dominoes=[]
double_dominoes=[]


def Player():
    game_="".game()
    player_hand="".player()
    player_play1=""
    player_play2=""
    if (game_[0] in player_hand) or (game_[len(game_)-1] in player_hand):
        player_play1=input("Select a domino to play:")
        player_play2=input("Which side will you play?(r for right,l for left)")
        player_play2.lower()
        if player_play2=="l":
            if game_[0]==



for i in range(0,7):
    for j in range(0, 7):
        if (f'{str(i)}/{str(j)}' not in dominoes) and (f'{str(j)}/{str(i)}' not in dominoes):
            dominoes.append(f'{str(i)}/{str(j)}')
        if i==j:
            if i!=0 or j!=0:
                double_dominoes.append(f'{str(i)}/{str(j)}')
double_dominoes.append("0/0")

player=[]
computer_hand=[]
for i in range(0,7):
    random_=random.choice(dominoes)
    player.append(random_)
    dominoes.remove(random_)
for i in range(0,7):
    random_=random.choice(dominoes)
    computer_hand.append(random_)
    dominoes.remove(random_)
game=[]
turn=0
print(f'Your hand{player}')
for i in double_dominoes:
    if i in player:
        print("Player started")
        game.append(i)
        player.remove(i)
        turn=2
        break
    if i in computer_hand:
        print("Computer started")
        game.append(i)
        computer_hand.remove(i)
        turn=1
        break
print(f'game is {game}')
if turn=="":
    exit("Start again")
while len(computer_hand)!=0 or len(player)!=0:
    print(f'Your hand{player}')
    if turn==1:
        Player()


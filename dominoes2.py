import random
dominoes=[]
ply_deck = []
ai_deck = []
doubles=[]
game=""

for i in range(0,7):
    for j in range(0,7):
        if f'{str(i)}|{str(j)}' not in dominoes and f'{str(j)}|{str(i)}' not in dominoes:
            dominoes.append(f'{str(i)}|{str(j)}')
            if j==i:
                doubles.append(f'{str(i)}|{str(j)}')
        else:
            continue
doubles.remove("0|0")
doubles.append("0|0")


for i in range(0, 7):
    temp = random.choice(dominoes)
    ply_deck.append(temp)
    dominoes.remove(temp)
    temp = random.choice(dominoes)
    ai_deck.append(temp)
    dominoes.remove(temp)


def stock():
    if len(dominoes) != 1:
        temporary = random.choice(dominoes)
        return temporary
    else:
        print("There are no dominoes in stock.")


def ai():
    for i in ai_deck:
        if game[0]==i[0] or game[0]==i[1]:

def flipTile(tile):
    return [tile[1], tile[0]]



turn=0
for double in doubles:
    if double in ply_deck:
        turn = 2
        game+=double
        ply_deck.remove(double)
        print(f"You have played {double}")
        break
    if double in ai_deck:
        turn = 1
        game+=double
        ai_deck.remove(double)
        print(f"Ai have played {double}")
        break
if turn==0:
    exit("No one has doubles. Start again")
print(game)

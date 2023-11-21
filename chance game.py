import random
print("The game is simple, computer generates a random number and you are trying to guess it")
num=int(input("Enter a number(from 0 to 100):"))
random_num=random.randint(0,100)
sans=4
while sans>0:
    if num==random_num:
        print("congratulations you won!")
        break
    else:
        print(f'The number isn\'t matching .{sans} chances left.')
        sans -= 1
        if num>random_num:
            print("Enter a smaller number:")
        else:
            print("Enter a larger number.")
        if abs(random_num-num)<10:
            print("You are very close!!!")
        elif abs(random_num-num)<20:
            print("You got close.")
        elif abs(random_num-num)<40:
            print("You are far away.")
        else:
            print("You are very very far away.")
    num=int(input("Enter a different number:"))
if sans==0:
    print(f"You lost. The number was {random_num}.")

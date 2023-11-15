import random
num=int(input("Eded daxil edin:"))
random_num=random.randint(0,100)
sans=4
while sans>0:
    if num==random_num:
        print("Təbriklər düz tapdiniz")
        break
    else:
        print(f'Cavabınız səhvdir.{sans} şansınız qaldı')
        sans -= 1
        if num>random_num:
            print("Daha  kicik eded daxil edin")
        else:
            print("Daha boyuk eded daxil edin")
        if abs(random_num-num)<10:
            print("cox yaxinlasmisiniz")
        elif abs(random_num-num)<20:
            print("bir az yaxinlasmisiniz")
        elif abs(random_num-num)<40:
            print("uzaqsiniz")
        else:
            print("cox uzaqsiniz")
    num=int(input("Basqa eded daxil edin:"))
if sans==0:
    print(f"Uduzdunuz.Reqem {random_num} idi")
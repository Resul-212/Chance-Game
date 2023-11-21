for i in range(1,10):
    print(sep="\n")
    for j in range(1,11):
        if j==3 and i<5:
            print(end=" ")
        if j==4 and i<4:
            print(end=" ")
        if j==5 and i<3:
            print(end=" ")
        if i==1 and j>5:
            print(end=" ")
        print(f'{j}x{i}={i*j}',end=" ")

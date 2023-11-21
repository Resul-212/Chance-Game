list1=[200,100,50,20,10,5,1]
list2=[0,0,0,0,0,0,0]
amount=int(input("Enter the amount:"))
for i in range(0,len(list1)):
    if amount/list1[i]>=1:
        list2[i]=amount//list1[i]
        amount%=list1[i]
for i in range(0,len(list1)):
    if list[i]!=0:
        print(f'{list2[i]} pieces of {list1[i]} bills')

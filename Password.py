print("Must use at least one character in each category.")
password=input("Enter your password:(Characters can be used:0-9,a-z,A-Z,~!@#$%^&*_-+=`| () }{ []:;\"'<>,.?/)")
list_password=list(password)
combinations=["012","123","234","345","456","567","678","789"]
characters=['~', '!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=', '`', '|', ' ', '(', ')', ' ', '{', '}', ' ', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
if len(password)<8:
    exit("Paswword must contain 8 or more characters.")
k=0
temp=password[0]
for i in range(1,len(password)):      
    if (temp==password[i]) and k==0:
        k+=2
    elif (temp==password[i]):
        k+=1
    else:
        k=0
        temp=password[i]
    if k>2:
        exit("Password can not contain 3 or more same characters in a row.")
for j in combinations:
    if j in password:
        exit("Password can not contain 3 or more consecutive numbers.")
uppers=0
for g in list_password:
    if not g.isdigit() and g.upper()==g and (g not in characters):
        uppers+=1
characters_=0
for y in list_password:
    if y in characters:
        characters_+=1
if uppers!=0:
    if characters_!=0:
        exit("Password successfully set.")
    else:
        exit("Password must contain at least 1 special characer.(~!@#$%^&*_-+=`| () }{ []:;\"'<>,.?/)")
else:
    exit("Password must contain at least 1 uppercase letter.")

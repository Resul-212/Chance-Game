def result(x):
    if x=="":
        return 51
    if not x.isdigit():
        exit("Enter only numbers.")
    if int(x)<0 or int(x)>100:
        exit("Enter valid number.")
    return int(x)
result1=result(input("Enter math result:"))
result2=result(input("Enter physics result:"))
result3=result(input("Enter chemistry result:"))
def average():
    return float(format((result1+result2+result3)/3,f".2f"))

student={
    "name":"Elvin",
    "surname":"Imanov",
    "mathResult":result1,
    "physicsResult":result2,
    "chemistryResult":result3,
    "averageResult":average()
}
print(student)
if student.get("averageResult")>=81:
    print("Diploma work accepted.")
else:
    print("Diploma work declined.")

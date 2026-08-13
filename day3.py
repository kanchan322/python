names=["kanchan", "asmita",1,2,3,4,True,False]
print(names)

names=["kanchan", "asmita",1,2,3,4,True,False]
print(names[-1])

names=["kanchan", "asmita",1,2,3,4,True,False]
names[1]="ashu"
print(names)

names=["kanchan", "asmita",1,2,3,4,True,False]
print("before")
print(names)
print()
names.append("ashu")
print("after:")
print(names)

names=["kanchan", "asmita",1,2,3,4,True,False]
print("before")
print(names)
print()
names.remove("asmita")
print("after:")
print(names)

names=["kanchan", "asmita",1,2,3,4,True,False,"sita"]
print("before")
print(names)
print()
last=names.pop()
print("after")
print(names)
print(last)

names=["kanchan", "asmita","sita"]
print("before")
print(names)
print()

names.sort()
#print("after")
print(names)


names=["kanchan", "asmita","sita","ashu"]
print("before") 
print(names)
print()
print("sliced:")
print(names[0:2])


names=["kanchan", "asmita","sita","ashu"]
print("before") 
print(names)
print()
print("kanchan" in names)


#tuples
names=("kanchan", "asmita","sita","ashu","ram","kanchan")
print(names.count("kanchan"))


capitals={
    "nepal":"kathmandu",
    "usa":"washington dc",
    "franche":"paris",
    "china":"beijing",
    "india":"delhi",
    "uk":"london"}
print(capitals["nepal"])


capitals.update({
    "japan":"tokyo",
    "germany":"berlin"})
print(capitals)
print(capitals.items())


#condition
is_raining=True
if is_raining:
    print("take umbrella")
else:
    print("no need to take umbrella")


password=input("enter your password:").strip()
if password=="kanchan123":
    print("login successful")
else:
    print("invalid password")



score=75
if score>=60:
    print(" you passed")
    print("congratulations")
else:
    print(" you failed")
    print("better luck next time")


score=82
if   score>=90: print("grade A")
elif score>=80: print("grade B")
elif score>=70: print("grade C")
elif score>=60: print("grade D")
else:           print("grade E")

#for loop
names=["Alice", "Bob", "Charlie", "David", "Eve"]
for name in names:
    print(f"Hello, {name}")
    print(f"bye, {name}")
print("Hello")


fruits = ["apple", "banana", "cherry", "date", "mango"]
for fruit in fruits:
    upper=fruit.upper()
    lenght=len(fruit)
    print(f"The word {upper} consists of {lenght} letters")
print("done")    

#range function
for i in range(5):
    print(f"Round {i}")

for i in range(1, 6):
    print(f"5 * {i} = {5 * i}")

for i in range(1,6,2):
    print(i)

#accumulator
total=0
prices=[10,20,30,40,50]
for price in prices:
    total+=price
print(total)    
print(f"final price={total}")

numbers=[10,20,30,40,50]
biggest=numbers[0]
for n in numbers:
    if n>biggest:
        biggest=n
print(f"Biggest: {biggest}")


#while loop
countdown=5
while countdown > 0:
    print(f"T minus {countdown}....")
    countdown-=1
print("Blast off!")



secret="python"
guess=input("password: ")
while guess != secret:
    print("Wrong! Try again.")
    guess=input("password: ")
print("Correct! Access granted.")

#continue and break
fruits=["apple", "banana", "cherry", "date", "mango"]
for fruit in fruits:
    if fruit == "cherry":
        continue
    print(fruit)


  
for i in range (1, 11):
    print(i)

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for fruit in fruits:
    print(fruit)

for letter in "Python":
    print(letter)

for i in range(1, 11):
    print(i)

for i in range(1, 20):
    if i % 2 == 0:
        print(i)

number = int(input("Enter a number: "))

for i in range(1, 11):
    result = number * i
    print(f"{number} x {i} = {result}")

text = input("Enter a text: ")

count = 0

for char in text:
    if char == "a":
        count += 1

print("Number of 'a':", count)


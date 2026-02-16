# import time
# start = time.time()

# x = 1

# while x < 11:
#     print(x)
#     x = x+1

# end = time.time()
# print(f"Execution time: {round(end - start, 3)} seconds")

right_number = 7
max_tries = 0
guess = int(input("Guess a number between 1 and 10: "))
msg = "Congratulations! You guessed the right number."

while guess != right_number and max_tries < 2:
    max_tries += 1
    print("Wrong guess! Try again.")
    guess = int(input("Guess a number between 1 and 10: "))

if max_tries == 2 and guess != right_number:
    msg = "Sorry, you've used all your tries. The correct number was " + str(right_number) + "."
print(msg)

groupA = int(input("Enter points for Team A: "))
groupB = int(input("Enter points for Team B: "))
if groupA > groupB:
    print("Team A wins!")
elif groupB > groupA:
    print("Team B wins!")
elif groupB == groupA:
    print("It's a tie!")
else: 
    print("Invalid input.")
import  time
from time import sleep

print("Mind Game")
print("-" * 30)
print("Caution! This game will test your intelligence. Stay smart")
print("\n")


print("MENU")
print("-" * 30)
print("1) Start")
print("2) Help")
print("3) Quit")
option = int(input("Enter the options to get started(example 1,2 or 3): "))

i = 1

if option == 1:
    print("\n")
    print("Starting in...")
    for i in range(5, 0, -1):
     print(i)
     time.sleep(1)
    for i in range(1,2):
     print("Pick a number in your head")
     time.sleep(8)
    for i in range(1, 2):
     print("Add 10 to the number in your head")
     time.sleep(8)
    for i in range(1,2):
     print("Multiple the number you have now by 2")
     time.sleep(8)
    for i in range(1,2):
     print("Multiple the number by 4")
     time.sleep(8)
    for i in range(1,2):
     print("Subtract the number in your head from it")
     time.sleep(8)
    for i in range(1,2):
     print("Multiple the number by 4")
     time.sleep(8)
    for i in range(1,2):
     print("Now the answer is 80")
     time.sleep(8)
        
elif option == 2:
    print("This game tends to test your brine in calculating faster and accurate.\nTherefore stay calm and smart when attempting this game ")
elif option == 3:
    for i in range(1,4):
     print("Disconnecting...")
     time.sleep(1)
    print("Bye! See you later")
else:
    print("Invalid option input")



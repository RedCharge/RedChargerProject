import math
#Simple Caculator

def addition():
    return num1 + num2
def subtraction():
    return num1 - num2
def division():
    return num1 / num2
def power():
    return math.pow(num1, num2)
def square_root():
    return math.sqrt(num1)
def factorial():
    return math.factorial(num1)

# main body
while True:
   print("\nSimple Calculator")
   print("=" * 20)
   print("What would you like to do today:")
   print("1) ➕ Add")
   print("2) ➖ Subtract")
   print("3) ➗ Divide")
   print("4) 📈 Raise to a power ")
   print("5) 🧠 Square Root")
   print("6) 🤯 Factorial")
   print("7) 🚪 Exit")
   choice = int(input("Enter the options(1 to 7): "))

   if choice == 1:
      num1 = int(input("Enter the first number: "))
      num2 = int(input("Enter the second number: "))
      print(f"{num1} + {num2} = {addition()}")
   elif choice == 2:
      num1 = int(input("Enter the first number: "))
      num2 = int(input("Enter the second number: "))
      print(f"{num1} - {num2} = {subtraction()}")
   elif choice == 3:
      while True:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num2 == 0:
          print("Error: Division by 0 is undefined!")
        else:
          print(f"Ans: {num1} / {num2} = {division():.2f}")
          break
   elif choice == 4:
      num1 = float(input("Enter the number: "))
      num2 = int(input("Enter the power of that number: "))
      print(f"The power of {num1} is {power():.2f}")
   elif choice == 5:
      num1 = float(input("Enter the number: "))
      print(f"The square root of {num1} is {square_root():.2f}")
   elif choice == 6:
      num1 = int( input("Enter the number: "))
      print(f"The factorial of {num1} is {factorial()}")
   elif choice == 7:
      print("Thanks for calculating with us!")
      break
   else:
      print("That's not a valid choice.\n"
            "Pick a number from the menu")
print("\n")
print("ATU registration portal")
print("=" * 20)
while True:
  print("1) Add course")
  print("2) Delete course")
  print("3. Exit")
  choice = int(input("Enter your choice: "))
  user_list = []

  if choice == 1:
   n = int(input("How many course do you want to offer: "))
   for i in range(n):
     item = input(f"Enter the course {i + 1}: ")
     user_list.append(item)

   print("Your course")
   for item in user_list:
     print(item)
  elif choice == 2:
     d = int(input("How many courses do you want to delete: "))
     for i in range(d):
       item_to_delete = input(f"Enter the course {i + 1}: ")
       user_list.remove(item_to_delete.lower())

     print("Your course")
     for item in user_list:
       print(item)
  elif choice == "3":
     break
  else:
      print("Invalid choice")




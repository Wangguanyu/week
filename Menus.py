"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message

"""
"""
Enter name: Guido
(H)ello
(G)oodbye
(Q)uit

>>> A
Invalid choice
(H)ello
(G)oodbye
(Q)uit

>>> H
Hello Guido
(H)ello
(G)oodbye
(Q)uit

>>> G
Goodbye Guido
(H)ello
(G)oodbye
(Q)uit

>>> Q
Finished.

"""
name = str(input("Enter your name:"))
menu = "(H)ello\n(G)oodbye\n(Q)uit"
print(menu)
choice = str(input("Enter your choice:"))
while choice.upper() != "Q":
    if choice.upper() == "H":
        print("Hello,", name)
    elif choice.upper() == "G":
        print("Goodbye,", name)
    else:
        print("Invalid message.")
    print(menu)
    choice = str(input("Enter your choice:"))
print("Finished")



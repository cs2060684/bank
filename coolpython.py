print("Welcome to the secure banking framework")
print("What would you like to do?")
op1 = print("Draw money (op1)")
op2 = print("Add money(op2)")
op3 = print("go to settings(op3)")
choice = input("Your selection >")
if choice == op1:
    drawamount = input("how much would you like to draw? >")
    print("you have drawn:")
    print(drawamount)
if choice == op2:
    addamount = input("how much would you like to add")
    print("You have added:")
    print(addamount)
if choice == op3:
    print("this area is currently under development")
    
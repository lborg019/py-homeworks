def input():
    # infinite loop
    while True:
        try:
            cents = int(raw_input("Please enter amount of cents:\n> "))
        except ValueError:
            print("Not an integer!")
            continue
        else:
            break
    return cents

def getFractions(cents):
    # number of nickels
    # number of quarters
    # number of dollar
    nickels  = cents
    dimes    = (cents) / 10
    quarters = (cents) / 25
    dollars  = (cents) / 100
    print("%s nickel(s)")  % nickels
    print("%s dime(s)")    % dimes
    print("%s quarter(s)") % quarters
    print("%s dollar(s)")  % dollars

amount = input()
while int(amount) >= 0:
    print("%s cents:" % amount)
    getFractions(int(amount))
    amount = input()


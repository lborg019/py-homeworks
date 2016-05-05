def input():
    # infinite loop
    while True:
        try:
            cents = int(raw_input("Please enter amount of cents: (negative quits)\n> "))
        except ValueError:
            print("Not an integer!")
            continue
        else:
            break
    return cents

def getFractions(cents):

    while(cents > 10):
        if(cents > 100):
            dollars = cents / 100
            cents = cents - (dollars * 100)
            print("%s dollar(s)") % dollars
        elif (cents > 25):
            quarters = cents / 25
            cents = cents - (quarters * 25)
            print("%s quarter(s)") % quarters
        elif (cents > 10):
            dimes = cents / 10
            cents = cents - (dimes * 10)
            print("%s dime(s)") % dimes

    if(cents != 0):
        print("%s cent(s)") % cents


# call functions
amount = input()
while int(amount) >= 0:
    print("%s cents:" % amount)
    getFractions(int(amount))
    amount = input()


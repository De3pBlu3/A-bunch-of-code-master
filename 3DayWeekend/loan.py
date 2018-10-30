import os
def costofloan():
    os.system('cls')
    cost = float(input("How large is the loan? "))
    years = float(input("How many years is the loan? "))
    oft = int(input("How often do you pay each year? "))
    howmany = oft * years
    Fapr = float(input("What is the APR? (Write without percentage mark) "))
    Rapr = Fapr/100
    payEM = float(input("How much do you pay back each time? "))
    count = 0
    left = 0
    intrest = cost*Rapr

    while count < howmany:
        left = cost - payEM
        intrest += left * Rapr
        count += 1

        end = intrest + cost

    os.system('cls')
    print()
    print("The cost of the loan is = " + str(end))
    print()
    print("Or (The cost of intrest : " + str(intrest) + ") + " "(amount you pay back : " + str(cost) + ") = (amount you pay back in total : " + str(end) + ")")
    input()
costofloan()

import random
import itertools

con = 0
end = 0
rolls = []
lessthen = False
morethen = False
sim = False
raw_roll = input("What roll? ")
#raw_roll = "2d6"
raw_len = len(raw_roll)

x = raw_roll.find(">")
y = raw_roll.find("<")
if x != -1:
    morethen = True
    con = raw_roll[x + 1:raw_len]
    con = int(con.strip())
    z = x
elif y != -1:
    lessthen = True
    con = raw_roll[y + 1:raw_len]
    con = int(con.strip())
    z = x

if raw_roll[0] == "(":
    endofroll = raw_roll.find(")")
    roll = raw_roll[1:endofroll]
    add = True
else:
    add = False
    if morethen or lessthen == True:
        roll = raw_roll[0:z]
    else:
        roll = raw_roll

#print(roll)
length = len(roll)
result = roll.find('d') + 1
print(length)
print(result)
print("")
print(morethen)
print("")
num1 = int(roll[0:result - 1])
num2 = int(roll[result:length + 1])
print("Seperation:")
print("")
print("How many die: ", num1)
print("")
print("How many sides on each die:", num2)
print("")



print("This is high:", con)
for i in range(num1):
    result = random.randint(1, num2)
    if add == True:
        end += result
        rolls.append(result)
    else:
        rolls.append(result)

print(rolls)
if end != 0:
    print(end)

########################################
#if morethen == True and add == False:
#        sim = True
#        for x in range(num1):
#            if con > x:
#                print(con)
#                print(x)
#                print("Success in total")
#            else:
#                print("Fail in total")

#if lessthen == True and add == False:
#        sim = True
#        for x in range(num1):
#            if con < x:
#                print(con)
#                print(x)
#                print("Success in total")
#            else:
#                print("Fail in total")
#########################################

if morethen == True and sim == False:
    if con <= end:
        print("Success")
    else:
        print("Fail!")
if lessthen == True and sim == False:
    if con >= end:
        print("Success")
    else:
        print("Fail!")

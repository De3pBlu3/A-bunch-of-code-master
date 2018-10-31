#Setting as var to make it easy to change
x = 3
y = 5

# Defining the fizzbuzz function
def fizzbuzz(n):

    if n % x == 0 and n % y == 0:
        return 'FizzBuzz'
    elif n % x == 0:
        return 'Fizz'
    elif n % y == 0:
        return 'Buzz'
    else:
        return str(n)

#printing 1 - 100 while running the fizzbuzz function
print "\n".join(fizzbuzz(n) for n in xrange(1, 101))

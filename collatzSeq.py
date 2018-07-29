def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return(number // 2)
    elif number % 2 == 1:
        print(number)
        return(3 * number + 1)

number = None;
while number == None:
    print('Enter number:')
    try:
        number = int(input())
    except ValueError:
        print('You need to enter an integer.')

while number != 1:
    number = collatz(number)

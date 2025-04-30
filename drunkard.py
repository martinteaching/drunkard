import random

# Because we need two integers, keep looping until the user gives us those two integers (rather than, say, one or more strings).
while True:
    try:
        # Cast each input as an integer, and if either fails, the exception will simply bring us back to the top of the loop.
        width = int(input('Enter width of space: '))
        height = int(input('Enter height of space: '))
        # If we succeed in converting two integers from the input, break from (exit) the loop.
        break
    # Exceptions can have different 'types'. This is the type of exception we know is 'thrown' when trying to convert a non-integer string to an integer, so we explicitly listen for it.
    except ValueError:
         # We need to list something for the exception to adhere to Python's rules, but we don't need to do anything (we'll go back to the top of the loop automatically), so just add pass, which does nothing.
        pass
x = 0
y = 0
path = []
while x != width - 1 or y != height - 1:
    choice = random.randint(0, 3)
    if choice == 0 and y < height - 1:
        y += 1
    elif choice == 1 and x < width - 1:
        x += 1
    elif choice == 2 and y > 0:
        y -= 1
    elif choice == 3 and x > 0:
        x -= 1
    path.append('(' + str(x) + ',' + str(y) + ')')
print('Drunkard path: ' + str(path))
print('Final position: (' + str(x) + ',' + str(y) + ').')

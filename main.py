# Import class Drunkard from the drunkard module
from drunkard import Drunkard

# Create a new copy (instance) of our class - an object.
drunkard = Drunkard()

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

# Keep moving the drunkard until they reach home.
path = drunkard.go_home(width, height)
# Report the drunkard's path to the user.
print('Drunkard path: ' + str(path))
# Report on the drunkard's final position.
print('Final position: (' + str(drunkard.get_x()) + ',' + str(drunkard.get_y()) + ').')
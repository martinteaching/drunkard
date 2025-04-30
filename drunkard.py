import random

width = int(input('Enter width of space: '))
height = int(input('Enter height of space: '))
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

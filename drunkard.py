import random


class Drunkard:

    # The size of our 2D space is provided as two parameters, a width and a height.
    # Adding `self` allows us to access data that is held in the copy (instance) of the class (the object).
    # Even if not used, this explicitly states that this method needs to be accessed by creating an instance of this code as an object.
    def go_home(self, width, height):
        # We know our drunkard always starts at position 0, so represent this here.
        # Double underscore indicates that this is *not* something that should be accessed from outside the class (a private property), which is good coding practice.
        # This is something that it would be good to include in something called a 'constructor', something that runs every time we make an instance of a class.
        self.__x = 0
        self.__y = 0
        # We want to track the drunkard's path, so define a variable with multiple 'slots' (an 'array') that we can use to store the path.
        path = []
        # We know the drunkard has more steps to make while their current position is not equal to home (the maximum point), on either the X or Y axis. We represent this as a repeating loop.
        while self.__x != width - 1 or self.__y != height - 1:
            # To represent the drunkard's random choice we use a method, randint, from the random module. The drunkard has four choices (up, right, down, left) so we generate a number in the range 0 - 3 (inclusive) to represent each of these.
            choice = random.randint(0, 3)
            # If the random number (choice) is 0, we say the drunkard chooses to move up, however can only do so if they are not at the top of the 2D space. We represent this with respective conditions.
            if choice == 0 and self.__y < height - 1:
                self.__y += 1
            # The above logic repeats for the drunkard moving right, down and up with three additional clauses to the conditional.
            elif choice == 1 and self.__x < width - 1:
                self.__x += 1
            elif choice == 2 and self.__y > 0:
                self.__y -= 1
            elif choice == 3 and self.__x > 0:
                self.__x -= 1
            path.append('(' + str(self.__x) + ',' + str(self.__y) + ')')
        return path

    # 'Accessor methods', for both the X and Y coordinate, allow us to access the drunkard's position at any time.
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

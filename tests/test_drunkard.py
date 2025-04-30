# Filename: must being with 'test' in order to be picked up by python unittest module.
import unittest
from drunkard import Drunkard


# Inherit from 'TestCase', so that we can (A) access some useful functions that have already been defined in the parent class (e.g. 'assertEqual') and (B) override (re-define and replace the functionality of) certain functions that are going to be called when running the test (e.g. setUp).
class TestDrunkard(unittest.TestCase):

    # We know a function with this named will be called when the object is executed by the unittest module, so if we 'intercept' this call by adding a function with the same name, we can automatically run our code instead.
    # Note: some library classes break typical Python naming conventions, e.g. camelCase instead of snake_case.
    def setUp(self):
        # Define a storage space within the object of this class to store a copy of our drunkard code. This can then be subsequently accessed from our test methods.
        self.__drunkard = Drunkard()

    # Test: Ensure that the drunkard eventually reaches home (standard case)
    # Test method must begin with the word 'test' in order to be picked up
    def testGoHome(self):
        # Go home with a regular 2D space
        self.__drunkard.go_home(4, 4)
        self.assertEqual(self.__drunkard.get_y(), 3)

    # Test: Even with a larger grid, the drunkard eventually reaches home (edge case)
    def testMoveLarge(self):
        # Go home with a larger 2D space
        self.__drunkard.go_home(100, 100)
        self.assertEqual(self.__drunkard.get_y(), 99)

    # Test: Ensure the drunkard does move (negative case)
    def testNegative(self):
        self.__drunkard.go_home(4, 4)
        # It should *not* be the case that the drunkard *doesn't* move
        self.assertNotEqual(self.__drunkard.get_y(), 0)

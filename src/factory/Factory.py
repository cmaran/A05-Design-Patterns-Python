__author__ = 'cmaran'

"""Implementation of the abstract factory pattern"""

import random
from factory import CircleFactory, SquareFactory

class ShapeCreator:

    """A Shape Creator"""

    def __init__(self, f=None):
        """
        shapeFactory is our factory.
        """

        self.shapeFactory = f

    def showShape(self):
        """
        Creates and shows a shape using factory
        """

        shape = self.shapeFactory.getShape()
        print("We have a {}".format(shape))
        print("It has got {}".format(self.shapeFactory.getCorners()))


# Create the proper family
def getFactory():
    """
   returns a random selection of our factorys
    """
    return random.choice([CircleFactory.CircleFactory, SquareFactory.SquareFactory])()


if __name__ == "__main__":
    for i in range(5):
        creator = ShapeCreator(getFactory())
        creator.showShape()
        print("=" * 20)


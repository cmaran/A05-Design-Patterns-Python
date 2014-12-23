__author__ = 'cmaran'

from factory import Square

class SquareFactory:

    def getShape(self):
        """
        returns the shape
        """
        return Square.Square()

    def getCorners(self):
        """
        returns the number of corners
        """
        return "4 Corners"
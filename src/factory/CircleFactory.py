__author__ = 'cmaran'

from factory import Circle

class CircleFactory:

    def getShape(self):
        """
        returns the shape
        """
        return Circle.Circle()

    def getCorners(self):
        """
        returns the number of corners
        """
        return "0 Corners"
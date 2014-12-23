__author__ = 'cmaran'

class Car(object):

    def __init__(self):
        self.name = "Car"

    def make_noise(self, octane_level):
        """HAHAHA"""
        return "vroom{0}".format("!" * octane_level)

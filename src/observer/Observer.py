__author__ = 'mdorfinger'


class Observer():
    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def notify(message):
        print(message)
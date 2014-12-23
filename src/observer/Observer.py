__author__ = 'mdorfinger'

"""
Die Klasse Observer erstellt einen neuen Observer. Dieser kann dann ins Observable hinzugefügt werden.
"""


class Observer(object):
    def __init__(self):
        pass

    def update(self, message):
        pass


"""
Die Klasse ConcreteObserver erstellt einen konkreten Observer.
"""


class ConcreteObserver(Observer):
    """
    Die Methode notify benachrichtigt den konkreten Observer mit einer Message (Message wird im Observable festgelegt).
    """
    def update(self, message):
        print(message)
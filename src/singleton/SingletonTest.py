__author__ = 'mdorfinger'

from singleton import Singleton

@Singleton.Singleton  # Die Klasse die nach dem @Singleton steht, wird dann im Konstruktor aufgerufen
class SingletonTest:
    def __init__(self):
        pass

a = SingletonTest()  # es werden 2 mal SingletonTests erstellt um zu überprüfen ob sie gleich sind (gleiche Instanz)
b = SingletonTest()
print(a is b)  # True > Instance ist gleich > Singleton funktioniert
print(a)  # man kann nun sehen, dass die Speicherstelle bei a und b gleich ist
print(b)


class SingletonTest:  # diese Klasse hat kein @Singleton
    def __init__(self):
        pass

a = SingletonTest()
b = SingletonTest()
print('\n',a is b)  # false, weil kein Singleton
print(a)  # man kann sehen, dass die Speicherstelle unterschiedlich ist
print(b)

__author__ = 'mdorfinger'

"""

Das Singleton-Pattern sorgt dafür, dass nur eine instance der Klasse erstellt wird

"""
class Singleton():

    def __init__(self, klasse):
        self.klasse = klasse
        self.instance = None # beim ersten Aufruf ist die Instance none

    def __call__(self, *args, **kwargs):
        if self.instance == None: # man überprüft beim Aufruf, instance none ist
            self.instance = self.klasse(*args, **kwargs) # wenn ja, wird die Klasse neu erstellt
        return self.instance # die instance wird zurückgegeben


@Singleton
class SingletonTest:
    def __init__(self):
        print()

f = SingletonTest() # es werden 2 mal SingletonTests erstellt um zu überprüfen ob sie gleich sind.
g = SingletonTest()

print(f is g) # True > Instance ist gleich > Singleton funktioniert
print(f) # man kann nun sehen, dass die Speicherstelle bei f und g gleich ist
print(g)


class SingletonTest: # diese Klasse hat kein @Singleton
    def __init__(self):
        print()

f = SingletonTest()
g = SingletonTest()

print(f is g) # false, weil kein Singleton
print(f) # man kann sehen, dass die Speicherstelle unterschiedlich ist
print(g)
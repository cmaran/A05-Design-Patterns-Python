__author__ = 'mdorfinger'

"""

Das Singleton-Pattern sorgt dafür, dass nur eine instance der Klasse erstellt wird

"""
class Singleton():

    def __init__(self, klasse): # Klasse ist die, die nach dem @Singleton steht
        self.klasse = klasse
        self.instance = None # beim ersten Aufruf ist die Instance none

    def __call__(self):
        if self.instance == None: # man überprüft beim Aufruf, instance none ist
            self.instance = self.klasse() # wenn ja, wird die Klasse neu erstellt
        return self.instance # die instance wird zurückgegeben


@Singleton
class SingletonTest:
    def __init__(self):
        print()

a = SingletonTest() # es werden 2 mal SingletonTests erstellt um zu überprüfen ob sie gleich sind (gleiche Instanz)
b = SingletonTest()

print(a is b) # True > Instance ist gleich > Singleton funktioniert
print(a) # man kann nun sehen, dass die Speicherstelle bei a und b gleich ist
print(b)


class SingletonTest: # diese Klasse hat kein @Singleton
    def __init__(self):
        print()

a = SingletonTest()
b = SingletonTest()

print(a is b) # false, weil kein Singleton
print(a) # man kann sehen, dass die Speicherstelle unterschiedlich ist
print(b)
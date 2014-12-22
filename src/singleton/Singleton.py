__author__ = 'mdorfinger'

"""
Das Singleton-Pattern sorgt dafür, dass nur eine Instanz der Klasse erstellt wird.
"""
class Singleton():

    """
    In der Init-Methode wird die Instance auf None gestellt, außerdem bekommt man die Klasse.
    """
    def __init__(self, klasse): # Klasse ist die, die nach dem @Singleton steht
        self.klasse = klasse
        self.instance = None # beim ersten Aufruf ist die Instance none

    """
    In der Call-Methode wird überprüft, ob die Klasse schon eine Instanz ist. Wenn sie noch keine Instanz ist, wird
    eine neue erstellt. Die Instanz wird zurückgegeben.
    """
    def __call__(self):
        if self.instance == None: # man überprüft beim Aufruf, instance none ist
            self.instance = self.klasse() # wenn ja, wird die Klasse neu erstellt
        return self.instance # die instance wird zurückgegeben


@Singleton # Die Klasse die nach dem @Singleton steht, wird dann im Konstruktor aufgerufen
class SingletonTest:
    def __init__(self):
        pass

a = SingletonTest() # es werden 2 mal SingletonTests erstellt um zu überprüfen ob sie gleich sind (gleiche Instanz)
b = SingletonTest()
print(a is b) # True > Instance ist gleich > Singleton funktioniert
print(a) # man kann nun sehen, dass die Speicherstelle bei a und b gleich ist
print(b)



class SingletonTest: # diese Klasse hat kein @Singleton
    def __init__(self):
        pass

a = SingletonTest()
b = SingletonTest()
print('\n', a is b) # false, weil kein Singleton
print(a) # man kann sehen, dass die Speicherstelle unterschiedlich ist
print(b)
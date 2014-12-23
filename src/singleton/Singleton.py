__author__ = 'mdorfinger'

"""
Das Singleton-Pattern sorgt dafür, dass nur eine Instanz der Klasse erstellt wird.
"""


class Singleton():
    """
    In der Init-Methode wird die Instance auf None gestellt, außerdem bekommt man die Klasse.
    """

    def __init__(self, klasse):  # Klasse ist die, die nach dem @Singleton steht
        self.klasse = klasse
        self.instance = None  # beim ersten Aufruf ist die Instance none

    """
    In der Call-Methode wird überprüft, ob die Klasse schon eine Instanz ist. Wenn sie noch keine Instanz ist, wird
    eine neue erstellt. Die Instanz wird zurückgegeben.
    """

    def __call__(self):
        if self.instance == None:  # man überprüft beim Aufruf, instance none ist
            self.instance = self.klasse()  # wenn ja, wird die Klasse neu erstellt
        return self.instance  # die instance wird zurückgegeben
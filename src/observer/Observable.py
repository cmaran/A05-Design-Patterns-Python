__author__ = 'mdorfinger'

"""
Die Klasse Observable erstellt ein Observable mit den Methoden add, delete und notifyall.
"""


class Observable(object): # da es in Python keine Interfaces gibt wird es so gelöst, dass alle Methoden ein pass beinhalten
    def __init__(self, *args, **kwargs):
        pass

    def add_observer(self, name, observer):
        pass

    def delete_observer(self, name, observer):
        pass

    def notify_all(self, *args, **kwargs):
        pass


"""
Die Klasse ConcreteObservable erstellt ein konkretes Observable. Darin können verschiedene Observer hinzugefügt, gelöscht oder benachrichtigt werden.
"""


class ConcreteObservable(Observable):
    """
    In der Init Methode wird die _observers - Liste leer angelegt. Außerdem wird der super-Konstruktor aufgerufen.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._observers = []

    """
    Mit der add_observer Methode wird ein Observer hinzugefügt.
    """
    def add_observer(self, name, observer):
        if observer not in self._observers: # observer nur hinzugefügt wenn noch nicht vorhanden
            self._observers.append(observer)
            print('add observer', name)
        else:
            print('Observer',name, 'kann nicht hinzugefügt werden.')

    """
    Mit der delete_observer Methode wird ein Observer gelöscht.
    """
    def delete_observer(self, name, observer):
        if observer in self._observers: # observer nur gelöscht wenn noch nicht vorhanden
            self._observers.remove(observer)
            print('delete observer', name)
        else:
            print('Observer kann nicht gelöscht werden.')

    """
    Mit der notify_all Methode werden alle Observer mit einer Massage benachrichtigt.
    """
    def notify_all(self, message):
        for observer in self._observers: #allen observer wird eine Nachricht gesendet
            observer.notify(message)
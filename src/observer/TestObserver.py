__author__ = 'mdorfinger'

from observer import Observable, Observer

"""
Die Klasse TestObserver testet die 2 anderen Klasse und das Prinzip des Observer-Patterns. Dazu wird ein Observable
und 3 Observers erstellt
"""


class TestObserver():
    obs = Observable.ConcreteObservable()  # ein konkretes Observable wird erstellt
    concrete_observer1 = Observer.ConcreteObserver()  # 3 Observer werden erstellt
    concrete_observer2 = Observer.ConcreteObserver()
    concrete_observer3 = Observer.ConcreteObserver()
    obs.add_observer(1, concrete_observer1)  # und zum Observable hinzugefügt
    obs.add_observer(2, concrete_observer2)
    obs.add_observer(3, concrete_observer3)
    obs.notify_all('message to all observer') # Nachricht muss 3 mal gesendet werden (an 3 Observer)
    obs.remove_observer(1, concrete_observer3)  # Observer 3 wird gelöscht
    obs.notify_all('message to all observer') # die Nachricht muss 2 mal gesendet werden (2 Observer gibt es noch)

    # zum testen wird observer 1 nochmal hinzugefügt
    obs.add_observer(1, concrete_observer1)
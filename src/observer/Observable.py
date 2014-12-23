__author__ = 'mdorfinger'


class Observable():
    def __init__(self, *args, **kwargs):
        self._observers = []

    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def delete_observer(self, observer):
            self._observers.remove(observer)

    def notify_observers(self, message):
        for obs in self._observers:
            obs.notify(message)

    def send_message(self, message):
        self.notify_observers(message)
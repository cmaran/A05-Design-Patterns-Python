__author__ = 'mdorfinger'

from observer import Observable, Observer


class TestObserver():
    @staticmethod
    def main():
        obs = Observable.Observable()

        a = Observer.Observer()
        b = Observer.Observer()
        c = Observer.Observer()

        obs.add_observer(a)
        obs.add_observer(b)
        obs.add_observer(c)

        obs.delete_observer(b)

        obs.notify_observers()

        obs.send_message('testi')
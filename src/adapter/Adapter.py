__author__ = 'cmaran'


from adapter import Dog, Human, Car, Cat


class Adapter(object):

    def __init__(self, obj, adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self.obj, attr)


def main():
    objects = []
    dog = Dog.Dog()
    objects.append(Adapter(dog, dict(make_noise=dog.bark)))
    cat = Cat.Cat()
    objects.append(Adapter(cat, dict(make_noise=cat.meow)))
    human = Human.Human()
    objects.append(Adapter(human, dict(make_noise=human.speak)))
    car = Car.Car()
    objects.append(Adapter(car, dict(make_noise=lambda: car.make_noise(3))))

    for obj in objects:
        print("A {0} goes {1}".format(obj.name, obj.make_noise()))


if __name__ == "__main__":
    main()
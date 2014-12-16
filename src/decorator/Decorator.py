__author__ = 'cmaran'


class Student(object):
    """
    Student

    :param String fName: First name
    :param int sName: Surname
    """

    def __init__(self, fName, sName):
        """
        constructor

        :param String fName: First name
        :param int sName: Surname
        """
        self.fName = fName
        self.sName = sName

    def paragraph_decorate(func):
        """
        decorator-function for paragraphs

        decorates the given name with Paragraph-Tags
        """
        def func_wrapper(*args, **kwargs):
            return "<p>{0}</p>".format(func(*args, **kwargs))

        return func_wrapper

    def italic_decorate(func):
        """
        decorator-function for paragraphs

        decorates the given name with Italic-Tags
        """
        def func_wrapper(*args, **kwargs):
            return "<i>{0}</i>".format(func(*args, **kwargs))

        return func_wrapper

    def strong_decorate(func):
        """
        decorator-function for paragraphs

        decorates the given name with Strong-Tags
        """
        def func_wrapper(*args, **kwargs):
            return "<strong>{0}</strong>".format(func(*args, **kwargs))

        return func_wrapper

    def bold_decorate(func):
        """
        decorator-function for paragraphs

        decorates the given name with Bold-Tags
        """
        def func_wrapper(*args, **kwargs):
            return "<b>{0}</b>".format(func(*args, **kwargs))

        return func_wrapper

    @paragraph_decorate
    @italic_decorate
    @bold_decorate
    @strong_decorate
    def get_fullname(self):
        return "First name:" + self.fName + " Surname:" + self.sName


yolo = Student("Peter", "Lustig")
babo = Student("Max", "Mustermann")
swag = Student("Tester", "Tesperson")

print(yolo.get_fullname())
print(swag.get_fullname())
print(babo.get_fullname())
class View:
    def __init__(self):
        self.view1 = None
    def hello(self):
        print("hello")

class Model:
    def __init__(self):
        self.__view = None
    def attach_view(self, v):
        self.__view = v
    def any_function(self):
        self.__view.hello()

class Controller:
    def __init__(self):
        self.model = model.Model()
        self.model.attach_view(v)

c = Controller()
c.model.attach_view(v)

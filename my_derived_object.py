import myobject

class myDerivedObject(myobject.MyObject):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return self.greeting 

from field_class import Field

class Name(Field):
    def __init__(self, name):
        self.value = name

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, name):
        if len(name) > 0:
            self.__value = name
        else:
            raise ValueError('Contact should have name')
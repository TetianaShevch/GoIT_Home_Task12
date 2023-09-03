from field_class import Field

class Phone(Field):
    def __init__(self, phone):
       self.value = phone

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, phone):
        if 15 >= len(phone) and 9 <= len(phone):
            self.__value = phone
        else:
            raise ValueError('Phone is not correct')   
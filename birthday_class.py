from field_class import Field
from datetime import datetime

class BirthDay(Field):
    def __init__(self, birthday):
        self.__value = None
        self.value = birthday

    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, birthday: str):
        if len(birthday) > 0:
            try:
                self.__value = datetime.strptime(birthday, '%d.%m.%Y')
                
            except Exception:
                raise ValueError('Data of birhday should have formate dd.mm.yyyy')
        else:
            print('The date of birthday is unknown')
    
        
class Field():
    def __init__(self, value):
        self.value = value
        
    @staticmethod
    def valid_value(value):
        if type(value) != str:
            raise TypeError('received data must be STR')
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value: str) -> None:
        self.valid_value(value)
        self.__value = value
    
    def __str__(self) -> str:
        return f'{self.value}'
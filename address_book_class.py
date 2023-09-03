from collections import UserDict
from record_class import Record
from name_class import Name
import pickle

class AddressBook(UserDict):
    def __init__(self, n = 3):
        super().__init__()
        self.counter = 0
        self.n = n
        self.file = 'Address_Book.bin' 

    def __saving_address_book(self): # Метод збереження даних адресної книги на диск (файл Address_Book.bin).
        with open(self.file, 'wb') as fl:
            pickle.dump((self.data), fl)

             
    def loading_address_book(self, file): # Метод завантаження даних адресної книги з диску (файлу Address_Book.bin).
        with open(file, 'rb') as fl:
            self.data = pickle.load(fl)
        
        
    def add_record(self, record = Record):
        self.data[record.name.value] = record 
        print(f'Contact of {record.name.value} was added')
        self.__saving_address_book() # викликається метод збереження адресної книги на диск при додаванні запису.

    def __next__(self):
        if self.n > len(self.data):  
            self.n = len(self.data) 
        result = ""
        i = 0
        if self.counter < len(self.data):
            for record in self.data.values():  
                if i < self.counter//self.n * self.n:  
                    i += 1                             
                    continue                           
                result += str(record)
                self.counter += 1
                if not self.counter % self.n:  
                    return result
                elif self.counter == len(self.data):  
                    return result
        else: 
            raise StopIteration
            
     
    def __iter__(self):
        return self
    
    
                    

            
        
    
    
        
    
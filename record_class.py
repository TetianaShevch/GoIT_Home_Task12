from name_class import Name
from phone_class import Phone
from birthday_class import BirthDay
from datetime import date

class Record():
    
    def __init__(self, name: Name, phone: Phone = None, birthday = None): # телефон і дата народження не є обовязковими агрументами, тому можуть бути і None
        self.name = name
        self.phones = [] # по замовчюванню створимо пустий список
        self.birthday = birthday
        if phone:
            self.phones.append(phone)  # якщо телефон задано, то додамо його в список
    
    def days_to_birthday(self):
        """
        Метод days_to_birthday() для кожного запису друкує й передає, скільки днів залишилось до дня народження. 
        Якщо день народження невідомий, метод days_to_birthday() друкує відповідне повідомлення.
        """
        if self.birthday: # якщо день народження відомо, то підраховуємо кількість днів до наступного дня народження 
            today = date.today()
            dt = date(today.year, self.birthday.value.month, self.birthday.value.day)
            difference = (dt - today).days
            number_of_days = difference if difference >= 0 else (365 + difference)
            # print(f"The {self.name}'s birthday will be after {number_of_days} days")
            return number_of_days
        else:
            print("The contact's birthday is unknown.") # якщо день народження невідомий, друкуємо відповідне повідомлення.
    
    def __str__(self):
        """
        Метод визначає, в якій формі будуть формуватися записи при конвертації у рядок.
        """
        birthday_str = str(date(self.birthday.value.year, self.birthday.value.month, self.birthday.value.day)) if self.birthday != None else "-"
        phones_str = " ".join([ph.value for ph in self.phones]) if self.phones else "-"
        return f'{self.name} -->> phone(s): {phones_str}; birthday: {birthday_str}'
    
    def add_phone(self, phone: Phone):
        for i in self.phones:
            if i == phone:
                print('Phone is already in Address Book') # якщо телефон вже є в списку
                return
        self.phones.append(phone)  # якщо телефона в списку немає, додамо його в список
        print('Phone was added')
        
    def del_phone(self, phone: Phone):
        for i in self.phones:
            if i == phone:
                self.phones.remove(i) # якщо телефон в списку, видаляємо його
                print(f'Phone was removed')
                return
        print('Phone is not in Address Book') # якщо телефона немає в списку

    def change_phone(self, old_phone: Phone, new_phone: Phone):
        for i in self.phones:
            if i == old_phone:
                i = new_phone  #  якщо телефон в списку, змінюємо його
                print(f'Phone was changed')
                return
        print('Phone is not in Address Book') # якщо телефона немає в списку
    


    
    
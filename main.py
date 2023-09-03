"""
Починаючи роботу, пробуємо загрузити адресну книгу ab з файлу Address_Book.json.
Якщо такого файду не існує, Створюємо адресну книгу ab як екземпляр класу AddressBook. 
Заносимо в адресну книгу 5 контактів, для кожного контакта отримуємо й друкуємо, 
скільки днів залишилось до дня народження (days_to_birthday()). 
Якщо день народження невідомий, функція days_to_birthday() друкує відповідне повідомлення.

Запускаємо ітератор по адресній книзі для виводу заданої в конструкторі класу AddressBook кількості записів. 
Щоб вивести наступну порцію записів, просимо натиснути "enter".

"""

from address_book_class import AddressBook
from record_class import Record
from name_class import Name
from phone_class import Phone
from birthday_class import BirthDay
from faker import Faker, Factory 
import pathlib

if __name__ == "__main__":
    
    ab = AddressBook()
    if pathlib.Path(ab.file).is_file():
        try:
            ab.loading_address_book(ab.file) 
        except:
            print('The file is broken or empty')   

    # print('Name1')
    # name1 = Name('Bill')
    # phone1 = Phone('+3805012345670')
    # birthday1 = BirthDay('21.07.1970')
    # rec1 = Record(name1, phone1, birthday1) 
    # ab.add_record(rec1) # записуємо контакт Bill в адресну книгу
    # assert isinstance(ab['Bill'].birthday, BirthDay) 
    # rec1.days_to_birthday() # друкуємо кількість днів до дня народження
        
    print('Name2')
    name2 = Name('Mary')
    # phone2 = Phone('05023456709')
    birthday2 = BirthDay('12.12.2003')
    rec2 = Record(name2, birthday=birthday2)
    ab.add_record(rec2)
    rec2.days_to_birthday()

    # print('Name3')
    # name3 = Name('John')
    # phone3 = Phone('05023456709')
    # birthday3 = BirthDay('28.08.2003')
    # rec3 = Record(name3, phone3, birthday=birthday3)
    # ab.add_record(rec3)
    # new_phone3 = Phone('0976543645')
    # rec3.add_phone(new_phone3)
    # rec3.days_to_birthday()

    # print('Name4')
    # rec4 = Record(Name('Mike'), Phone('+380671233434'))
    # ab.add_record(rec4)
    # rec4.days_to_birthday()

    # print('Name5')
    # rec5 = Record(Name('Tom'), birthday=BirthDay('02.09.2018'))
    # ab.add_record(rec5)
    # new_phone5 = Phone('+380885436456')
    # rec5.add_phone(new_phone5)
    # rec5.days_to_birthday()
    
    
    for n_records in ab: # Запускаємо ітератор по адресній книзі для вивода заданої кількості записів. 
        print(n_records)
        input('Press "enter" for continue') # Щоб отримати наступну порцію записів, просимо натиснути клавішу "enter".
    
    # new_phone = Phone('5778890')
    # rec.add_phone(new_phone)
    # mistaken_phone = Phone('789000')
    # rec.del_phone(mistaken_phone)
    # rec.del_phone(new_phone)
    # rec.add_phone(mistaken_phone)
    # rec.change_phone(mistaken_phone,new_phone)

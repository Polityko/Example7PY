# Задача 1. Создайте телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах

from tkinter import *

def add_contact():
    new_contact = '{name} {surname}: {phone}'\
         .format(name=entryName.get(), surname=entrySurname.get(), phone=entryPhone.get())
    allContacts.insert(END, new_contact)
    write_contacts()

def delete_contact():
    select = allContacts.curselection()
    allContacts.delete(select[0])
    write_contacts()

def write_contacts():
    data  = open('phonebook.txt', 'w', encoding='utf-8')
    for row in allContacts.get(0, END):
        data.writelines(row + '\n')
    data.close()

def print_contacts():
    data  = open('phonebook.txt', 'r', encoding='utf-8')
    for contact in data.readlines():
        allContacts.insert(END, contact)
    data.close()

root = Tk()

buttonAddContact = Button(root, text='Добавить контакт', command=add_contact)
buttonAddContact.grid(row=3, column=0, columnspan=2)
buttonDeleteContact = Button(root, text='Удалить контакт', command=delete_contact)
buttonDeleteContact.grid(row=4, column=1)

labelName = Label(root, text='Введите имя')
labelName.grid(row=0, column=0)
labelSurname = Label(root, text='Введите фамилию')
labelSurname.grid(row=1, column=0)
labelPhone = Label(root, text='Введите номер телефона')
labelPhone.grid(row=2, column=0)

entryName = Entry(root, width=15)
entryName.grid(row=0, column=1)
entrySurname = Entry(root, width=15)
entrySurname.grid(row=1, column=1)
entryPhone = Entry(root, width=15)
entryPhone.grid(row=2, column=1)

allContacts = Listbox(root, height=8, width=45, selectmode=EXTENDED)
allContacts.grid(row=4, column=0)

print_contacts()

root.mainloop()
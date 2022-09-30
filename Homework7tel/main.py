import controller as c

filename = 'PhoneBook.csv' 
myfile = open(filename, 'a+') 
myfile.close

c.main_menu(filename)
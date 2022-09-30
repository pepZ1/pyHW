def newcontact(filename): 
    firstname = input('Введите ваше имя: ')
    lastname = input('Введите вашу фамилию: ')
    phoneNum = input('Введите ваш номер телефона: ') 
    emailID = input('Введите ваш E-mail: ') 
    contactDetails = (f'{firstname} {lastname};{phoneNum};{emailID}\n')
    myfile = open(filename, "a") 
    myfile.write(contactDetails) 
    print(f'Запись {contactDetails} успешно добавлена!')
    myfile.close 
    enter = input("Для продолжения нажмите Enter") 
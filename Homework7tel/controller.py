import ExeMenuCom as Commands

def main_menu(filename):
    
    print('\nГЛАВНОЕ МЕНЮ\n1. Просмотреть все контакты\n2. Добавить новый контакт\n3. Выход') 
    
    choice = input('Выберите раздел: ')

    match choice:
        case '1':
            myfile = open(filename, "r+") 
            filecontents = myfile.read()
            if len(filecontents) == 0: 
                print('Нет информации') 
            else: 
                print(filecontents)
            myfile.close 
            enter = input("Для продолжения нажмите Enter") 
            main_menu(filename)

        case '2':
            Commands.newcontact(filename)
            main_menu(filename)

           
        
        case '3':
            print('Спасибо!')
fileName = 'HW python lesson 6/telephone directory.txt'


def writeFile(fileName):   #печать в файл
    with open(fileName, 'a') as data:
        data.writelines(input('ввод нового контакта в формате ФИО номер тебефона черз запятую: ') + '\n') # ("сообщение", "перенос на новую строку")
# writeFile(fileName)

def readFile(fileName): #чтение файла
    result = []
    with open(fileName, 'r+') as data:
        for Line in data:
            result.append(Line.split())
    return result


def PrintDirectory(directory): # печать всей записной книжки
    for user in directory:
        print(user)

# PrintDirectory(readFile(fileName))


def findUsersName(directory): # печать записи по ключевому слову
    name = str(input('поиск конткта по имени: ')) + ','
    for user in directory:
        if user[0] == name or user[1] == name or user[2] == name:
            print(user)
        
# findUsersName(readFile(fileName))

def findUsersPhone(directory): # печать записи по ключевому слову
    Phone = str(input('поиск конткта по номеру телефона: '))
    for user in directory:
        if user[3] == Phone:
            print(user)

# findUsersPhone(readFile(fileName))


# name = str(input('поиск конткта по имени: ')) + ','
# for user in readFile(fileName):
#     if user[0] == name or user[1] == name or user[2] == name:
#         print(user)
#         with open(fileName, 'a') as data:





with open("HW python lesson 6/telephone directory.txt", "r") as f:
      
    
    data = f.readlines()
      

with open("HW python lesson 6/telephone directory.txt", "w") as f:
      
    for line in data :
          
        
        if line.strip("\n") != "Ivanov, Ivan, Ivanovich, +79111234567" : 
            f.write(line)


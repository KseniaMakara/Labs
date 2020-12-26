''' --------------------Завдання--------------------------
 5.	База даних поштарки. База даних абонементів: номер будинку,
    кількість газет, що виписуються, перелік назв газет, що виписуються.
    Організувати вибір за довільним запитом.
    Дані зберігаються в масиві записів, який створюється динамічно.   '''
# --------------------Solution---------------------------
Postman = []
def serch(choose, criteria):
    if choose == 1:
        for i in range(len(Postman)):
            if Byer[i]["House number "] == criteria:
                print(Postman[i])
    if choose == 2:
        for i in range(len(Byer)):
            if Byer[i]["Amount of magazines"] == criteria:
                print(Postman[i])
    if choose == 3:
        for i in range(len(Byer)):
            if Byer[i]["List of magazines"] == criteria:
                print(Postman[i])
while True:
    print("\n")
    print("1. All info\n"
          "2. Info about postman\n"
          "3. Find postman\n"
          "4. Exit\n")

    choose = int(input("Choose number:"))

    if choose == 1:
        print(Byer)
    elif choose == 2:

        '''----Info about postman----'''
        house_number = input("Enter house number: ")
        amount_of_magazines = int(input("Enter amount of magazines : "))
        list_of_magazines = input("Enter list of magazines: ")
        postmanDict = {"Adress": "", "Phone number": 0, "Specialization": "", "Time": 0}

        '''---Definition of the dictionary---'''
        postmanDict["House number"] = house_number
        postmanDict["Amount of magazines"] = amount_of_magazines
        postmanDict["List of magazines"] = list_of_magazines
        Postman.append(byerDict)
    elif choose == 3:
        print("Find:\n"
              "1.House number\n"
              "2.Amount of magazines\n"
              "3.List of magazines\n")
        choose2 = int(input(" Choose number: "))
        if choose2 == 1:
            searchCriteria = input("Choose house number: ")
            serch(1, searchCriteria)
        if choose2 == 2:
            searchCriteria = int(input(" Choose amount of magazines : "))
            serch(2, searchCriteria)
        if choose2 == 3:
            searchCriteria = int(input(" Choose list of magazines: "))
            serch(3, searchCriteria)
        print("\n")
    elif choose == 3:
        break
    else:
        print("Enter right number\n")
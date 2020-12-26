''' --------------------Завдання--------------------------
 5.	Довідник покупця. База торгівельних підприємств міста:
 назва, адреса та телефон, спеціалізація, час роботи. Організувати
 вибір магазину за довільним запитом. Дані зберігаються в масиві.'''
# --------------------Solution---------------------------
Byer = []
def serch(choose, criteria):
    if choose == 1:
        for i in range(len(Byer)):
            if Byer[i]["Address"] == criteria:
                print(Byer[i])
    if choose == 2:
        for i in range(len(Byer)):
            if Byer[i]["Phone"] == criteria:
                print(Byer[i])
    if choose == 3:
        for i in range(len(Byer)):
            if Byer[i]["Specialization"] == criteria:
                print(Byer[i])
    if choose == 4:
        for i in range(len(Byer)):
            if Byer[i]["Time"] == criteria:
                print(Byer[i])

while True:
    print("\n")
    print("1. All info\n"
          "2. Info about shop\n"
          "3. Find shop\n"
          "4. Exit\n")

    choose = int(input("Choose number:"))

    if choose == 1:
        print(Byer)
    elif choose == 2:

        '''----Info about shop----'''
        address = input("Enter address: ")
        phone_number = int(input("Enter phone number : "))
        specialization = input("Enter specialization: ")
        time = int(input("Enter time : "))
        byerDict = {"Adress": "", "Phone number": 0, "Specialization": "", "Time": 0}

        '''---Definition of the dictionary---'''
        byerDict["Adress"] = adress
        byerDict["Phone"] = phone_number
        byerDict[" specialization"] = specialization
        byerDict[" time"] = time
        Byer.append(byerDict)
    elif choose == 3:
        print("Find:\n"
              "1.Address\n"
              "2.Phone\n"
              "3.specialization\n"
              "4.time\n")
        choose2 = int(input(" Choose number: "))
        if choose2 == 1:
            searchCriteria = input("Choose address: ")
            serch(1, searchCriteria)

        if choose2 == 2:
            searchCriteria = int(input(" Choose phone : "))
            serch(2, searchCriteria)
        if choose2 == 3:
            searchCriteria = int(input(" Choose specialization: "))
            serch(3, searchCriteria)
        if choose2 == 4:
            searchCriteria = int(input("Choose time: "))
            serch(4, searchCriteria)
        print("\n")
    elif choose == 4:
        break
    else:
        print("Enter right number\n")
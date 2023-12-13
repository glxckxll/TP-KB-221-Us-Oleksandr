list = [
    {"name":"Вадим", "age":"24", "course":"2", "phone":"380975128898"},
    {"name":"Данило","age":"19", "course":"1","phone":"380710994999"},
    {"name":"Захар","age":"22", "course":"3", "phone":"380710994998"},
    {"name":"Іван","age":"21", "course":"2", "phone":"380508380180"},
    {"name":"Матвій","age":"26", "course":"4", "phone":"380954146429"},
    {"name":"Павло","age":"26", "course":"1", "phone":"380974104357"},
    {"name":"Тарас","age":"25", "course":"2", "phone":"380632541982"}
]

def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ", age is " + elem["age"] + ", course is " + elem["course"] + ", phone is " + elem["phone"]
        print(strForPrint)
    return


def addNewElement():
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    age = input("Please enter student age: ")
    course = input("Please enter student course: ")
    
    newItem = {"name": name, "age" : age, "course": course, "phone": phone}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break

    list.insert(insertPosition, newItem)
    print("New element has been added")
    return


def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break

    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Delete position", str(deletePosition))
        del list[deletePosition]
    return


def updateElement():
    name = input("Please enter name to be updated: ")
    found = False

    for index, item in enumerate(list):
        if item["name"] == name:
            found = True
            update_field = input("Enter the field to update (name, age, course, phone): ")
            new_value = input("Enter the new value: ")
            list[index][update_field] = new_value
            print("Element updated successfully")
            break

    if not found:
        print("Element with such name was not found")

def main():
    while True:
        chouse = input(
            "Please specify the action [ C create, U update, D delete, P print, X exit ] "
        )
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                break
            case _:
                print("Wrong chouse")
                main()


if __name__ == "__main__":
    main()
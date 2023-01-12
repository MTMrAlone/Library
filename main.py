from library import *
from formatting import color
from os import system

# Username is Codemeli
# Default Password 1111

lib = Library("Shariaati High-School", "Files/database.db")
panel_text = "Library Panel" + " (" + lib.name + ")"

while True:
    system("cls")
    print(color["info"], panel_text)
    print(color["info"], "=" * len(panel_text))
    print(color["info"], "1. Create user")
    print(color["info"], "2. Edit user")
    print(color["info"], "3. View user")  # Not Complete
    print(color["info"], "4. Get user id")
    print(color["info"], "=" * len(panel_text))
    print(color["info"], "5. Create book")  # Not Complete
    print(color["info"], "6. Edit book")  # Not Complete
    print(color["info"], "7. View book")  # Not Complete
    print(color["info"], "8. Get book id")  # Not Complete
    print(color["info"], "=" * len(panel_text))
    print(color["info"], "9. View logs")
    print(color["info"], "10. Rent book")
    print(color["info"], "11. Back rent book")
    print(color["info"], "12. View expired rents")
    print(color["info"], "13. Revival rent book")
    print(color["info"], "=" * len(panel_text))

    try:
        q = int(input(color["question"] + " Input: "))
    except ValueError:
        system("cls")
        continue

    if q == 1:
        system("cls")
        username = input(color["question"] + " *Username (Codemeli): ")
        phone = input(color["question"] + " *Phone (Telephone Hamrah): ")
        name = input(color["question"] + " *Name (Nam): ")
        family = input(color["question"] + " *Family (Nam Khanevadegi): ")
        birthday = input(color["question"] + " *Birthday (Tarikh Tavalod Miladi): ")
        nclass = input(color["question"] + " *Class Number (Shomareh Class): ")
        fname = input(color["question"] + " *Father Name (Nam Pedar): ")
        email = input(color["question"] + " Email: ")
        school = input(color["question"] + " School Name (Nam Madrese): ")

        if (len(username) != 10) or (len(phone) != 11):
            print(color["failed"], "Your entered value not valid.")
            input("(press enter for back to menu)")
            continue
        if email == "":
            email = False
        if school == "":
            school = "Shariaati High-School"

        lib.add_user(username, phone, name, family, birthday, nclass, fname, school, email)
        print(color["success"], "User created.")
        input("(press enter for back to menu)")
    elif q == 2:
        system("cls")
        uid = input(color["question"] + " Enter user ID: ")
        table = input(color["question"] + " Enter user table: ")
        value = input(color["question"] + " Enter user value: ")

        if table == "class" or table == "password" or table == "book" or table == "in" or table == "out" or \
                table == "level":
            vtype = "int"
        else:
            vtype = "str"
        lib.edit_user(uid, table, value, vtype)
        print(color["success"], "ID", uid, "was edited.")
        input("(press enter for back to menu)")
    elif q == 3:
        pass
    elif q == 4:
        system("cls")
        username = input(color["question"] + " Enter username: ")

        try:
            uid = lib.get_user_id(str(username))
        except IndexError:
            print(color["failed"], "Your entered username not valid.")
        else:
            print(color["success"], username, "ID :", str(uid))
        input("(press enter for back to menu)")
    else:
        continue

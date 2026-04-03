# python-practice-month3
Python File Handling + CRUD System Practice


def add():
    name = input("Name: ")
    marks = input("Marks: ")

    with open("students.txt", "a") as f:
        f.write(name + "," + marks + "\n")

    print("Added")


def view():
    try:
        with open("students.txt", "r") as f:
            data = f.readlines()

        print("\n--- List ---")
        for line in data:
            print(line.strip())

    except:
        print("No file")


def delete():
    try:
        with open("students.txt", "r") as f:
            data = f.readlines()

        name = input("Enter name to delete: ")

        with open("students.txt", "w") as f:
            for line in data:
                if not line.startswith(name + ","):
                    f.write(line)

        print("Deleted")

    except:
        print("No file")


def run():
    while True:
        print("\n1 Add")
        print("2 View")
        print("3 Delete")
        print("4 Exit")

        c = int(input("Choice: "))

        if c == 1:
            add()
        elif c == 2:
            view()
        elif c == 3:
            delete()
        elif c == 4:
            break
        else:
            print("Invalid")


run()

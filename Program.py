import json
import csv_data
import json_data

persons = json_data.read_file()


def main():
    while True:
        print(70 * "-")
        choice = input("\t\tWelcome, please choose a menu\n\n"
                       "\t\t1. Read in Original file (person.csv)\n"
                       "\t\t2. Show JSON-data \n"
                       "\t\t3. Add Person\n"
                       "\t\t4. Delete Person\n"
                       "\t\t5. Save File\n"
                       "\t\t6. Exit\n")
        if choice == "1":
            persons = csv_data.read_file()
        elif choice == "2":
            for person in persons:
                print(person)
        elif choice == "3":
            print("Enter Personal Information for a new person:")
            first_name = input("First Name: \n")
            last_name = input("Last Name: \n")
            email = input("Email (example@gmail.com): \n")
            print("A person has been added!")
            persons.append(
                {"FirstName": first_name, "LastName": last_name, "email": email})
            json_data.write_file(persons)
        elif choice == "4":
            email = input("Write the user email you want to remove: \n")
            index = 0
            for person in persons:
                if person['email'].strip() == email.strip():
                    break
                index += 1
            if index < len(persons):
                persons.pop(index)
            json_data.write_file(persons)

            print("A person has been removed!")

        elif choice == "5":
            json_data.write_file(persons)
        elif choice == "6":
            print("Program exit!\n ")
            print(60 * "-")
            quit()
            break
        else:
            print("\nSorry, but", choice,  "is not a valid choice.\n")


main()
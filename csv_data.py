
def read_file(filename="lab2-persons.csv"):
    lines = []
    try:
        with open(filename, "r", encoding="utf-8-sig") as csvfile:
            for line in csvfile:
                line = line.rstrip("\n").split(";")
                persons_dict = {
                    "FirstName": line[1],
                    "LastName": line[2],
                    "email": line[3],
                }
                lines.append(persons_dict)
            return lines
    except FileExistsError as error:
        print(error)
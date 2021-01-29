import json


def write_file(data):
    try:
        with open("save_file.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile)
    except FileNotFoundError as error:
        print(error)


def read_file(filename="save_file.json"):
    try:
        with open(filename, "r", encoding="utf-8-sig") as jsonfile:
            jsonLines = json.load(jsonfile)
            return jsonLines
    except FileExistsError as error:
        print(error)

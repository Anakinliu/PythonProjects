import json
numbers = {
    "un": 2,
    "pw": "sdadasd"
}

username = [1, 2, 3]

with open("numbers.json", "w") as file_obj:
    json.dumps(numbers, file_obj)
#
# with open("numbers.json") as file_obj:
#     res = json.load(file_obj)
#     print(res)



import json


def read_json():
    with open(file="Package/file.json", encoding="utf-8", mode="r") as file:
        info = json.load(file)
        for i in info:
            print(f'id: {i["_id"]}; name: {i["name"]} ({i["gender"]}); phone: {i["phone"]}; address: {i["address"]}')

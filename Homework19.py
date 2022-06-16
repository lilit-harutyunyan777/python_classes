import os

import json

import yaml

my_dict = {"name" : "Ann", "surname": "Smith", "Age": 40}

print(my_dict)

print(os.getcwd())

with open("my_gson.json", "w") as my_gson_file:

    json.dump(my_dict, my_gson_file)

with open("my_gson.json", "r") as my_gson_file:

    my_text = ""

    data = json.load(my_gson_file)

    print(data)

    for i in data:

        my_text += i + " " + str(data[i]) + " "

    print(my_text)

    print(type(my_text))

print(data)

with open("yml_file.yaml", "w") as yml_file:

    yaml.dump(data, yml_file, allow_unicode=True)

    print(yml_file.read())

with open("yml_file.yaml", "r") as yml_file:

    data_yaml = yaml.safe_load(yml_file)

with open("my_json_2.json", "w") as gson_2_file:

    json.dump(data_yaml,gson_2_file)

    print(gson_2_file.read())

    my_text_2 = ""

    for i in data_yaml:

        my_text_2 +=  i + " " + str(data_yaml[i]) + " "

    print(my_text_2)
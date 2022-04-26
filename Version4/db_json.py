import json


def write_values(newData):
    try:
        with open('albums_data.txt', 'r') as json_file:
            oldData = json.load(json_file)
        with open('albums_data.txt', 'w') as json_file:
            oldData.append(newData)
            jsoned_data = json.dumps(oldData, indent=True)
            json_file.write(jsoned_data)
    except:
        with open('albums_data.txt', 'w') as json_file:
            oldData = []
            oldData.append(newData)
            jsoned_data = json.dumps(oldData, indent=True)
            json_file.write(jsoned_data)


def read_values():
    try:
        with open('albums_data.txt', 'r') as objects:
            return json.load(objects)
    except:
        pass



def write_values(values):
    try:
        file = open("albums_data.txt", "a", encoding='utf-8')
        file.write(values)
        file.close()
    except:
        file = open("albums_data.txt", "w", encoding='utf-8')
        file.write(values)
        file.close()


def read_values():
    try:
        file = open("albums_data.txt", 'r', encoding='utf-8')
        objects = file.read().split('\n')
        file.close()
        return objects
    except:
        pass

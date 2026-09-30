def read_config(path):
    file = open(path)
    data = file.read()
    return data

config = read_config("settings.txt")
print(config)
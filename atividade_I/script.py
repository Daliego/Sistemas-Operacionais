import os

parent_path = os.getcwd()

directoryName = 'ricardoDirectory'

path = os.path.join(parent_path, directoryName)

text = 'Só alegria hahaha'

try:
    os.mkdir(path)
except OSError as error:
    print(error)

theTextFile = open(f'{path}\\fileText.txt', "a")
theTextFile.write(text)
theTextFile.close()

print(open(f'{path}\\fileText.txt', "r").read())


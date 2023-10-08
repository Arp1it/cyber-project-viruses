from sys import argv
import os

script = argv
name = str(script[0])
namee = name.split("/")
nameee = namee[-1]
print(nameee)
# exit()

cmd = 'start payload.txt'
os.system(cmd)
os.mkdir('clone')
os.system(r"copy payload.txt clone")
os.system(r"copy " + nameee + " clone")
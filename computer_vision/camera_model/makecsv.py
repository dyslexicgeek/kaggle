import re

classes = open("classes.csv", "w");
with open("filenames", "r") as ins:
    array = []
    for line in ins:
        line = line.replace('\n','')
        classname = (line[line.find("(")+1:line.find(")")])
        writeStr = line+","+classname
        #print(writeStr)
        classes.write(writeStr)
        classes.write('\n')


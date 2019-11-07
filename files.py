# imports
import csv

# helper functions
def getLines(fileText, arrayName):
    for line in fileText:
        tempString = ""
        for char in line:
            if (char == '\n'):
                continue
            tempString += char
        arrayName.append(tempString)
    # print(arrayName)

def isError(func, *args, **kw):
    try:
        func(*args, **kw)
        return False
    except Exception:
        return True

# open file
fileName = input("Input file name with extension: ")
# filename = "test.txt"
brainFile = open(fileName, "r")
# print (brainFile.read());
patientID = input("Patient ID: ")

lines = [] 
areas = []
names = []
getLines(brainFile, lines)
for line in lines:
    charArray = line.split(' ')
    area = 0
    name = ""
    for elem in charArray:
        # if (int(elem) <= 9 and int(elem) >= 0):
        if (isError(float, elem) == False):
            area = elem
        else:
            name += elem
    areas.append(float(area))
    names.append(name)
# print (areas)
# print (names)

def horizontal_write (file, names, areas):
    fileCSV = file + ".csv"
    with open(fileCSV, mode='w') as origin:
        result_writer = csv.writer(origin, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        result_writer.writerow((patientID, ''))
        result_writer.writerow(names)
        result_writer.writerow(areas)

horizontal_write(patientID, names, areas)

def vertical_write (file, list1):
    with open(file, mode='w') as origin:
        result_writer = csv.writer(origin, delimiter = ',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        result_writer.writerow((patientID, ''))
        for num in range(0, len(list1)):
            result_writer.writerow((list1[num],''))

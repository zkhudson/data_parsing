import re

timestamp_delete = 2
index = 0
threshold_counter = 0

with open("input001.txt") as open_file:
    data = open_file.read()

#Given an initial setup string using the format '3 1000 4' at the begining of the file:
# find the column to monitor (1st number)
# find the thresehold for the number you are monitoring (2nd number)
# find the consecutive occurences before printing the time stamp (3rd number)
setup = re.search(r'(\d{1}\b\s\b\d{2,4}\b\s\b\d{,2}\b)', data, re.X)
setup = setup.group()
column = int(setup[0])
threshold = int(setup[2:-2])
threshold_consecutive = int(setup[-1])

# find the timestamp data and remove the first two occurences
# first two occurences are not apart of the data set table
timestamp = re.findall(r'(\d\d\:\d\d\:\d\d\b)+', data, re.X)
while timestamp_delete > 0:
    timestamp.__delitem__(0)
    timestamp_delete -= 1

def data_parse(parser, index, threshold, threshold_consecutive, threshold_counter):
    for parser[index] in parser:
        if parser[index] > threshold:
            threshold_counter += 1
            if threshold_counter >= threshold_consecutive:
                print(timestamp[index])
        elif parser[index] < threshold and threshold_counter > 0:
            threshold_counter = 0
        index += 1

# Checks the column value that was desired to be acquired during setup and performs appropiate data parsing
if column == 1:
    parser = re.findall(r'(\s{2,5}\b\d{4,5}\b\s{2,5})+', data, re.X)
    parser = [int(i) for i in parser]
    data_parse(parser, index, threshold, threshold_consecutive, threshold_counter)
elif column == 2:
    print("I can't do this column yet...")
elif column == 3:
    parser = re.findall(r'(\b\d\d\.\d\d\b)+', data, re.X)
    parser = [float(i) for i in parser]
    data_parse(parser, index, threshold, threshold_consecutive, threshold_counter)
elif column == 4:
    print("I can't do this column yet...")
elif column == 5:
    print("I can't do this column yet...")
elif column == 6:
    print("I can't do this column yet...")
else:
    print("Pick a valid column in the data table!")

# Returns the original data set that was parsed and the associated timestamps
print(parser)
print(timestamp)





file = open("test.txt")

print(file.read())      # read all the contents of file
file.close()            # remember to close the file to avoid memory leaks


print("*****1*****")
file = open("test.txt")
print(file.read(7))    # read the first n byte/character of file, going to new line is one character
file.close()


print("*****2*****")
# open the file and close it automatically WHEN the code execution is completed
with open("test.txt") as file:          # default: read mode
    # read one single line at a time
    print(file.readline())
    print(file.readline())


print("*****3*****")
with open("test.txt") as file:

    line = file.readline()      # store the 1st line into variable "line"

    while line != '':
        print(line)
        line = file.readline()


print("*****4*****")
with open("test.txt") as file:

    # readlines() --> ≈ read(); read entire file & each line will get stored in a list
    # file.readlines() = ["abc", "bcd", "cde"]
    for eachLine in file.readlines():
        print(eachLine)

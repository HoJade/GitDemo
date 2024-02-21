file = open("test.txt")
file.close()


# read the file and store all the lines into a list
# reverse the list
# write the reversed list back to the file
with open("test.txt", "r") as reader:           # "r" = read; "w" = write
    content = reader.readlines()                # get all content into a list
    print(content)
    reversed(content)                           # reverse the list

    with open("test.txt", "w") as writer:       # "w" mode would replace the current content and save with new content
        for line in reversed(content):
            writer.write(line)                  # order of the lines of the "test.txt" file will get reversed

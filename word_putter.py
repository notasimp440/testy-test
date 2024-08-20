file = open('words.txt')
wd = input("write a word: ")
for line in file:
    if line == "":
        file.write(wd)
    else:
        file.write("\n" + wd)
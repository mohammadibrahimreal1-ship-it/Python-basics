try:
    file = open("Me.txt", "r")
    for line in file:
        print(line)
    file.close()

except FileNotFoundError:
    print("File not found.")
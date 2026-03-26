# read from source file
f1 = open("input.txt", "r")
data = f1.read()
f1.close()

# convert to uppercase
data = data.upper()

# write to new file
f2 = open("output.txt", "w")
f2.write(data)
f2.close()

print("File copied in uppercase.")
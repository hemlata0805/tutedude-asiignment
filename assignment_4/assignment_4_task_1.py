try:
    file1 = open('sample.txt', 'r')
    # statements
    reading_file = file1.readlines()
    print("Reading file content:")
    count = 1
    for i in reading_file:
        print("Line",count,":", i.strip())
        count += 1
    file1.close()
except FileNotFoundError:
    print("Error: the file sample.txt was not found.")

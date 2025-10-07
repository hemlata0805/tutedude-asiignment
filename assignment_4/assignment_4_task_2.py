file1=open('output.txt','w')
text=input("enter text to add to the file: ")
writing_file=file1.write(text)       #it will return characters and all the content in the file will be removed and only hello will be there
print("Data successfully written to output.txt")      # Output:6


file1=open('output.txt','a')
append_text = input("Enter additional text to append: ")
appending_file=file1.write("\n"+append_text)       #it will return characters
print("Data successfully appended.")      # Output:24
file1.close()

file1=open('output.txt','r')
reading_file=file1.read()
print("Final content of output.txt")
print(reading_file)
file1.close()
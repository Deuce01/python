#Give the string as static input and store it in a variable.
givenstring=input('Enter some random string = ')
#Enter the file name of the  file using the input() function and store it in a variable.
filename = input("Enter the first file name = ")
#In append mode, open the first file with the entered file name.
givenfile=open(filename,"a")
#Write a new line character to the given file using the write() function and '\n'.
givenfile.write("\n")
#Append the given string to the given file using the write() function.
givenfile.write(givenstring)
#Close the given file using close() function.
givenfile.close()
print('Printing the contents of the given file :')
with open(filename, 'r') as givenfile:
  #Using for loop, go over the lines in the first file.
    for fileline in givenfile:
      #print the lines
        print(fileline)

# Give the number as user input using the int(input()) function and
# store it in a variable.
gvn_numb = int(input("Enter some random Number = "))
# Convert the given number to a string using the str() function and
# store it in another variable.
str_numb = str(gvn_numb)
# Apply the lstrip() method with the argument passed as 0 on the above string number
# and store it in another variable.
lstrip_num = str_numb.lstrip("0")
# Check if 0 is present in the above lstrip number using the if conditional statement.
if("0" in lstrip_num):
  # If the statement is true, then print "The given number is a Duck Number".
    print("The above given number {", gvn_numb, "} is a Duck number")
else:
  # If the statement is false, print "The given number is Not a Duck Number".
    print("The above given number {", gvn_numb, "} is Not a Duck number")

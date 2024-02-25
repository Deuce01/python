# In read mode, open the first file say  samplefile1.txt.
with open("samplefile1.txt") as file1:
  # In write mode, open the second file say  samplefile2.txt.
    with open("samplefile2.txt", "w") as file2:
      # Using for loop, go over the lines in the first file.
        for iline in file1:
          # Copy the ith line of the first file to the second file using the write function.
            file2.write(iline)

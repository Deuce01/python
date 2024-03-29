# Import fitz module using the import keyword
import fitz
# Import io(input-output) module using the import keyword
import io
# Import Image from PIL module using the import keyword
from PIL import Image

# Open some random PDF file using the open() function of the fitz module 
# by passing the filename/path as an argument to it.
gvn_pdf= fitz.open("samplepdf_file.pdf")
# Calculate the number of pages in a given PDF file using the len() function
# by passing the given pdf file as an argument to it.
no_of_pages = len(gvn_pdf)

# Loop in each page of the pdf till the number of pages using the for loop
for k in range(no_of_pages):
    # Get the page at iterator index
    page = gvn_pdf[k]
    # Get all image objects present in this page using the getImageList() function
    # and store it in a variable
    img_lst = page.getImageList()
    # Loop in these image objects using the for loop and enumerate() function
    for imgcount, image in enumerate(img_lst, start=1):
        # Get the XREF of the image information.
        img_xref = image[0]
        # Extract image information by passing the above image xref to the extractImage() function
        imageinformation = gvn_pdf.extractImage(img_xref)
        # Extract image bytes by passing "image" to the above imageinformation
        img_bytes = imageinformation["image"]
        # Access the image extension by passing "ext" to the above imageinformation
        img_extension = imageinformation["ext"]
        # Load this image to PIL using the BytesIO() function by passing the above 
        # image bytes as argument to it.
        rslt_img= Image.open(io.BytesIO(img_bytes))
        # Save this above result image using the save() function with the given image count and extension
        rslt_img.save(open(f"page{k+1}_img{imgcount}.{img_extension}", "wb"))

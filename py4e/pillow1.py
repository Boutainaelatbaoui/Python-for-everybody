# -------------------------------------------------
# -- Practical => Image Manipulation With Pillow --
# -------------------------------------------------

from PIL import Image

# open the image
myImage = Image.open(r"C:\Users\PC\Desktop\kirmizi2.PNG")

# Show The Image
myImage.show()

# My Cropped Image
myBox = (0, 0, 300, 300)
myNewImage = myImage.crop(myBox)

# Show The New Image
myNewImage.show()

# My Converted Mod Image
myConverted = myImage.convert("L")
myConverted.show()

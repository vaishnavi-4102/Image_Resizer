# Installing pillow module

from PIL import Image

def resize(image,new_width):
    width,height = image.size
    ratio = height/width
    new_height = (int)(ratio*new_width)
    resized_img = image.resize((new_width,new_height))
    return resized_img

    

image = Image.open("marvel.jpg")

# image.show() --> To show the image
print("Size of the image is:")
print(image.size) 

width = int(input("Enter the width of the image:"))

print("Resizing the image....")
print("Pls wait....")
image = resize(image,width)
print("Resized image will now be shown....")
image.show()


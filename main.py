import glob
import imagehash
from PIL import Image 

my_image_url = "mypic.jpg"  # getting my image

my_hash = imagehash.average_hash(Image.open(my_image_url)) # converting image into hash code

girls = glob.glob('./girls/*.jpg') # getting girls pic from file
selected = girls[0]
accepted_diff = 1000    
for girl in girls:
    girl_hash = imagehash.average_hash(Image.open(girl))  # converting girls pic to hashcodes
    dif = girl_hash- my_hash    # Diference of my hash code and girls hash code
    if dif < accepted_diff:     # If  difference is lesser than 1000, she will be my gf
        selected = girl
        accepted_diff = dif

bf_img = Image.open(my_image_url)
gf_img = Image.open(selected) 
couple_img = Image.new('RGB',(bf_img.width + gf_img.width, bf_img.height))  # To show  my image and gf image in a single pic 
couple_img.paste(bf_img,(0,0))
couple_img.paste(gf_img,(bf_img.width,0))
couple_img.save("my_valentine_pic.jpg")
couple_img.show()
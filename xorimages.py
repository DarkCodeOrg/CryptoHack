from PIL import Image, ImageChops

im1 = Image.open("lemur.png")
im2 = Image.open("flag.png")

im3 = ImageChops.difference(im1,im2)


im3.show()
im3.save("final.png")



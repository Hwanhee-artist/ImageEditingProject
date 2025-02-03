import os, sys
from PIL import Image
#im = Image.open("mj.jpg")
#print(im.format, im.size, im.mode)

while True:
    print(" ")
    image_name = input("Type the name of your image: ")

    crop = input("Type the size of pixels you want to crop the image: ")
    crop = int(crop)

    infile = image_name
    im = Image.open(infile)

    if im.format != "JPEG":
        for infile in sys.argv[1:]:
          f, e = os.path.splitext(infile)
          outfile = f + ".jpg"
          if infile != outfile:
             try:
                with Image.open(infile) as im:
                    im.save(outfile)
             except OSError:
                print("cannot convert", infile)

    box = (0,0,crop,crop)
    region = im.crop(box)
    region = region.transpose(Image.Transpose.ROTATE_180)
    im.paste(region, box)
    print(infile, im.format, f"{im.size}x{im.mode}")

    im.show()
    print("")
    print("Do you want to edit more? y/n")
    if input() == "y": continue
    if input() == "n": break



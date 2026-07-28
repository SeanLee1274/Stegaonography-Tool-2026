#detect.py
import os
from PIL import Image

def CompareImages (image_1, image_2):
    x = 0
    y = 0

    image1 = Image.open(image_1)
    pixles1 = image1.load()
    width1, height1 = image1.size

    image2 = Image.open(image_2)
    pixles2 = image2.load()
    width2, height2 = image2.size
    flag = True
    for y in range(height1):
        for x in range(width1):
            R1_value, G1_value, B1_value = pixles1[x, y]
            R2_value, G2_value, B2_value = pixles2[x, y]

            if R1_value != R2_value:
                flag = False
                break

            if G2_value != G2_value:
                flag = False
                break

            if B1_value != B2_value:
                flag = False
                break
        if flag == False:
            break

    return flag

def main():
    print("This assumes that you have the original file.")
    inputName1 = "dog1.png"
    inputName2 = "dog1_copy.png"

    inputImagePath1 = os.path.join("images", inputName1)
    inputImagePath2 = os.path.join("images", inputName2)

    if CompareImages(inputImagePath1, inputImagePath2):
        print("There is NO sign of steganography in this image")
    else: 
        print("There is signs of steganography in this image")


if __name__ == "__main__":
    main()
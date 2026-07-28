#Embed.py
import os
from PIL import Image

def TextToBinary(message):
    binaryString = ""
    for letter in range(len(message)): 
        binary = format(ord(message[letter:letter+1]),'08b')
        binaryString += binary + ' '
    return binaryString

def JPG_To_PNG(JPG_Image_Path, fileName):
    PNG_path = JPG_Image_Path[:-3] + "png"
    PNG_Image =  Image.open(JPG_Image_Path)
    PNG_Image.save(PNG_path)
    return

def main():
    #message = input("Input your message : ")
    #binary = TextToBinary(message)
    inputName = input("Name of image : ")
    inputImagePath = os.path.join("images", inputName)
    if inputName[-3:] == "jpg":
        print ("Image is file type : '.jgp'. Changing to type '.png'")
        JPG_To_PNG(inputImagePath, inputName)
    #print(binary)

if __name__ == "__main__":
    main()
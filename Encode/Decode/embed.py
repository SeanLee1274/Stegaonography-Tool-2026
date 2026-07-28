#Embed.py
import os
from PIL import Image

def TextToBinary(message):
    binaryString = ""
    for letter in range(len(message)): 
        binary = format(ord(message[letter:letter+1]),'08b')
        binaryString += binary + ' '
    return binaryString

#def JpgToPng(image)
    

def main():
    #message = input("Input your message : ")
    #binary = TextToBinary(message)
    inputImageName = input("Name of image : ")
    inputImage = os.path.join("images", inputImageName)
    #print(os.getcwd())
    #print(inputImage)
    inputImage = Image.open(inputImage)
    inputImage.show()
    #print(binary)

if __name__ == "__main__":
    main()
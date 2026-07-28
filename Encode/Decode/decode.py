#encode.py
import os
from PIL import Image

def BinaryToText(binaryString):
    string = ""
    for i in range(0,len(binaryString),8):
        chunk = binaryString[i:i+8]
        string += chr(int(chunk,2))
    return(string)

def decodePNG(PNG_path):
    x = 0
    y = 0

    image = Image.open(PNG_path)
    pixles = image.load()
    width, height = image.size

    header_Length = 16
    header_Binary_String = ""
    for x in range(0, 16):
        R_value, G_value, B_value = pixles[x,0]
        if (header_Length <= 0):
            break
        header_Length -= 1
        header_Binary_String += str(R_value & 1)
        if (header_Length <= 0):
                break
        header_Length -= 1
        header_Binary_String += str(G_value & 1)
        if (header_Length <= 0):
                break
        header_Length -= 1
        header_Binary_String += str(B_value & 1)
    message_length = int(header_Binary_String, 2)

    combined_Length = 16 + message_length
    message = ""
    for y in range(height):
        for x in range(width):
            R_value , G_value, B_value = pixles[x, y]
            if (combined_Length <= 0):
                break
            combined_Length -= 1
            message += str(R_value & 1)
            if (combined_Length <= 0):
                break
            combined_Length -= 1
            message += str(G_value & 1)
            if (combined_Length <= 0):
                break
            combined_Length -= 1
            message += str(B_value & 1)
        if (combined_Length <= 0):
            break
    print(BinaryToText(message[16:]))
    return

def main():
    inputName = input("Name of image : ")
    #inputName = "dog1_stego.png"
    inputImagePath = os.path.join("images", inputName)
    decodePNG(inputImagePath)

if __name__ == "__main__":
    main()
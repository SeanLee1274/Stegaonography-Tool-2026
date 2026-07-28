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
    return PNG_path

def PNG_ImageEmbedding(PNG_path, binaryMessage):
    binaryMessage = binaryMessage.replace(" ", "")

    x = 0
    y = 0

    image = Image.open(PNG_path)
    pixles = image.load()
    width, height = image.size

    counter = 0
    #print(len(binaryMessage))
    for y in range(height):
        #print(counter)
        for x in range(width):
            R_value, G_value, B_value = pixles[x, y]
            if (counter >= len(binaryMessage)):
                break
            R_value = R_value & ~1 | int(binaryMessage[counter])
            counter += 1
            #print(counter)

            if (counter >= len(binaryMessage)):
                break
            G_value = G_value & ~1 | int(binaryMessage[counter])
            counter += 1
            #print(counter)

            if (counter >= len(binaryMessage)):
                break
            B_value = B_value & ~1 | int(binaryMessage[counter])
            counter += 1
            #print(counter)

            pixles[x, y] = (R_value, G_value, B_value)
        if (counter >= len(binaryMessage)):
            break
    outputImage = PNG_path[:-4] + "_stego.png"
    image.save(outputImage)
    return outputImage

def main():
    message = input("Input your message : ")
    #message = "Hello World!"
    binary = TextToBinary(message)
    inputName = input("Name of image : ")
    #inputName = "dog1.jpg"
    inputImagePath = os.path.join("images", inputName)
    if inputName[-3:] == "jpg":
        print ("Image is file type : '.jgp'; Changing to type '.png'")
        inputImagePath = JPG_To_PNG(inputImagePath, inputName)
    outputImage = PNG_ImageEmbedding(inputImagePath, binary)

if __name__ == "__main__":
    main()
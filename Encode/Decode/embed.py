#Embed.py

def TextToBinary(message):
    binaryString = ""
    for letter in range(len(message)): 
        binary = format(ord(message[letter:letter+1]),'08b')
        binaryString += binary + ' '
    return binaryString

def main():
    message = input("Input your message : ")
    binary = TextToBinary(message)
    print(binary)

if __name__ == "__main__":
    main()
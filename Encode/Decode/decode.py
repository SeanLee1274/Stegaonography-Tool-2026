#encode.py

def BinaryToText(binaryString):
    string = ""
    for chunk in binaryString.split():
        string += chr(int(chunk, 2))
    return(string)

def main():
    binaryString = input("Input your binary (With spaces every 8 bits) : ")
    message = BinaryToText(binaryString)
    print(message)

if __name__ == "__main__":
    main()
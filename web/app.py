import streamlit as st
from PIL import Image
from  

st.title("Steganography Toolkit")

# Option: embed or decode
mode = st.radio("Choose an action", ["Embed", "Decode"])

# Drag box for the file
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

# Only show a message box if we're embedding — decoding doesn't need one
if mode == "Embed":
    message = st.text_input("Message to hide")

# Confirm button
if st.button("Confirm"):
    if uploaded_file is None:
        st.write("Please upload an image first.")
    else:
        image = Image.open(uploaded_file)

        if mode == "Embed":
            # TODO: call your embed logic here, e.g.:
            binary = TextToBinary(message)
            result_image = PNG_ImageEmbedding(image, binary)
            #st.write("Embed mode — plug in your embed function here")

        elif mode == "Decode":
            # TODO: call your decode logic here, e.g.:
            # result_text = decodePNG(image)
            st.write("Decode mode — plug in your decode function here")
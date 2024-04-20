import streamlit as st
from dotenv import load_dotenv
import os
from PIL import Image
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input,image,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input,image[0],prompt])
    # print(image[0]) 
    return response.text

def input_image_upload(uploaded_file):
    if uploaded_file is not None:
        # print(uploaded_file)
        bytes_data=uploaded_file.getvalue()

        image_part=[{
            "mime_type":uploaded_file.type,
            "data":bytes_data
        }]
        # print(bytes_data)
        # print(image_part)


        return image_part
    else:
        raise FileNotFoundError("No file uploaded.")
    

st.set_page_config(page_title="Image Checker")
st.header("Gemini Application")

input=st.text_input("Input Prompt: " ,key="input" )
uploaded_file=st.file_uploader("Upload a file: ",type=["png","jpg","jpeg"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_column_width=True)

submit=st.button("Give me the Details..")

input_prompt="""
You are an expert in understanding Images. You will receive
input images and you will have to give detail about the input image.

"""

if submit:
    image_data=input_image_upload(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)

    st.subheader("The Response is")
    st.write(response)
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai
from PIL import Image



st.set_page_config('DEFECT AI',page_icon='⚡︎ ⋆.˚ 🤖ིྀ˚.⋆ ⚡︎',layout='wide')

st.title('AI POWERED DEFECT ANALYZER🤖👾')
st.header(':blue[Prototype of autamated structural defect analyzer using AI]💡🦾')
st.subheader(f" :red[AI Powered structural defect analysis using Streamlit that allows users to upload the image of any structural defects and to get suggestions and recomendations for repair and rebuilt]📍")

with st.expander('About the app:'):
    st.markdown(f'''This app help to detect the defects like cracks,misalligments etc and provide
                - **Defect Detection**
                - **Recommendation**
                - **Suggestions for improvements''')
    
import os

key=os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=key)

input_image=st.file_uploader('Upload your file here🛍️',type=['png','jpeg','jpg'])
img=''
if input_image:
    img=Image.open(input_image).convert('RGB')
    st.image(img,caption='Uploaded Successfully')

prompt = f'''You are an quality engine
er and civil engineer. You need to Analyze the input 
image and provide necessary details for the below given questions 
in bullet points (max 3 points for each questions)

1.Identify the type of structural defect in the given image like cracks,bends,misalligements etc
2.Identify the color of the defect in the given image
3.Provide suggestions for repairing the defect in the given image
4.Indentify the possible causes of the defect in the given image
5.Provide recommendations for preventing such defects in the future
6.Provide a severity level for the defect in the given image (low, medium, high)
7.Provide a confidence score for the analysis (0-100%)
8.Provide any additional observations or insights about the defect in the given image
9.Provide a summary of the analysis in one or two sentences
10.Provide a list of similar defects that have been observed in the past and their outcomes'''

model=genai.GenerativeModel('gemini-2.5-flash-lite')

def generate_result(prompt,img):
    result =model.generate_content(f'''Using the given {prompt}
                                   and given image {img}
                                   analyze the image and give the 
                                   results as per the given prompt''')
    
    
    return result.text

submit=st.button('Analyze the image')

if submit:
    with st.spinner('Results Loading...'):
        response= generate_result(prompt,img)
        
        st.markdown('## :green[Results]')
        st.write(response)
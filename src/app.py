import streamlit as st
from PIL import Image
import pytesseract
from googletrans import Translator
import pyperclip
from functions import get_img_resize,get_key_from_value
from configurations import *
from streamlit_js_eval import streamlit_js_eval
from streamlit_cropper import st_cropper
import pandas as pd


translator = Translator()
# Activate wide mode
st.set_page_config(layout='wide')


if 'detected_text' not in st.session_state:
    st.session_state.detected_text = ""
if 'translated_text' not in st.session_state:
    st.session_state.translated_text = ""
if 'img_text' not in st.session_state:
    st.session_state.img_text = ""
if 'init_destination' not in st.session_state:
    st.session_state.init_destination = None
if 'image_file' not in st.session_state:
    st.session_state.image_file = None   
if 'screen_width' not in st.session_state:
    st.session_state.screen_width = None

st.title('Optical Character Recognition (OCR) & Translator')
st.subheader('Please Upload an Image to Begin.')

# First row for language selection
col1, col2 = st.columns(2)

# Left column for source language selection
with col1:
    src = st.selectbox("From (Auto Detect Enabled)",['English', 'Chinese-Simplified', 'Malay', 'Filipino', 'Vietnamese', 'Tamil','Thai'], key='source_lang')
    source = translate_lang[src]
    st.write("")

# Right column for destination language selection
with col2:
    destination = st.selectbox("To",['English', 'Chinese-Simplified', 'Malay', 'Filipino', 'Vietnamese', 'Tamil','Thai'], key='destination_lang')
    dst = translate_lang[destination]
    st.write("")

# Left column for OCR and image upload
with col1:
    image_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg', 'JPG'])
    if image_file is not None: 
        img = Image.open(image_file)
        st.subheader('Image you Uploaded...')
        # Resize the image to fit the column width in the streamlit page
        screen_width = streamlit_js_eval(js_expressions='screen.width', key = 'SCR')
        st.session_state.screen_width = screen_width
        if st.session_state.screen_width is not None:
            resized_img= get_img_resize(img,st.session_state.screen_width)
            cropped_img = st_cropper(img_file=resized_img,realtime_update=True)
            st.session_state.image_file = cropped_img if cropped_img else image_file

    if st.button("Convert Text"):
        st.session_state.img_text = pytesseract.image_to_string(st.session_state.image_file, config=custom_config)
        st.session_state.detected_text = ' '.join(st.session_state.img_text.split())
        st.write('')

    if st.session_state.detected_text:         
        detected_lang=translator.detect(st.session_state.detected_text).lang
        if detected_lang is None:
            st.write(f"### Please upload a clear image")
        else:
            print_lang = f"Detected Language is {get_key_from_value(detected_lang)}"
            st.write(f"### {print_lang}")
            st.text_area('Extracted Text',st.session_state.img_text,height=200)

with col2:
    # Display the text area with the translated text inside the container
    if st.session_state.detected_text: 
        try:
            with st.spinner('Translating Text...'):
                sour = translator.detect(st.session_state.detected_text).lang
                result = translator.translate(st.session_state.img_text, src=f'{sour}', dest=f'{dst}').text
            st.text_area('Translated Text',result,height=200) 
            st.session_state.translated_text = result
            st.write('')
        except Exception as e:
            st.error("Translation Error: {}".format(str(e)))

# Create a button to copy the text to clipboard
with col1:
    if st.button('Copy Extracted Text'):
        pyperclip.copy(st.session_state.detected_text)
        st.write('Extracted Text copied to clipboard!')
    
    download_format_extracted = st.selectbox("Select Ectracted File Format", ["CSV", "TXT"])

    if download_format_extracted == "CSV":
        extracted_text_df = pd.DataFrame({'Extracted Text': [st.session_state.detected_text]})
        extracted_text_filename = 'extracted_text.csv'
        st.download_button(label="Download Extracted Text", data=extracted_text_df.to_csv(), file_name=extracted_text_filename, mime='text/csv')
    elif download_format_extracted == "TXT":
        extracted_text_filename = 'extracted_text.txt'
        st.download_button(label="Download Extracted Text", data=st.session_state.detected_text, file_name=extracted_text_filename, mime='text/plain')
        
with col2:
    if st.button('Copy Translated Text'):
        pyperclip.copy(result)
        st.write('Transalted Text copied to clipboard!')
   
    download_format_translated = st.selectbox("Select Translated File Format", ["CSV", "TXT"])
    
    if download_format_translated == "CSV":
        translated_text_df = pd.DataFrame({'Extracted Text': [st.session_state.translated_text]})
        translated_text_filename = 'translated_text.csv'
        st.download_button(label="Download Translated Text", data=translated_text_df.to_csv(), file_name=translated_text_filename, mime='text/csv')
    elif download_format_translated == "TXT":
        translated_text_filename = 'translated_text.txt'
        st.download_button(label="Download Translated Text", data=st.session_state.translated_text, file_name=translated_text_filename, mime='text/plain')
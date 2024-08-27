import streamlit as st
from googletrans import Translator
from configurations import *

def get_img_resize(img,screen_width):
    aspect_ratio = img.width / img.height
    new_width = int(screen_width/ 3)
    new_height = int(new_width / aspect_ratio)
    resized_img = img.resize((new_width, new_height))
    return resized_img

def get_key_from_value(value):
    for key, val in translate_lang.items():
        if val == value:
            return key
    return None 
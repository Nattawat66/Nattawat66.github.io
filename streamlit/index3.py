import torch
import streamlit as st
from PIL import Image
from diffusers import DiffusionPipeline as DP
print(st.__version__)
st.header('GEN IMAGE')
st.button('หน้าแรก')

st.title('OOP in ML')
mainpic = st.image('https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExemV2ZG94dG40M2ZsMGkwOWlieXJzZmp5Nno1OWN1ZHhyN2txc3hmeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/F6ZC06fX688qk/giphy.gif')
text = st.text_input("Your Text Gen Image: ")

if text:
    print("Work")
    dp = DP.from_pretrained("runwayml/stable-diffusion-v1-5")
    image_data = dp(text).images[0]
    image = Image.fromarray(image_data)
    image.show()
    st.write(f'กำลังสร้างภาพ {text} ')
import streamlit as st
print(st.__version__)
st.sidebar.header('Sidebar')
st.sidebar.button('หน้าแรก')
st.sidebar.button('ผลงาน')
st.sidebar.button('ติดต่อ')


st.title('OOP in ML')
mainpic = st.image('https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExemV2ZG94dG40M2ZsMGkwOWlieXJzZmp5Nno1OWN1ZHhyN2txc3hmeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/F6ZC06fX688qk/giphy.gif')
text = st.text_input("Your Text: ")

if text:
    st.write(f'กำลังสร้างภาพ {text} ')
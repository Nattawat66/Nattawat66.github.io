import streamlit as st

st.sidebar.header('Sidebar')
st.sidebar.button('หน้าแรก')
st.sidebar.button('ผลงาน')
st.sidebar.button('ติดต่อ')

st.title('OOP in ML')

text = st.text_input("Your Text:")

white = 'https://i.pinimg.com/originals/84/2a/d6/842ad68b315b0f586c30b465221da609.jpg'
blue = 'https://www.solidbackgrounds.com/images/1920x1080/1920x1080-true-blue-solid-color-background.jpg'
red = 'https://cdn.cbeditz.com/cbeditz/large/11624180233y7cbwwoh8nwlxa1yo6fl8zbjpitosz4vsvfsw9kllah1ckrqm9gvt96btnqmw0hz7vltthklbipp63bx0eyhqqrym92bfnkwqdn4.png'

color = white

if not text:
    color = white
elif text == 'blue':
    color = blue
    st.write(f'กำลังสร้างภาพสีน้ำเงิน')
elif text == 'red':
    color = red
    st.write(f'กำลังสร้างภาพสีแดง')
else:
    st.write(f'ไม่มีสีที่ตรงกับข้อความ: {text}')

mainpic = st.image(color)

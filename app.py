import streamlit as st
import requests
from PIL import Image


custom_style = """
<style>
    .stApp {
        background-color: #e6e8eb;
    }
</style>
"""


st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")
st.markdown(custom_style, unsafe_allow_html=True)




img_contact_form = Image.open("C:\\Users\\Administrator\\Desktop\\website\\image\\python.png")

img_contact_form = img_contact_form.resize((450,280))

img_lottie_animation = Image.open("C:\\Users\\Administrator\\Desktop\\website\\image\\vba.png")
img_lottie_animation = img_lottie_animation.resize((450,280))


# header
with st.container():
    st.subheader("Welcome to my website")
    st.title("JACK")

with st.container():
    st.write("----")
    left_column, right_column = st.columns((2,1))
    with left_column:
        st.header("Who is Jack?")
        st.write("##")
        st.write("Hello there! My name is Jack, and I'm delighted to welcome you to my personal corner of the web. I'm a 24-year-old with a passion for a diverse range of skills and experiences."
                 "Professionally, I've delved into the world of data and technology. I consider myself a wizard when it comes to Excel, SQL, and I even speak the language of VBA and Python. With two years of experience leading tours for Western tourists, I've honed my communication skills and gained a deep appreciation for different cultures."
                 "My journey also took me to the vibrant realm of sales. I spent a year at a dynamic company specializing in home appliances and electronics, where I connected with customers and helped them find the perfect solutions for their needs."
                 "Currently, I'm contributing my expertise as a Quality Assurance (QA) professional at Foxconn, a company known for its cutting-edge technology and innovation. This role allows me to ensure the highest quality of products and services while constantly learning and growing in the tech industry."
                 "This website serves as a platform to share my journey, experiences, and insights with you. Whether you're interested in tech, travel, or just want to know more about me, I'm excited to connect with you here. Feel free to explore and get in touch")


        st.markdown("[See more](https://www.bing.com/search?q=Bing+AI&showconv=0&FORM=hpcodx)")

    with right_column:
        st_lottie(lottie_coding, height=300, width=500, key="coding")

#--------PROJECT-----
with st.container():
    st.write("----")
    st.header("All Project")
    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(img_lottie_animation)

    with text_column:
        st.header("My VBA project")
        st.write("By a passion for technology, from being a tour guide with zero coding background"
                "I put in the effort and created useful products to support my work")
        st.markdown("[Check All My Project](https://pypi.org/project/streamlit-lottie/)")

#---------------------------
with st.container():
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.header("My Python project")
        st.write("I'm relatively new to this programming language, "
                 "but I've already created many automations for my tasks and developed some basic applications with sufficient functionality for my company.")
        st.markdown("[My Python Project](https://chat.openai.com/c/cdb6613b-03a4-462a-90f6-b02b95b6b9b3)")


# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")


    contact_form = """
    <form action="https://formsubmit.co/tranmanhquyenqn@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="text" name="email" placeholder="Your message" required>
        <button type="submit">Send</button>
    </form>
    """
    left_column,right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()










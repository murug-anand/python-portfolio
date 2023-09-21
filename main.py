import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="About Me!",page_icon=":tada:",layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_coding = "https://lottie.host/375fc509-8e0e-43ad-bfec-cfce5fb63488/FjJcdFkFmb.json"

with st.container():
    st.title("Hello There:wave: I am MURUGANAND")
    st.write("I am Solution-oriented and highly resourceful Python Developer seeking to leverage robust programming and front-end development skills to solve complex problems. Adept at creating reliable, optimised, and innovative solutions to improve website functionality and user experience. Committed to continuous learning and adding value to a dynamic, forward-thinking company.")
    st.write("[Linken In ](https://www.linkedin.com/in/muruganand-s/)")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("My Skills")
        st.write("##")
        st.write("I possess a diverse skill set that encompasses Python, HTML, CSS, JavaScript, and SQL, making me well-equipped to develop dynamic and interactive web applications. With proficiency in Python, I can create robust back-end solutions, while my expertise in HTML and CSS allows me to craft elegant and responsive user interfaces. JavaScript empowers me to add interactivity and user-friendly features to websites, and my SQL knowledge enables efficient database management and data retrieval.My portfolio showcases how I seamlessly integrate these skills to deliver engaging web experiences that combine functionality and aesthetics")
    with right_column:
        st_lottie(lottie_coding, height=350, key="coding")
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    st.subheader("Web Portfolio")
    st.caption("Not this one! This one which you are currently watching is made of Only Python and little bit of CSS")
    st.write("Developed a personal [web portfolio](https://murug-anand.github.io/cv/) using HTML, CSS, and JavaScript to showcase my skills, projects, and achievements. The portfolio features a responsive design and a clean, modern layout to provide an engaging user experience.")
    st.subheader("Home Automation")
    st.write("I have designed and implemented a system that allows users to remotely control their home appliances using Blynk app on their smartphones .Programmed the NodeMCU to connect to the home Wi-Fi network ,control relay module and receive commands from blynk app through the IFTTT platform.")
    st.subheader("Vehicle Speed detector")
    st.write("I have developed a vehicle speed detector using Arduino and IR sensors as part of a mini project . Achieved accuracy of 95 percent in detecting vehicle speed and implementing a userfriendly interface using a LCD display")
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")
    contact_form = """
    <form action="https://formsubmit.co/muruganandofficial@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

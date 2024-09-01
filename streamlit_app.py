import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(layout= "wide")

def loadlottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coder = "https://lottie.host/03fad3a1-1e17-4056-aff8-4e23e6129430/gw5wdDcYdD.json"
image = Image.open("/Users/rebad/OneDrive/Documents/AAA Github/basic-steamlit-app/image/edusculp.png")
image1 = Image.open("/Users/rebad/OneDrive/Documents/AAA Github/basic-steamlit-app/image/campuseats.png")


with st.container():
    
        st.title("Joshua Robert Rebadomia")
        st.markdown(
            """
            <style>
            .animated-text {
                font-size: 24px;
                font-weight: bold;
                background: linear-gradient(270deg, #ff6ec4, #7873f5);
                background-size: 400% 400%;
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                animation: GradientAnimation 8s ease infinite;
            }

            @keyframes GradientAnimation {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
            </style>
            <p class="animated-text">Developer</p>
            """, 
            unsafe_allow_html=True
        )
        st.write("""
        Building Tomorrow's Solutions, One Line of Code at a Time.
        """)



st.write('---')

with st.container():
    selected = option_menu(
    menu_title = None,
    options = ['About', 'Projects', 'Contact'],
    icons = ['person', 'briefcase', 'envelope'],
    orientation = 'horizontal'
    )

if selected == 'About':

    with st.container():
        col3,col4 = st.columns(2)
        with col3:
            st.write("##")
            st.header("Hi! I'm Joshua Robert Rebadomia,")
            st.write("A 22-year-old Developer based in Pakigne Velpal 1, Minglanilla, Cebu. My passion lies in coding and creating innovative solutions that make a difference. With a focus on continuous learning and growth, I am dedicated to exploring new technologies and pushing the boundaries of what’s possible in the tech world. My journey is one of curiosity and commitment to mastering the art of development.")
        with col4:
            st_lottie(loadlottieurl(lottie_coder), height=500, width=500)
    st.write("---")
    with st.container():
        col5,col6 = st.columns(2)
        with col5:
            st.subheader("""
            Education
            - 2015-2019
                - Holy Rosary School of Pardo J. Tabura Street, Pardo
                - Cebu City, Philippines 6000
            - 2019-2021
                - Cebu Institute of Technology University
                - Natalio B. Bacalso Ave, Cebu City, 6000
            - 2021-2024
                - Cebu Insitute of Technology University
                - Natalio B. Bacalso Ave, Cebu City, 6000
            """)
        with col6:
            st.subheader("""
            Skills
            - **Programming Languages:** Python, JavaScript, HTML, CSS
            - **Frameworks:** React, Streamlit
            - **Databases:** MySQL, MongoDB
            """)

if selected == 'Projects':
    with st.container():
        st.header("My projects")
        st.write("##")

        col7,col8 = st.columns(2)

        with col7:
            st.image(image)
            st.subheader("Edusculp")
            st.write("""
            - **Project Description:** This is a project that I made using React and MySQL.
            """)
            st.markdown("[Visit Github Repository](https://github.com/Dumosse/edusculp)") 

        with col8:
            st.image(image1)
            st.subheader("Campuseats")
            st.write("""
            - **Project Description:** This is a project that I made using React, MongoDB, Java.
            """)
            st.markdown("[Visit Github Repository](https://github.com/shannandrei/campus_eats)") 

            
if selected == 'Contact':
    with st.container():
        st.write("## Contact Me")
        st.write("Feel free to reach out through any of the following channels:")

        col9,col10 = st.columns(2)

        with col9:
            st.write("**Email:** [rebadomiarobert@gmail.com](mailto:rebadomiarobert@gmail.com)")
            st.write("**Phone:** +639694228183")
            st.write("**GitHub:** [https://github.com/SHUUAA](https://github.com/SHUUAA)")

        with col10:
            st.write("### Or send me a message:")
            st.markdown(
                """
                <style>
                .contact-form input, .contact-form textarea, .contact-form button {
                    width: 100%;
                    margin-bottom: 10px;
                    border-radius: 10px;
                    padding: 10px;
                }
                .contact-form textarea {
                    height: 150px;
                    resize: vertical;
                }
                .contact-form button {
                    background-color: #2a9d8f;
                }

                </style>
                <form class="contact-form" action="https://formsubmit.co/rebadomiarobert@gmail.com" method="POST">
                    <input type="email" name="email" placeholder="Your Email" required>
                    <textarea name="message" placeholder="Your Message" required></textarea>
                    <button type="submit">Send</button>
                </form>
                """, 
                unsafe_allow_html=True
            )
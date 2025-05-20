import streamlit as st
import qrcode
from io import BytesIO
import time

st.set_page_config("QR Generator", page_icon="📄", layout="centered", initial_sidebar_state="collapsed")

with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown("""<h2 class="floating-text"><span style="color: white;
             text-decoration: none;">QR Code Generator</span></h2>""", unsafe_allow_html=True)       # top 65 --> Paragraph
                                                                                                     # top 45 --> Heading
with st.sidebar:
    st.header("Settings ⚙️")
    if "dark_mode" not in st.session_state:                       # Initialize theme state
        st.session_state.dark_mode = False
    if st.toggle("🌙  Dark Theme", value=st.session_state.dark_mode, key="theme_toggle"):
        st.session_state.dark_mode = True
    else:
        st.session_state.dark_mode = False
    if st.session_state.dark_mode:
        st.markdown("""
            <style>
            .stApp { 
                background-color: #1e1e1e; 
                color: white;}
            [data-testid="stSidebar"] {
            background-color: #2c2c2c !important;
            }
            [data-testid="stSidebar"] * {
            color: white !important;
            }
                    
            .stTextInput > div > div > input,
            .stTextInput > label, 
            .stNumberInput label, 
            .stSelectbox label, 
            .stButton >button,
            .stDownloadbutton>button {
                color: inherit !important;
                background-color: inherit !important;
                border: none !important;}
            .stButton>button, .stDownloadbutton>button {
                background-color: #333 !important;
                color: white !important;
                border: 1px solid #555 !important;</style>
            """, unsafe_allow_html=True)
    else: 
        st.markdown("""
            <style>
            .stApp { 
                background-color: #def2f1 ; 
                color: black;}""", unsafe_allow_html=True)

st.markdown("<div class='sliding-text'>Welcome to QR Code Generator</div>", unsafe_allow_html=True)

st.image("image.png", use_container_width=True)

a1, a2, a3, a4= st.columns(4)
a1.metric("Fast Generation", "⚡0.2s", "Avg time ⏱️ ", border=True)
a2.metric("Dark Mode Users", "🌓 33%","+3 %", border=True)
a3.metric("User Satisfaction", "98%", "High 👍🏻", delta_color="inverse", border=True)
a4.metric("Multi-Device", "Ready", "📱💻🖥️", border=True)

st.container(height=100, border=False)

data= st.text_input("Enter the data for the QR code:", placeholder="Enter text, url, etc.")

if st.button("Generate QR Code"):
    if data:
        img = qrcode.make(data).convert("RGB")

        buf = BytesIO()                                           # Save the image in-memory buffer 
        img.save(buf, format="PNG")
        buf.seek(0)

        c1, c2, c3= st.columns(3)
        c2.image(buf, caption="-- Generated QR Code --", use_container_width=True)                      # Show the QR
        st.success("QR Code generated successfully!")
        c2.download_button("Download QR Code", 
                        data=buf,
                        file_name="QR_Code.png", 
                        mime="image/png", 
                        help="Click to download the QR Code",
                        use_container_width=True,
                        icon=":material/download:")
    else:
        st.error("Please enter some data to generate a QR code.")

st.container(height=50, border=False)

if "typing_done" not in st.session_state:
    text = "_**Hello there !!**, Welcome to my webpage here the information of my webpage_"
    placeholder = st.empty()
    context_text = ""

    for char in text:
        context_text += char
        placeholder.markdown(context_text)
        time.sleep(0.03)    
    st.session_state.typing_done = True
else:
    st.markdown("**Hello there !!**, Welcome to my webpage here the information of my webpage")

b1, b2 =st.columns(2)
b1.markdown("This QR Code Generator webpage is built using Python and Streamlit, offering a fast and interactive way to create QR codes from text or URLs. It uses the qrcode library to generate the codes, and Streamlit displays them instantly after input. The app includes features like a dark mode toggle, a download button for saving the QR code, and animated containers for a smooth user experience.")
b2.markdown("An external CSS file is used to style the webpage, giving it a modern and clean look beyond the default Streamlit design. Users can enter any text, link, or data, and the app instantly converts it into a scannable QR code. These codes can be used for sharing websites, contact info, Wi-Fi details, or event links, making the app both practical and easy to use.")

st.markdown('<h5 style="text-align: center;"><span style="color: grey;">Share Your Thoughts !!</span></h5>',
    unsafe_allow_html=True)
b1, b2, b3, b4, b5 = st.columns(5)
with b3:
    @st.dialog("Share your Thoughts ~")
    def email_form():
        name = st.text_input("Recipient Name", key="name")
        recipient = st.text_input("Recipient Email", key="email")
        message = st.text_area("Message", key="message")
        if st.button("Send", key="send"):
            st.session_state.email_sent = True                      # Here you would add your email-sending logic
            st.rerun()

    if "email_sent" not in st.session_state:
        if st.button("Write Here..."):
            email_form()
    else:
        st.success("Message sent!")

st.divider()
st.markdown('<p style="text-align: center;"><span style="color: grey;">-- Connect with us --</span></p>', unsafe_allow_html=True)
b1, b2, b3, b4 = st.columns(4)
b1.markdown("<u>Connect us</u>", unsafe_allow_html=True)
b1.markdown('<a href="https://www.linkedin.com/" target="_blank" style="color: #9ba3a3; text-decoration: none;">🔗 Linkedin</a>',unsafe_allow_html=True)
b1.markdown('<a href="https://github.com//" target="_blank" style="color: #9ba3a3; text-decoration: none;">🚀 GitHub</a>', unsafe_allow_html=True)

b2.markdown("<u>Social Media</u>", unsafe_allow_html=True)
b2.markdown('<a href="https://www.facebook.com" target="_blank" style="color: #9ba3a3; text-decoration: none;">👍🏼 Facebook</a>', unsafe_allow_html=True)
b2.markdown('<a href="https://www.instagram.com/" target="_blank" style="color: #9ba3a3; text-decoration: none;">📷 Instagram</a>', unsafe_allow_html=True)

b3.markdown("<u>About us</u>", unsafe_allow_html=True)
b3.markdown('<a href="https://www.google.co.in/" target="_blank" style="color: #9ba3a3; text-decoration: none;">🔍 About</a>', unsafe_allow_html=True)
b3.markdown('<a href="https://www.google.co.in/" target="_blank" style="color: #9ba3a3; text-decoration: none;">💼 Careers</a>',  unsafe_allow_html=True)

b4.markdown("<u>Contact us</u>", unsafe_allow_html=True)
b4.markdown('<a href="https://www.google.co.in/" target="_blank" style="color: #9ba3a3; text-decoration: none;">✉️ Email.com</a>', unsafe_allow_html=True)
b4.markdown('<a href="https://www.google.co.in/" target="_blank" style="color: #9ba3a3; text-decoration: none;">📞 +91 0123456789</a>', unsafe_allow_html=True)

st.divider()

st.image("https://i.pinimg.com/originals/c2/63/d2/c263d2184f802a05ef422346a937ed1a.gif", 
         caption="-- Thank you for visiting us --", 
         use_container_width=True)
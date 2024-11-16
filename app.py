import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configure the generative model with the API key
f=open(r"C:\Users\yuvraj\Downloads\keys\geminiAPI.txt")
key=f.read()
genai.configure(api_key=key)
#genai.configure(api_key="AIzaSyAxYojiuaLswHwedp5Iqaa7m7VZlcPd1v8")

sys_prompt = """You are an AI code reviewer specializing in providing detailed and constructive feedback on code quality,
                readability, optimization, and adherence to best practices. Your expertise covers multiple programming languages,
                algorithms, and design patterns. If the user's request is unrelated to code review,
                politely respond with: 'Sorry, I’m programmed specifically to review code and cannot assist with other topics.'
                Always aim to offer clear, actionable, and concise feedback.
                And Your output code should be in diffrent line with a bulletpoint and output should contain whole rewrited fixed code."""

model = genai.GenerativeModel(model_name="models/gemini-1.5-flash", 
                              system_instruction=sys_prompt)

# Load an AI bot image
ai_bot_image = Image.open("ai_bot.png")  # Replace with the path to your AI bot image

# Streamlit UI components
col1, col2 = st.columns([1, 7])  # Create two columns for layout
with col1:
    st.image(ai_bot_image, width=80)  # Display the AI bot image

with col2:
    st.title("AI :blue[Code] Reviewer:keyboard:")
    st.sidebar.subheader("Enter Your :blue[Code] Here:sunglasses::arrow_heading_down:")

user_prompt = st.sidebar.text_input("Enter your query:", placeholder="Type your query here...")

btn_click = st.sidebar.button("Generate Answer")
if btn_click:
    # Create a placeholder for the "Please Wait..." message
    running_placeholder = st.empty()
    running_placeholder.subheader("Please Wait Running Is In Process...:hourglass_flowing_sand:\n Your Output Will Be Generated Shortly!!! Have A Sip Of Coffee.:coffee:")

if btn_click and user_prompt.strip():
    try:
        response = model.generate_content(user_prompt)
        # Replace the "Please Wait..." message with the result
        running_placeholder.empty()  # Clear the placeholder
        st.text_area("Output:", value=response.text, height=300)
    except Exception as e:
        st.error(f"An error occurred: {e}")

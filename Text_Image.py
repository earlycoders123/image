import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Replace with your actual Stability AI API Key
API_KEY = "sk-rXn4kzhTxnzBdJK5u9MryCmzmzY1tM0lqE7aPRUz4S3BkATq"

# Stability AI API endpoint
API_URL = "https://api.stability.ai/v2beta/stable-image/generate/sd3"

# Streamlit App
st.title("🎨 AI Picture Maker")
st.write("Type anything and AI will draw it!")

# Get user prompt
prompt = st.text_input("What should AI draw?")

# Generate Button
if st.button("Generate Image"):
    if prompt:
        st.info("Please wait... AI is drawing your picture!")
        # Prepare the API request (multipart/form-data)
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Accept": "image/*"
        }
        files = {
            'prompt': (None, prompt),
            'output_format': (None, 'png')
        }

        # API Request
        response = requests.post(API_URL, headers=headers, files=files)

        # Handle API Response
        if response.status_code == 200:
            image = Image.open(BytesIO(response.content))
            st.image(image, caption="Here’s your AI-generated picture!")

            st.download_button("Download Image", response.content, "AI_Picture.png", "image/png")
        else:
            st.error("Oops! Something went wrong. Please check your API key or try again.")
    else:
        st.warning("Please type something for AI to draw!")

st.caption("Made with ❤️ using Stability AI and Streamlit")

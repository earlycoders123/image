import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Stability AI API Key (store securely in st.secrets in production)
API_KEY = "sk-rXn4kzhTxnzBdJK5u9MryCmzmzY1tM0lqE7aPRUz4S3BkATq"

# API Endpoint
API_URL = "https://api.stability.ai/v2beta/stable-image/generate/sd3"

# Headers
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "image/png"
}

# Streamlit App UI
st.set_page_config(page_title="Stability AI Image Generator", page_icon="🎨")
st.title("🎨 Stability AI Image Generator for Kids")
st.write("Type anything, and AI will draw it for you!")

# User Input
prompt = st.text_input("📝 What should AI draw?")

# Generate Button
if st.button("✨ Generate Image"):
    if prompt.strip() != "":
        with st.spinner("Drawing your image..."):
            json_data = {
                "prompt": prompt,
                "output_format": "png"
            }
            response = requests.post(API_URL, headers=headers, json=json_data)

            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                st.image(image, caption="🎉 Here’s your AI-generated image!")

                st.download_button(
                    label="📥 Download Image",
                    data=response.content,
                    file_name="ai_image.png",
                    mime="image/png"
                )
            else:
                st.error(f"Failed to generate image. Status Code: {response.status_code}")
    else:
        st.warning("Please enter a description!")

st.caption("Made with ❤️ using Stability AI and Streamlit")

import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Your Stability AI API Key (use Streamlit secrets in production)
API_KEY = "sk-rXn4kzhTxnzBdJK5u9MryCmzmzY1tM0lqE7aPRUz4S3BkATq"

# API Endpoint
API_URL = "https://api.stability.ai/v2beta/stable-image/generate/sd3"

# Headers
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "image/png",
    "Content-Type": "application/json"
}

# Streamlit App
st.set_page_config(page_title="Stability AI Image Generator", page_icon="🎨")
st.title("🎨 AI Image Generator using Stability AI")
st.write("Describe anything, and AI will draw it for you!")

prompt = st.text_input("📝 What should AI draw for you?")

if st.button("✨ Generate Image"):
    if prompt.strip():
        with st.spinner("Generating your image..."):
            payload = {
                "prompt": prompt,
                "output_format": "png"
            }

            response = requests.post(API_URL, headers=headers, json=payload)

            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                st.image(image, caption="🎉 Here's your AI-generated image!")

                st.download_button(
                    label="📥 Download Image",
                    data=response.content,
                    file_name="ai_image.png",
                    mime="image/png"
                )
            else:
                st.error(f"❌ Failed to generate image. Status Code: {response.status_code}")
                st.json(response.json())
    else:
        st.warning("Please enter a description!")

st.caption("Made with ❤️ using Stability AI SD3 and Streamlit")

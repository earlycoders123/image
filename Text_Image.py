import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Set your Hugging Face API Key
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2"
HF_API_KEY = "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"  # Use st.secrets on Streamlit Cloud

headers = {"Authorization": f"Bearer {HF_API_KEY}"}

# Streamlit App Setup
st.set_page_config(page_title="Hugging Face AI Image Generator", page_icon="🎨")
st.title("🎨 AI Text-to-Image Generator for Kids")
st.write("Describe anything and AI will draw it for you!")

# Input
prompt = st.text_input("📝 Describe your image:")

if st.button("🎨 Generate Image"):
    if prompt.strip():
        with st.spinner("Creating your image..."):
            response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
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
        st.warning("Please describe what you want to see!")

st.caption("Made with ❤️ using Hugging Face Stable Diffusion and Streamlit")

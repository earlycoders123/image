import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Use your Stability API Key
API_KEY = "sk-rXn4kzhTxnzBdJK5u9MryCmzmzY1tM0lqE7aPRUz4S3BkATq"  # Store in Streamlit Secrets in production

# API Endpoint
API_URL = "https://api.stability.ai/v2beta/stable-image/generate/sd3"

# Headers (only Authorization and Accept needed)
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "image/*"
}

# Streamlit App
st.set_page_config(page_title="Stability AI Image Generator", page_icon="🎨")
st.title("🎨 AI Image Generator using Stability AI SD3")
st.write("Describe anything, and AI will draw it for you!")

prompt = st.text_input("📝 What should AI draw for you?")

if st.button("✨ Generate Image"):
    if prompt.strip():
        with st.spinner("Generating your image..."):
            # Sending as multipart/form-data
            files = {
                'prompt': (None, prompt),
                'output_format': (None, 'png')
            }

            response = requests.post(API_URL, headers=headers, files=files)

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
                try:
                    st.json(response.json())
                except:
                    st.write(response.text)
    else:
        st.warning("Please enter a description!")

st.caption("Made with ❤️ using Stability AI SD3 and Streamlit")

import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# Stability AI API Key (store in secrets for production)
API_KEY = "sk-rXn4kzhTxnzBdJK5u9MryCmzmzY1tM0lqE7aPRUz4S3BkATq"

# API Endpoint for SD 1.5 (v1 API - Lower Credit Usage)
API_URL = "https://api.stability.ai/v1/generation/stable-diffusion-512-v2-1/text-to-image"

# Headers
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "image/png"
}

# Streamlit App
st.set_page_config(page_title="Stability AI Image Generator (Cheaper Model)", page_icon="🎨")
st.title("🎨 AI Image Generator (Stable Diffusion 2.1)")
st.write("Describe anything and get your AI-generated image at lower cost!")

prompt = st.text_input("📝 What should AI draw for you?")

if st.button("✨ Generate Image"):
    if prompt.strip():
        with st.spinner("Generating your image..."):
            # Payload using older v1 API
            json_payload = {
                "text_prompts": [{"text": prompt}],
                "cfg_scale": 7,
                "clip_guidance_preset": "FAST_BLUE",
                "samples": 1,
                "steps": 30
            }

            response = requests.post(API_URL, headers=headers, json=json_payload)

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

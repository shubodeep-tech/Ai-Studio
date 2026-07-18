import streamlit as st
import requests
import urllib.parse
import random

st.set_page_config(page_title="AI Image Studio", page_icon="🎨")

st.title(" AI Image Studio")
st.write("Turn your imagination into images!")


st.sidebar.header("Settings")

art_style = st.sidebar.selectbox(
    "Choose an art style",
    ["Realistic", "Anime", "Cyberpunk", "Watercolor", "Pixel Art", "Oil Painting"]
)

width = st.sidebar.slider("Width", min_value=256, max_value=1024, value=512, step=64)
height = st.sidebar.slider("Height", min_value=256, max_value=1024, value=512, step=64)

magic_enhance = st.sidebar.checkbox(" Enable Magic Enhance")


user_prompt = st.text_input("Enter your prompt", placeholder="e.g. A dragon flying over a castle")


surprise_prompts = [
    "An astronaut riding a horse on Mars",
    "A cyberpunk street food vendor in Tokyo",
    "A dragon made entirely of stained glass",
    "A pirate ship sailing through the clouds",
    "A robot tending a zen garden at sunset",
]

col1, col2 = st.columns(2)
generate_clicked = col1.button("Generate")
surprise_clicked = col2.button(" Surprise Me!")


def build_image(prompt_text: str):
    """Builds the full prompt, calls the API with correct params, and displays/downloads the image."""
    full_prompt = f"{art_style} style: {prompt_text}"

    if magic_enhance:
        full_prompt += ", masterpiece, 8k resolution, highly detailed, trending on artstation, unreal engine 5 render"

    encoded_prompt = urllib.parse.quote(full_prompt)


    url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width={width}&height={height}"

    with st.spinner("Generating your image..."):
        response = requests.get(url)

    if response.status_code == 200:
        st.image(response.content, caption=prompt_text, use_container_width=True)


        st.download_button(
            label=" Download Image",
            data=response.content,
            file_name=f"{art_style}_image.png",
            mime="image/png",
        )
    else:
        st.error("Failed to generate image. Please try again.")



if generate_clicked:
    if user_prompt.strip() == "":
        st.warning("Please enter a prompt first!")
    else:
        build_image(user_prompt)

if surprise_clicked:

    random_prompt = random.choice(surprise_prompts)
    st.info(f"Surprise prompt: **{random_prompt}**")
    build_image(random_prompt)
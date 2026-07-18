Live Demo:  https://ai-studio-2p9382w5dunpbqtdtuyvua.streamlit.app/
<img width="2920" height="1794" alt="3E78D0B7-E9CB-4AC7-9B5F-8AFA73EF0323" src="https://github.com/user-attachments/assets/db1c3a64-9ac2-4891-915a-0b86d8edde05" />

#  AI Image Studio

A simple Streamlit web app that turns text prompts into AI-generated images using the [Pollinations AI](https://pollinations.ai/) image API.

Built as part of the **MirAI School of Technology — Virtual Summer Internship 2026: AI Builder Track**.

## Features

- **Custom prompts** — type any idea and generate an image from it
- **Art style selector** — Realistic, Anime, Cyberpunk, Watercolor, Pixel Art, Oil Painting
- **Working width/height sliders** — actually control the generated image dimensions
- **✨ Magic Enhance** — a toggle that secretly boosts your prompt with quality keywords (`masterpiece, 8k resolution, highly detailed, trending on artstation, unreal engine 5 render`) for better results
- **🎲 Surprise Me** — stuck for ideas? Click this to generate a random creative prompt instantly
- **Download button** — saves the image with a proper `.png` extension, named after the chosen art style

## Requirements

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [Requests](https://docs.python-requests.org/)

## Installation

```bash
pip install streamlit requests
```

## Usage

1. Clone this repository:
   ```bash
   git clone https://github.com/you/repo.git
   cd repo
   ```
2. Run the app:
   ```bash
   streamlit run app.py
   ```
3. Open the local URL Streamlit gives you (usually `http://localhost:8501`) in your browser.
4. Enter a prompt, tweak the settings in the sidebar, and click **Generate** — or click **Surprise Me** for a random idea.
5. Download your finished image using the **Download Image** button.

## Project Structure

```
.
├── app.py          # Main Streamlit application
└── README.md       # Project documentation
```

## How It Works

The app sends your prompt (plus selected width, height, and optional enhancement keywords) to the Pollinations AI image endpoint:

```
https://image.pollinations.ai/prompt/{prompt}?width={width}&height={height}
```

The returned image is displayed in the app and made available for download as a `.png` file.

## Credits

- Image generation powered by [Pollinations.ai](https://pollinations.ai/)
- Built with [Streamlit](https://streamlit.io/)
- Created for MirAI School of Technology's AI Builder internship track

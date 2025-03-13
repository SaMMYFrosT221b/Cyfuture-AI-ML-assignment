# Image Generation with Stable Diffusion and DALL-E

This Python script allows you to generate images using either Stable Diffusion or DALL-E models.

## Prerequisites

- Python 3.7 or higher
- CUDA-capable GPU (for Stable Diffusion)
- OpenAI API key

## Installation

1. Clone this repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the script:
   ```
   python main.py
   ```

2. When prompted:
   - Enter your OpenAI API key
   - Type your image description/prompt
   - Choose the model:
     - Type 'sd' for Stable Diffusion
     - Type 'dalle' for DALL-E

3. The generated image will be saved as:
   - `sd_image.png` for Stable Diffusion
   - `dalle_image.png` for DALL-E

## Notes

- Stable Diffusion requires a GPU with CUDA support
- DALL-E requires a valid OpenAI API key and internet connection
- Generated images are saved in the same directory as the script
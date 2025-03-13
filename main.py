import torch
from diffusers import StableDiffusionPipeline
import openai
from PIL import Image
import requests
from io import BytesIO

# Ask for OpenAI API Key from the user
openai.api_key = input("Enter your OpenAI API key: ").strip()

# Load Stable Diffusion Model
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe.to("cuda")  # Use GPU if available

# Function to generate image using Stable Diffusion
def generate_image_sd(prompt, output_path="sd_image.png"):
    image = pipe(prompt).images[0]  # Generate image
    image.save(output_path)  # Save the image
    print(f"Stable Diffusion Image saved at: {output_path}")

# Function to generate image using DALL-E
def generate_image_dalle(prompt, output_path="dalle_image.png"):
    response = openai.Image.create(
        prompt=prompt,
        n=1,  # Generate one image
        size="1024x1024"
    )
    image_url = response['data'][0]['url']  # Get image URL
    image = Image.open(BytesIO(requests.get(image_url).content))  # Download image
    image.save(output_path)  # Save the image
    print(f"DALL-E Image saved at: {output_path}")

# Ask for user input
prompt = input("Enter the image description: ").strip()
model_choice = input("Choose model (sd/dalle): ").strip().lower()

# Generate image based on user choice
if model_choice == "sd":
    generate_image_sd(prompt)
elif model_choice == "dalle":
    generate_image_dalle(prompt)
else:
    print("Invalid choice. Please select 'sd' or 'dalle'.")

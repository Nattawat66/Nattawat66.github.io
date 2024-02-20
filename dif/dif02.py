import torch
from diffusers import DiffusionPipeline as DP
from PIL import Image

def text_to_image(text, diffuser_model):
    dp = DP.from_pretrained("runwayml/stable-diffusion-v1-5")
    image_data = dp(text).images[0]
    image = Image.fromarray(image_data)
    image.show()

if __name__ == "__main__":
    input_text = "Hello, World!"
    diffuser_model = "Example_diffuser_model"
    text_to_image(input_text, diffuser_model)

import gradio as gr
from rembg import remove
from PIL import Image
import io

def remove_background(input_img):
    img_byte_arr = io.BytesIO()
    input_img.save(img_byte_arr, format='PNG')
    result = remove(img_byte_arr.getvalue())
    output = Image.open(io.BytesIO(result)).convert("RGBA")
    return output

interface = gr.Interface(
    fn=remove_background,
    inputs=gr.Image(type="pil"),
    outputs="image",
    title="Background Remover",
    description="Upload an image to remove its background. Output will be transparent PNG."
)

interface.launch()

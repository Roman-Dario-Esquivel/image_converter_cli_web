from PIL import Image
import cairosvg
import os

def convert_svg_to_png(svg_path, temp_path):
    cairosvg.svg2png(url=svg_path, write_to=temp_path)

def apply_watermark(base_img, watermark_path):
    ext = os.path.splitext(watermark_path)[1].lower()
    if ext == ".svg":
        watermark_path = watermark_path.replace(".svg", "_temp.png")
        convert_svg_to_png(watermark_path.replace("_temp.png", ".svg"), watermark_path)

    watermark = Image.open(watermark_path).convert("RGBA")
    watermark = watermark.resize((int(base_img.width * 0.3), int(base_img.height * 0.3)))
    position = (base_img.width - watermark.width - 10, base_img.height - watermark.height - 10)
    base_img.paste(watermark, position, watermark)
    return base_img

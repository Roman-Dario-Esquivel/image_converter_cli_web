import os
import subprocess
from PIL import Image
from modules.watermark import apply_watermark

def get_size_kb(path):
    return round(os.path.getsize(path) / 1024, 2)

def process_image(input_path, output_dir, formats, width, height, quality, watermark_path, dry_run=False):
    name = os.path.splitext(os.path.basename(input_path))[0]
    original_size = get_size_kb(input_path)

    if dry_run:
        print(f"🔍 Simulación: {name} → Formatos: {formats}")
        return {
            "name": os.path.basename(input_path),
            "original_size": original_size,
            "webp_size": "simulado" if "webp" in formats else "-",
            "avif_size": "simulado" if "avif" in formats else "-"
        }

    img = Image.open(input_path).convert("RGB")
    img = img.resize((width, height)) if width and height else img
    if watermark_path:
        img = apply_watermark(img, watermark_path)

    temp_path = os.path.join(output_dir, f"{name}_temp.jpg")
    img.save(temp_path, optimize=True)

    result = {
        "name": os.path.basename(input_path),
        "original_size": original_size
    }

    if "webp" in formats:
        webp_path = os.path.join(output_dir, f"{name}.webp")
        subprocess.run(["cwebp", "-q", str(quality), temp_path, "-o", webp_path])
        result["webp_size"] = get_size_kb(webp_path)

    if "avif" in formats:
        avif_path = os.path.join(output_dir, f"{name}.avif")
        subprocess.run(["avifenc", "--min", str(quality-20), "--max", str(quality), temp_path, avif_path])
        result["avif_size"] = get_size_kb(avif_path)

    os.remove(temp_path)
    return result

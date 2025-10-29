import argparse
import os
from modules.logger import setup_logger, log_status
from modules.processor import process_image
from modules.reporter import Report
from tqdm import tqdm

def main():
    parser = argparse.ArgumentParser(description="Conversor de imágenes optimizado para WebP y AVIF")
    parser.add_argument("--input", required=True, help="Carpeta de entrada")
    parser.add_argument("--output", required=True, help="Carpeta de salida")
    parser.add_argument("--format", required=True, help="Formatos: webp, avif o ambos separados por coma")
    parser.add_argument("--width", type=int, help="Ancho deseado")
    parser.add_argument("--height", type=int, help="Alto deseado")
    parser.add_argument("--quality", type=int, default=80, help="Calidad de compresión (0-100)")
    parser.add_argument("--watermark", help="Ruta a imagen PNG/SVG como marca de agua")
    parser.add_argument("--log", help="Archivo de log")
    parser.add_argument("--csv", help="Archivo de reporte CSV")

    args = parser.parse_args()
    formats = [f.strip() for f in args.format.split(",")]
    os.makedirs(args.output, exist_ok=True)

    logger = setup_logger(args.log) if args.log else None
    report = Report(args.csv) if args.csv else None

    for file in tqdm(os.listdir(args.input)):
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(args.input, file)
            try:
                result = process_image(
                    input_path=input_path,
                    output_dir=args.output,
                    formats=formats,
                    width=args.width,
                    height=args.height,
                    quality=args.quality,
                    watermark_path=args.watermark
                )
                if logger: log_status(logger, result)
                if report: report.add(result)
            except Exception as e:
                if logger: log_status(logger, {"name": file, "error": str(e)})
                if report: report.add_error(file, str(e))

    if report: report.save()

if __name__ == "__main__":
    main()

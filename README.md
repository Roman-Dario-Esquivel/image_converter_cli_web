# 🖼️ Image Converter CLI & WebP/AVIF

(ES) Este proyecto proporciona una herramienta de línea de comandos (CLI) escrita en **Python** para la conversión eficiente de imágenes. Permite transformar archivos **JPG, JPEG y PNG** a formatos modernos como **WebP y AVIF**, con opciones avanzadas de procesamiento como redimensionado, aplicación de marcas de agua, *logging* y generación de reportes CSV.

(EN) This project provides a command-line interface (CLI) tool written in **Python** for efficient image conversion. It allows transforming **JPG, JPEG, and PNG** files into modern formats like **WebP and AVIF**, with advanced processing options such as resizing, watermarking, logging, and CSV report generation.

---

## 🚀 Funcionalidades / Key Features

### (ES)
* **Conversión a formatos modernos:** Soporte para **WebP** y **AVIF**.
* **Procesamiento por lotes:** Convierte múltiples imágenes de una carpeta de entrada.
* **Opciones avanzadas:** Control de calidad, redimensionado (`--width`, `--height`), y marca de agua (`--watermark`).
* **Reportes:** Generación de archivos **CSV** con el resumen de la conversión.
* **Simulación:** Modo *dry-run* para previsualizar acciones sin modificar archivos.
* **Logging:** Guardado detallado de la ejecución en un archivo de log.

### (EN)
* **Modern Format Conversion:** Support for **WebP** and **AVIF**.
* **Batch Processing:** Converts multiple images from an input folder.
* **Advanced Options:** Quality control, resizing (`--width`, `--height`), and watermarking (`--watermark`).
* **Reporting:** Generation of **CSV** files with a conversion summary.
* **Simulation:** Dry-run mode to preview actions without modifying files.
* **Logging:** Detailed execution logging saved to a file.

---

## 🛠️ Instalación y Uso / Installation and Usage

### (ES) Prerrequisitos / (EN) Prerequisites

Necesitas tener **Python 3** instalado. / You need to have **Python 3** installed.

### (ES) Instalación / (EN) Installation

1.  Clona este repositorio / Clone this repository:
    ```bash
    git clone [https://github.com/Roman-Dario-Esquivel/image_converter_cli_web.git](https://github.com/Roman-Dario-Esquivel/image_converter_cli_web.git)
    cd image_converter_cli_web
    ```
2.  Instala las dependencias necesarias. / Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    # (Opcional) Usando entorno virtual: / (Optional) Using virtual environment:
    # python3 -m venv venv
    # source venv/bin/activate
    # pip install -r requirements.txt
    ```

### (ES) Estructura Básica del Comando / (EN) Basic Command Structure

```bash
python3 convert_images.py --input <input_folder> --output <output_folder> --format <webp|avif|webp,avif> [options]
```
| Caso de Uso / Use Case                                                                        | Comando de Ejemplo / Example Command                                                                                   |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| (ES) Conversión simple a WebP / (EN) Simple WebP Conversion                                   | `python3 convert_images.py --input ./originales --output ./convertidas/webp --format webp`                             |
| (ES) A WebP y AVIF con calidad 90 / (EN) To WebP and AVIF with quality 90                     | `python3 convert_images.py --input ./originales --output ./convertidas/alta_calidad --format webp,avif --quality 90`   |
| (ES) Redimensionado (1024x768) con marca de agua / (EN) Resizing (1024x768) with Watermark    | `python3 convert_images.py --input ./originales --output ./convertidas/redimensionadas --format webp,avif --width 1024 --height 768 --watermark ./marca.svg` |
|                                                                                               |
| (ES) Simulación (Dry-Run) / (EN) Simulation (Dry-Run)                | `python3 convert_images.py --input ./originales --output ./convertidas/simulacion --format webp,avif --dry-run`        |
| (ES) Reporte CSV y Log completo / (EN) Complete CSV Report and Log  | `python3 convert_images.py --input ./originales --output ./convertidas/completo --format webp,avif --log ./logs/conversion.log --csv ./reportes/` |


| Parámetro / Parameter | (ES) Descripción                                      | (EN) Description                                      | Obligatorio / Required |
|-----------------------|------------------------------------------------------|-------------------------------------------------------|------------------------|
| `--input`             | Carpeta con imágenes originales.                     | Folder with original images.                          | ✅                     |
| `--output`            | Carpeta donde se guardarán las convertidas.          | Folder where converted files will be saved.           | ✅                     |
| `--format`            | Formatos de salida: webp, avif o ambos.              | Output formats: webp, avif, or both.                  | ✅                     |
| `--width`             | Ancho deseado (opcional).                            | Desired width (optional).                             | ❌                     |
| `--height`            | Alto deseado (opcional).                             | Desired height (optional).                            | ❌                     |
| `--quality`           | Calidad de compresión (0–100, por defecto 80).       | Compression quality (0–100, default 80).              | ❌                     |
| `--watermark`         | Ruta a imagen PNG o SVG como marca de agua.          | Path to PNG or SVG image for watermarking.            | ❌                     |
| `--log`               | Ruta al archivo de log.                              | Path to the log file.                                 | ❌                     |
| `--csv`               | Ruta o carpeta para guardar el reporte CSV.          | Path or folder to save the CSV report.                | ❌                     |
| `--dry-run`           | Simula la conversión sin guardar archivos.           | Simulates conversion without saving files.            | ❌                     |
| `--no-console`        | Oculta el resumen en consola.                        | Hides the console summary.                            | ❌                     |


✒️ Autor
[Roman Darío Esquivel](https://github.com/Roman-Dario-Esquivel)  – Desarrollador principal del proyecto

⚖️ Licencia / License
(ES) Este proyecto está distribuido bajo la Licencia Apache 2.0. Consulta el archivo LICENSE para más detalles.

(EN) This project is distributed under the Apache License 2.0. See the LICENSE file for more details.

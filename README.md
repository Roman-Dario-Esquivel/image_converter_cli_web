Ejemplos de uso del conversor CLI
Este conversor permite transformar imágenes .jpg, .jpeg y .png en formatos WebP y AVIF, con opciones avanzadas como redimensionado, marca de agua, simulación (--dry-run), logging y generación de reportes CSV.

🧱 Estructura básica
bash
python3 convert_images.py \
  --input <carpeta_entrada> \
  --output <carpeta_salida> \
  --format <formatos> \
  [opciones]
✅ Ejemplo 1: Conversión simple a WebP
bash
python3 convert_images.py \
  --input ./originales \
  --output ./convertidas/webp \
  --format webp
Convierte todas las imágenes a WebP sin redimensionar ni aplicar marca de agua.

✅ Ejemplo 2: Conversión a WebP y AVIF con calidad personalizada
bash
python3 convert_images.py \
  --input ./originales \
  --output ./convertidas/alta_calidad \
  --format webp,avif \
  --quality 90
Convierte a ambos formatos con calidad 90 (más alta que el valor por defecto de 80).

✅ Ejemplo 3: Redimensionado + marca de agua SVG
bash
python3 convert_images.py \
  --input ./originales \
  --output ./convertidas/redimensionadas \
  --format webp,avif \
  --width 1024 \
  --height 768 \
  --watermark ./marca.svg
Redimensiona las imágenes a 1024x768 y aplica una marca de agua SVG.

✅ Ejemplo 4: Conversión completa con log y reporte CSV
bash
python3 convert_images.py \
  --input ./originales \
  --output ./convertidas/completo \
  --format webp,avif \
  --quality 80 \
  --log ./logs/conversion.log \
  --csv ./reportes/
Guarda el log en ./logs/conversion.log

Genera un reporte CSV con fecha en ./reportes/reporte_YYYYMMDD_HHMM.csv

Muestra resumen en consola

✅ Ejemplo 5: Simulación sin guardar archivos (--dry-run)
bash
python3 convert_images.py \
  --input ./originales \
  --output ./convertidas/simulacion \
  --format webp,avif \
  --quality 80 \
  --dry-run
Simula la conversión sin guardar archivos. Ideal para validar antes de ejecutar en producción.

✅ Ejemplo 6: Conversión silenciosa (--no-console)
bash
python3 convert_images.py \
  --input ./originales \
  --output ./convertidas/silencioso \
  --format webp,avif \
  --csv ./reportes/reporte_silencioso.csv \
  --no-console
No muestra el resumen en consola. Solo guarda el reporte CSV.

📦 Parámetros disponibles
Parámetro	Descripción
--input	Carpeta con imágenes originales (obligatorio)
--output	Carpeta donde se guardarán las convertidas (obligatorio)
--format	Formatos de salida: webp, avif o ambos separados por coma
--width	Ancho deseado (opcional)
--height	Alto deseado (opcional)
--quality	Calidad de compresión (0–100, por defecto 80)
--watermark	Ruta a imagen PNG o SVG como marca de agua (opcional)
--log	Ruta al archivo de log (opcional)
--csv	Ruta o carpeta para guardar el reporte CSV (opcional)
--dry-run	Simula la conversión sin guardar archivos
--no-console	Oculta el resumen en consola (solo útil si usás --csv)
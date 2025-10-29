import logging
from datetime import datetime

def setup_logger(log_path):
    logging.basicConfig(filename=log_path, level=logging.INFO)
    return logging.getLogger()

def log_status(logger, data):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if "error" in data:
        logger.info(f"[{timestamp}] ❌ {data['name']} → Error: {data['error']}")
    else:
        logger.info(f"[{timestamp}] ✅ {data['name']} → WebP: {data.get('webp_size','-')}KB | AVIF: {data.get('avif_size','-')}KB")

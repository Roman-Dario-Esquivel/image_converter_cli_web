def setup_logger(log_path=None):
    if log_path:
        logging.basicConfig(filename=log_path, level=logging.INFO)
        return logging.getLogger()
    return None

def log_status(logger, data):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    mensaje = ""
    if "error" in data:
        mensaje = f"[{timestamp}] ❌ {data['name']} → Error: {data['error']}"
    else:
        mensaje = f"[{timestamp}] ✅ {data['name']} → WebP: {data.get('webp_size','-')}KB | AVIF: {data.get('avif_size','-')}KB"
    
    print(mensaje)
    if logger:
        logger.info(mensaje)

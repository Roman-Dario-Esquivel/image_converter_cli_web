import csv
import os
from datetime import datetime
from tabulate import tabulate

class Report:
    def __init__(self, path=None):
        self.rows = []
        self.path = path
        if self.path:
            # Crear carpeta si no existe
            os.makedirs(os.path.dirname(self.path), exist_ok=True)

    def add(self, data):
        self.rows.append([
            data["name"],
            data["original_size"],
            data.get("webp_size", "-"),
            data.get("avif_size", "-"),
            "OK"
        ])

    def add_error(self, name, error):
        self.rows.append([name, "-", "-", "-", f"Error: {error}"])

    def show(self):
        print("\n📊 Resumen de conversión:\n")
        print(tabulate(
            self.rows,
            headers=["Imagen", "Original (KB)", "WebP (KB)", "AVIF (KB)", "Estado"],
            tablefmt="fancy_grid"
        ))

    def save(self):
        if not self.path:
            return
        with open(self.path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Imagen", "Original (KB)", "WebP (KB)", "AVIF (KB)", "Estado"])
            writer.writerows(self.rows)

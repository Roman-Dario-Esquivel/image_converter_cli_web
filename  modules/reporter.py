import csv
import os

class Report:
    def __init__(self, path):
        self.path = path
        self.rows = []

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

    def save(self):
        with open(self.path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Imagen", "Original (KB)", "WebP (KB)", "AVIF (KB)", "Estado"])
            writer.writerows(self.rows)

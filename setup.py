from setuptools import setup, find_packages

setup(
    name="image_converter_cli",
    version="1.0",
    packages=find_packages(),
    py_modules=["convert_images"],
    entry_points={
        "console_scripts": [
            "imgconvert=convert_images:main"
        ]
    },
    install_requires=[
        "pillow",
        "tabulate",
        "tqdm"
    ],
    entry_points={
        "console_scripts": [
            "imgconvert=convert_images:main"
        ]
    },
    author="Roman",
    description="Conversor de imágenes modular para WebP y AVIF con CLI",
)


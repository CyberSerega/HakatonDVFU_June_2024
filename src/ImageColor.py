from PIL import Image
from colorthief import ColorThief

def generate_color(image_path):
    # Извлечение основных цветов из изображения
    color_thief = ColorThief(image_path)
    palette = color_thief.get_palette(color_count=5)
    return palette

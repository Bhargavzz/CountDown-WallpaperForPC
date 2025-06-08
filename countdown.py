from PIL import Image, ImageDraw, ImageFont
from datetime import date
import ctypes

# Set your target date
target_date = date(2025, 7, 31)
today = date.today()
days_left = (target_date - today).days

# Create a blank image (1920x1080, black background)
background = Image.new('RGB', (1920, 1080), color='black')
draw = ImageDraw.Draw(background)

# Load font
font_path = r"C:\Windows\Fonts\arial.ttf"
font = ImageFont.truetype(font_path, 127.5)

# Draw the countdown text
text = f"{days_left} Days to Go"
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
x = (1920 - text_width) // 2
y = (1080 - text_height) // 2
draw.text((x, y), text, font=font, fill="white")

# Save and set as wallpaper
output_path = r"C:\Users\vishn\OneDrive\Desktop\Countdown\wallpaper_updated.jpg"
background.save(output_path)

ctypes.windll.user32.SystemParametersInfoW(20, 0, output_path, 3)

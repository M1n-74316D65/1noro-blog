#!/usr/bin/env python3
# install pillow with pip3 install pillow
# install pillow in archlinux with pacman -S python-pillow
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# URL de la imagen
# thanks to https://picsum.photos/
url = "https://picsum.photos/1300/715/?blur=3"

# Descargar la imagen
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# Obtener las dimensiones de la imagen
width, height = img.size

# Calcular el valor promedio de los píxeles de la imagen
avg_pixel_value = sum(img.convert("L").getdata()) / (width * height)

# Elegir el color del texto en función del valor promedio de los píxeles
if avg_pixel_value < 128:
    text_color = "white"
else:
    text_color = "black"

# Crear un objeto ImageDraw
draw = ImageDraw.Draw(img)

# Escribir el texto en el centro de la imagen
text = "rats.land"
textheight = 100
font = ImageFont.truetype("res/PublicSans-Bold.ttf", textheight)
textwidth = draw.textlength(text, font=font)
x = (width - textwidth) / 2
y = (height - textheight) / 2
# draw.text((x, y), text, font=font)
draw.text((x, y), text, font=font, fill=text_color)

# Guardar la imagen con la marca de agua
img.save("out.jpg")

import pytesseract
from PIL import Image

image = Image.open('D:\screenshot4\\6.jpg')
result = pytesseract.image_to_string(image)

print(result)
pip install pillow
from google.colab import files
files.upload()
from PIL import Image

# Load uploaded image
image = Image.open("invicta.jpg")   # change name if needed

# Resize image
resized = image.resize((300, 300))

# Convert and save
resized.save("output.png")
resized.save("output.bmp")
resized.save("output.jpg")

print("Image resized and converted successfully")
from google.colab import files
files.download("output.png")
files.download("output.bmp")
files.download("output.jpg")

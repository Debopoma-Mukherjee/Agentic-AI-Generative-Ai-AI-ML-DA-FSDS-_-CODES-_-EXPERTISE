import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import requests 
from io import BytesIO

def load_image_from_url(url):
    response=requests.get(url)
    return Image.open(BytesIO(response.content))

image_url=r"https://images.all-free-download.com/images/thumbjpg/sunflower_yellow_flowers_215332.jpg"
image=load_image_from_url(image_url)

plt.figure(figsize=(6,4))
plt.imshow(image)
plt.title("Black and White Cat")
plt.axis("off")
plt.show()

elephant_np=np.array(image)
print("Image shape:", elephant_np.shape)

image_gray=image.convert("L")

plt.figure(figsize=(6,4))
plt.imshow(image_gray, cmap="gray")
plt.title("Black and White Cat (Grayscale)")
plt.show()
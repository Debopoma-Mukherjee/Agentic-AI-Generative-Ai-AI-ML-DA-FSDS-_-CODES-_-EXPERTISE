import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import requests
from io import BytesIO

def load_image_from_url(url):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    return img

sunflower_url="https://images.all-free-download.com/images/thumbjpg/sunflower_yellow_flowers_215332.jpg"
sunflower=load_image_from_url(sunflower_url).convert("RGB")
sunflower_np=np.array(sunflower)


R,G,B=sunflower_np[:,:,0],sunflower_np[:,:,1],sunflower_np[:,:,2]   

red_img=np.zeros_like(sunflower_np)
green_img=np.zeros_like(sunflower_np)
blue_img=np.zeros_like(sunflower_np)

red_img[:,:,0]=R
green_img[:,:,1]=G
blue_img[:,:,2]=B

plt.figure(figsize=(12,8))

plt.subplot(2,2,1)
plt.imshow(sunflower_np)
plt.title("Original Image")
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(red_img)
plt.title("Red Channel")
plt.axis('off')

plt.subplot(2,2,3)
plt.imshow(green_img)
plt.title("Green Channel")
plt.axis('off')

plt.subplot(2,2,4)
plt.imshow(blue_img)
plt.title("Blue Channel")
plt.axis('off')

plt.tight_layout()
plt.show()

sunflower_gray=sunflower.convert("L")
sunflower_gray_np=np.array(sunflower_gray)

plt.figure(figsize=(6,6))
plt.imshow(sunflower_gray_np, cmap='gray')
plt.title("Grayscale Image")
plt.axis('off')
plt.show()

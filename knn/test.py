from PIL import Image
import os

image_file=os.listdir(r'.\MNIST dataset\train-images')
print type(image_file[1])
for f in image_file:
	s='.\\MNIST dataset\\train-images\\'+f
	im=Image.open(s)
	
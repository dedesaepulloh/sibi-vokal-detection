from PIL import Image
from numpy import asarray

img = Image.open('images/train/J.a1058f74-bf84-11eb-bc19-3ca067262819.jpg')
numpydata = asarray(img)

print(numpydata)

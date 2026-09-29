from PIL import Image

img=Image.open("digit.png")
print("size of image:-",img.size)

img=img.convert("L")
img=img.resize((28,28))
img.save("digit_28X28.png")

print("resize:-",img.size)


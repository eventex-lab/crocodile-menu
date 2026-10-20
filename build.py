# Render build: crop the photos used by index.html.
# image.jpg = latest Beverage Promotions poster; food art comes from the public Drive copy.
import os, shutil, urllib.request
from PIL import Image
os.makedirs("public/img", exist_ok=True)
urllib.request.urlretrieve("https://drive.usercontent.google.com/download?id=1xy5n2A6BWnWqmm4HlSrT2vwEu0vm7qXJ&export=download&confirm=t", "food.png")
bev = Image.open("image.jpg").convert("RGB")
food = Image.open("food.png").convert("RGB")
s = bev.width / 1414
def save(im, box, name, w, scale=1):
    c = im.crop(tuple(int(v * scale) for v in box))
    c = c.resize((w, int(c.height * w / c.width)), Image.LANCZOS)
    c.save("public/img/%s.jpg" % name, quality=80, optimize=True, progressive=True)
save(food, (0, 790, 1024, 1460), "food", 900)
save(bev, (30, 470, 720, 1130), "party", 640, s)
save(bev, (810, 1030, 1200, 1545), "wine", 520, s)
save(bev, (0, 1545, 690, 1960), "beer", 640, s)
shutil.copy("index.html", "public/index.html")
print("built", os.listdir("public/img"))

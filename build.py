# Render build: fetch the original menu artwork and crop the photos used by index.html
import os, shutil, urllib.request
import pymupdf as fitz
from PIL import Image
SRC = {
    "bev.pdf": "1eeFGl7W0w8gwtx9ukVvJ4ZoNFzHsGu-R",
    "food.png": "1xy5n2A6BWnWqmm4HlSrT2vwEu0vm7qXJ",
}
os.makedirs("public/img", exist_ok=True)
for name, fid in SRC.items():
    url = "https://drive.usercontent.google.com/download?id=%s&export=download&confirm=t" % fid
    urllib.request.urlretrieve(url, name)
page = fitz.open("bev.pdf")[0]
z = 1655 / page.rect.width
page.get_pixmap(matrix=fitz.Matrix(z, z)).save("bev.png")
bev = Image.open("bev.png").convert("RGB")
food = Image.open("food.png").convert("RGB")
s = bev.width / 910
def save(im, box, name, w, scale=1):
    c = im.crop(tuple(int(v * scale) for v in box))
    c = c.resize((w, int(c.height * w / c.width)), Image.LANCZOS)
    c.save("public/img/%s.jpg" % name, quality=78, optimize=True, progressive=True)
save(food, (0, 790, 1024, 1460), "food", 900)
save(bev, (0, 330, 520, 730), "party", 640, s)
save(bev, (500, 650, 830, 1010), "wine", 520, s)
save(bev, (30, 1000, 470, 1287), "beer", 640, s)
shutil.copy("index.html", "public/index.html")
print("built", os.listdir("public/img"))

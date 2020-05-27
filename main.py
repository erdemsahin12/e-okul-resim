from PIL import Image
import os

for resim_adi in os.listdir("kaynak"):
    x = Image.open(f"kaynak/{resim_adi}")
    print("ilk boyut ", x.size)
    y = x.resize((133, 171))
    print("yeni boyut ", y.size)
    resim_adi = os.path.splitext(resim_adi)[0]
    y.save(f"hedef/{resim_adi}.png", "png")
    print("tamam")

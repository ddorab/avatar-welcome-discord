import numpy as np
from PIL import Image, ImageDraw

avatar = Image.open("img/2a68368c6fb9e11ab3069294038d8367.webp")
avatar_w, avatar_h = avatar.size

lum_img = Image.new('L', [avatar_h, avatar_w], 0)

draw = ImageDraw.Draw(lum_img)
draw.pieslice([(0, 0), (avatar_h, avatar_w)], 0, 360, fill=255, outline="white")

avatar_arr = np.array(avatar)
lum_img_arr = np.array(lum_img)
final_img_arr = np.dstack((avatar_arr, lum_img_arr))

img = (Image.fromarray(final_img_arr))

# img.show()

img_w, img_h = img.size
bg = Image.open("img/background.jpg")

bg_w, bg_h = bg.size

offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
bg.paste(img, offset, img)
bg.save("result.png")
result = Image.open("result.png")
result.show()

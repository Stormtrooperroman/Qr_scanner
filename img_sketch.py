from PIL import Image
im = Image.open("vid.gif")

w, h = im.size

cut = (0, 496, w, h-573)
new_h = (h-496-573)
new_image = Image.new('RGB',(w, im.n_frames*new_h), (250,250,250))
for i in range(0, im.n_frames):
    im.seek(i)
    img=im.crop(cut)
    new_image.paste(img,(0,new_h*i))




new_image.save(f"final.png")


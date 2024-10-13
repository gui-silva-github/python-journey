from PIL import Image

img = Image.open(r"a imagem a ser aberta")

mirror.img = img.transpose(Image.FLIP_LEFT_RIGHT)
mirror.img.save('mirror_image.png')
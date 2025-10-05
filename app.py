from PIL import Image, ImageOps, ImageFilter

#Add the input image path 
input_path = ""      
#Add the output image path           
output_path = "black_white.png"
DPI = 300                         
CM = 10                           

inches = CM / 2.54
pixels = round(inches * DPI)

image = Image.open(input_path).convert("RGBA")
background = Image.new("RGBA", image.size, "WHITE")
image = Image.alpha_composite(background, image).convert("L")

#Boost contrast
image = ImageOps.autocontrast(image, cutoff=0)

#Added blur to smooth edges
image = image.filter(ImageFilter.GaussianBlur(radius=1))

threshold = 150  
black_white_img = image.point(lambda p: 0 if p < threshold else 255, mode="1")

canvas = Image.new("1", (pixels, pixels), 1)  
black_white_img.thumbnail((pixels, pixels), Image.NEAREST)
offset_x = (pixels - black_white_img.width) // 2
offset_y = (pixels - black_white_img.height) // 2
canvas.paste(black_white_img, (offset_x, offset_y))

canvas.convert("L").save(output_path, dpi=(DPI, DPI))
print("Saved:", output_path)



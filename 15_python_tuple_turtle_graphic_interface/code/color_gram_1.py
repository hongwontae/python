from colorgram import extract

arr_color = []
colors = extract('image.jpg', 30)

for color in colors :
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_rgb_color = (r,g,b)
    arr_color.append(new_rgb_color)

print(arr_color)


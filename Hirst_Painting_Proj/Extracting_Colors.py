import colorgram

rgb_colors = [] #creating an empty list for the future for loop
colors = colorgram.extract('image.jpg', 30) #Remember that the reference file must be in the same file level as the program using this notation

for color in colors: #for loop to create tuples of the colors in the image
    r = color.rgb.r #method to extract the r part of the rgb color of each color
    g = color.rgb.g #method to extract the g part of the rgb color of each color
    b = color.rgb.b #method to extract the b part of the rgb color of each color
    new_color = (r , g, b) #creates a tuple of the new colors
    rgb_colors.append(new_color) #appends the rgb values of the colors to a list

print(rgb_colors)
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import argparse


# USE: Run this file in terminal with the arguments found in the parser below
#  INPUT -> Image filepath, Output filepath, Ascii character palate, Output width in characters, Exposure, Contrast, Color (Black/White)
# OUTPUT -> .txt file

def char_brightness(pix_val, weight):
    brightness_arr = []
    brightness_arr.append(sum(sum(pix_val[:7]))/126)  # top_M
    brightness_arr.append(sum(sum(pix_val[:, :5]))/110)   # MID L
    brightness_arr.append(sum(sum(pix_val[6:16, 5:13]))/80)  # MID M
    brightness_arr.append(sum(sum(pix_val[:, 13:]))/110)   # MID R
    brightness_arr.append(sum(sum(pix_val[15:]))/126)  # BOT M
    brightness_arr += weight*[sum(sum(pix_val))/(22*18)]
    return brightness_arr


def char_palate(arr,weight=4, color=1):
    brightness = []
    font = ImageFont.truetype('/Users/greysonbrothers/Desktop/ /- python/art/fonts/Menlo-Regular.ttf',size=30)
    for char in arr:
        img = Image.new(mode='1', size=(18, 22), color=(color))
        d = ImageDraw.Draw(img)
        d.text((0, -6), char, fill=(1-color), font=font)
        pix_val = np.asarray(img)
        brightness.append(char_brightness(pix_val, weight))
    return dict(zip(arr,brightness))


def char_map(local_pixels, chars):
    mn = float('inf')
    letter = ''
    for key in chars:
        current = minkowski_dist(local_pixels,chars[key])
        if current < mn:
            mn = current
            letter = key
    return letter


def minkowski_dist(v1,v2, p=1):
    dist = []
    for i in range(len(v1)):
        dist.append(pow(np.abs(v1[i]-v2[i]),p))
    return sum(dist)**(1/p)


def get_neighbors(arr,x,y,weight=4):
    nb = [arr[x-1, y], arr[x, y-2],   arr[x, y],   arr[x, y+2], arr[x+1, y]]
    nb += weight*[arr[x, y]]
    return(nb)


def load_image(path, w=100):
    image = Image.open(path)
    width, height = image.size
    image = image.convert('L') # convert the image to monochrome
    k = image.size[0]/w  # /400
    image = image.resize((int(width/k)*2, int(height/k)))
    return image


def convert_image(input_path, output_path, palate, w=100, weight=4, exposure=0.5, color='b'):
    c = 1 if color == 'b' else 0
    e = exposure if color == 'b' else 1/exposure
    img = load_image(input_path, w)
    pix_val = (np.asarray(img)/255)**e
    chars = char_palate(palate, weight=weight, color=c)

    current_line = ''
    ascii_text = open(output_path, 'w')
    for x in range(2,img.size[1]-2):
        for y in range(2,img.size[0]-2):
            local_pixels = get_neighbors(pix_val,x,y, weight)
            current_char = char_map(local_pixels, chars)
            current_line += current_char
            print(current_char, end='', flush=True)
        ascii_text.write(current_line + '\n')
        print()
        current_line = ''
    ascii_text.close()


if __name__ == "__main__":

    char = [' ','.',"'",'-','\'',',','_',':','=','^','"','+','•','~',';','|','(',')','<','>','%','?','c','s','{','}','!','I','[',']','i','t','v','x','z','1','r','a','e','l','o','n','u','T','f','w','3','7','J','y','5','$','4','g','k','p','q','F','P','b','d','h','G','O','V','X','E','Z','8','A','U','D','H','K','W','&','@','R','B','Q','#','0','M','N']

    parser = argparse.ArgumentParser(description='Cleaning audio data')
    parser.add_argument('--input_path', '-i', type=str, default='images/obama.jpg',
                        help='Filepath for the desired image')
    parser.add_argument('--output_path', '-o', type=str, default='images/obama.jpg',
                        help='Filepath for the desired image')
    parser.add_argument('--palate', '-p', type=list, default=char,
                        help='Characters to build the image from, should be a python list')
    parser.add_argument('--width', '-w',type=int, default=100,
                        help='Number of characters to scale the width/resolution to')
    parser.add_argument('--exposure', '-e', type=float, default=0.50,
                        help='How much exposure is added (default 0.50), the closer to zero the brighter the image')
    parser.add_argument('--contrast', '-con', type=int, default=15,
                        help='How much individual pixels are weighted, default 15')
    parser.add_argument('--color', '-c', type=str, default='b',
                        help='Color the characters w (white) or b (black)')
    args, _ = parser.parse_known_args()

    convert_image(args.input_path, args.output_path, palate=args.palate, w=args.width, weight=args.contrast, exposure=args.exposure, color=args.color)

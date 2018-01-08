from tkinter import *

C64_CHARACTERS = [
    [60, 102, 118, 118, 6, 70, 60, 0],
    [24, 60, 102, 126, 102, 102, 102, 0],
    [62, 102, 102, 62, 102, 102, 62, 0],
    [60, 102, 6, 6, 6, 102, 60, 0],
    [30, 54, 102, 102, 102, 54, 30, 0],
    [126, 6, 6, 30, 6, 6, 126, 0],
    [126, 6, 6, 30, 6, 6, 6, 0],
    [60, 102, 6, 118, 102, 102, 60, 0],
    [102, 102, 102, 126, 102, 102, 102, 0],
    [60, 24, 24, 24, 24, 24, 60, 0],
    [120, 48, 48, 48, 48, 54, 28, 0],
    [102, 54, 30, 14, 30, 54, 102, 0],
    [6, 6, 6, 6, 6, 6, 126, 0],
    [198, 238, 254, 214, 198, 198, 198, 0],
    [102, 110, 126, 126, 118, 102, 102, 0],
    [60, 102, 102, 102, 102, 102, 60, 0],
    [62, 102, 102, 62, 6, 6, 6, 0],
    [60, 102, 102, 102, 102, 60, 112, 0],
    [62, 102, 102, 62, 30, 54, 102, 0],
    [60, 102, 6, 60, 96, 102, 60, 0],
    [126, 24, 24, 24, 24, 24, 24, 0],
    [102, 102, 102, 102, 102, 102, 60, 0],
    [102, 102, 102, 102, 102, 60, 24, 0],
    [198, 198, 198, 214, 254, 238, 198, 0],
    [102, 102, 60, 24, 60, 102, 102, 0],
    [102, 102, 102, 60, 24, 24, 24, 0],
    [126, 96, 48, 24, 12, 6, 126, 0],
    [60, 12, 12, 12, 12, 12, 60, 0],
    [48, 72, 12, 62, 12, 70, 63, 0],
    [60, 48, 48, 48, 48, 48, 60, 0],
    [0, 24, 60, 126, 24, 24, 24, 24],
    [0, 8, 12, 254, 254, 12, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [24, 24, 24, 24, 0, 0, 24, 0],
    [102, 102, 102, 0, 0, 0, 0, 0],
    [102, 102, 255, 102, 255, 102, 102, 0],
    [24, 124, 6, 60, 96, 62, 24, 0],
    [70, 102, 48, 24, 12, 102, 98, 0],
    [60, 102, 60, 28, 230, 102, 252, 0],
    [96, 48, 24, 0, 0, 0, 0, 0],
    [48, 24, 12, 12, 12, 24, 48, 0],
    [12, 24, 48, 48, 48, 24, 12, 0],
    [0, 102, 60, 255, 60, 102, 0, 0],
    [0, 24, 24, 126, 24, 24, 0, 0],
    [0, 0, 0, 0, 0, 24, 24, 12],
    [0, 0, 0, 126, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 24, 24, 0],
    [0, 192, 96, 48, 24, 12, 6, 0],
    [60, 102, 118, 110, 102, 102, 60, 0],
    [24, 24, 28, 24, 24, 24, 126, 0],
    [60, 102, 96, 48, 12, 6, 126, 0],
    [60, 102, 96, 56, 96, 102, 60, 0],
    [96, 112, 120, 102, 254, 96, 96, 0],
    [126, 6, 62, 96, 96, 102, 60, 0],
    [60, 102, 6, 62, 102, 102, 60, 0],
    [126, 102, 48, 24, 24, 24, 24, 0],
    [60, 102, 102, 60, 102, 102, 60, 0],
    [60, 102, 102, 124, 96, 102, 60, 0],
    [0, 0, 24, 0, 0, 24, 0, 0],
    [0, 0, 24, 0, 0, 24, 24, 12],
    [112, 24, 12, 6, 12, 24, 112, 0],
    [0, 0, 126, 0, 126, 0, 0, 0],
    [14, 24, 48, 96, 48, 24, 14, 0],
    [60, 102, 96, 48, 24, 0, 24, 0],
    [0, 0, 0, 255, 255, 0, 0, 0],
    [16, 56, 124, 254, 254, 56, 124, 0],
    [24, 24, 24, 24, 24, 24, 24, 24],
    [0, 0, 0, 255, 255, 0, 0, 0],
    [0, 0, 255, 255, 0, 0, 0, 0],
    [0, 255, 255, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 255, 255, 0, 0],
    [12, 12, 12, 12, 12, 12, 12, 12],
    [48, 48, 48, 48, 48, 48, 48, 48],
    [0, 0, 0, 7, 15, 28, 24, 24],
    [24, 24, 56, 240, 224, 0, 0, 0],
    [24, 24, 28, 15, 7, 0, 0, 0],
    [3, 3, 3, 3, 3, 3, 255, 255],
    [3, 7, 14, 28, 56, 112, 224, 192],
    [192, 224, 112, 56, 28, 14, 7, 3],
    [255, 255, 3, 3, 3, 3, 3, 3],
    [255, 255, 192, 192, 192, 192, 192, 192],
    [0, 60, 126, 126, 126, 126, 60, 0],
    [0, 0, 0, 0, 0, 255, 255, 0],
    [108, 254, 254, 254, 124, 56, 16, 0],
    [6, 6, 6, 6, 6, 6, 6, 6],
    [0, 0, 0, 224, 240, 56, 24, 24],
    [195, 231, 126, 60, 60, 126, 231, 195],
    [0, 60, 126, 102, 102, 126, 60, 0],
    [24, 24, 102, 102, 24, 24, 60, 0],
    [96, 96, 96, 96, 96, 96, 96, 96],
    [16, 56, 124, 254, 124, 56, 16, 0],
    [24, 24, 24, 255, 255, 24, 24, 24],
    [3, 3, 12, 12, 3, 3, 12, 12],
    [24, 24, 24, 24, 24, 24, 24, 24],
    [0, 0, 192, 124, 110, 108, 108, 0],
    [255, 254, 252, 248, 240, 224, 192, 128],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [15, 15, 15, 15, 15, 15, 15, 15],
    [0, 0, 0, 0, 255, 255, 255, 255],
    [255, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 255],
    [3, 3, 3, 3, 3, 3, 3, 3],
    [51, 51, 204, 204, 51, 51, 204, 204],
    [192, 192, 192, 192, 192, 192, 192, 192],
    [0, 0, 0, 0, 51, 51, 204, 204],
    [255, 127, 63, 31, 15, 7, 3, 1],
    [192, 192, 192, 192, 192, 192, 192, 192],
    [24, 24, 24, 248, 248, 24, 24, 24],
    [0, 0, 0, 0, 240, 240, 240, 240],
    [24, 24, 24, 248, 248, 0, 0, 0],
    [0, 0, 0, 31, 31, 24, 24, 24],
    [0, 0, 0, 0, 0, 0, 255, 255],
    [0, 0, 0, 248, 248, 24, 24, 24],
    [24, 24, 24, 255, 255, 0, 0, 0],
    [0, 0, 0, 255, 255, 24, 24, 24],
    [24, 24, 24, 31, 31, 24, 24, 24],
    [3, 3, 3, 3, 3, 3, 3, 3],
    [7, 7, 7, 7, 7, 7, 7, 7],
    [224, 224, 224, 224, 224, 224, 224, 224],
    [255, 255, 0, 0, 0, 0, 0, 0],
    [255, 255, 255, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 255, 255, 255],
    [192, 192, 192, 192, 192, 192, 255, 255],
    [0, 0, 0, 0, 15, 15, 15, 15],
    [240, 240, 240, 240, 0, 0, 0, 0],
    [24, 24, 24, 31, 31, 0, 0, 0],
    [15, 15, 15, 15, 0, 0, 0, 0],
    [15, 15, 15, 15, 240, 240, 240, 240],
    [195, 153, 137, 137, 249, 153, 195, 255],
    [231, 195, 153, 129, 153, 153, 153, 255],
    [193, 153, 153, 193, 153, 153, 193, 255],
    [195, 153, 249, 249, 249, 153, 195, 255],
    [225, 201, 153, 153, 153, 201, 225, 255],
    [129, 249, 249, 225, 249, 249, 129, 255],
    [129, 249, 249, 225, 249, 249, 249, 255],
    [195, 153, 249, 137, 153, 153, 195, 255],
    [153, 153, 153, 129, 153, 153, 153, 255],
    [195, 231, 231, 231, 231, 231, 195, 255],
    [135, 207, 207, 207, 207, 201, 227, 255],
    [153, 201, 225, 241, 225, 201, 153, 255],
    [249, 249, 249, 249, 249, 249, 129, 255],
    [57, 17, 1, 41, 57, 57, 57, 255],
    [153, 145, 129, 129, 137, 153, 153, 255],
    [195, 153, 153, 153, 153, 153, 195, 255],
    [193, 153, 153, 193, 249, 249, 249, 255],
    [195, 153, 153, 153, 153, 195, 143, 255],
    [193, 153, 153, 193, 225, 201, 153, 255],
    [195, 153, 249, 195, 159, 153, 195, 255],
    [129, 231, 231, 231, 231, 231, 231, 255],
    [153, 153, 153, 153, 153, 153, 195, 255],
    [153, 153, 153, 153, 153, 195, 231, 255],
    [57, 57, 57, 41, 1, 17, 57, 255],
    [153, 153, 195, 231, 195, 153, 153, 255],
    [153, 153, 153, 195, 231, 231, 231, 255],
    [129, 159, 207, 231, 243, 249, 129, 255],
    [195, 243, 243, 243, 243, 243, 195, 255],
    [207, 183, 243, 193, 243, 185, 192, 255],
    [195, 207, 207, 207, 207, 207, 195, 255],
    [255, 231, 195, 129, 231, 231, 231, 231],
    [255, 247, 243, 1, 1, 243, 247, 255],
    [255, 255, 255, 255, 255, 255, 255, 255],
    [231, 231, 231, 231, 255, 255, 231, 255],
    [153, 153, 153, 255, 255, 255, 255, 255],
    [153, 153, 0, 153, 0, 153, 153, 255],
    [231, 131, 249, 195, 159, 193, 231, 255],
    [185, 153, 207, 231, 243, 153, 157, 255],
    [195, 153, 195, 227, 25, 153, 3, 255],
    [159, 207, 231, 255, 255, 255, 255, 255],
    [207, 231, 243, 243, 243, 231, 207, 255],
    [243, 231, 207, 207, 207, 231, 243, 255],
    [255, 153, 195, 0, 195, 153, 255, 255],
    [255, 231, 231, 129, 231, 231, 255, 255],
    [255, 255, 255, 255, 255, 231, 231, 243],
    [255, 255, 255, 129, 255, 255, 255, 255],
    [255, 255, 255, 255, 255, 231, 231, 255],
    [255, 63, 159, 207, 231, 243, 249, 255],
    [195, 153, 137, 145, 153, 153, 195, 255],
    [231, 231, 227, 231, 231, 231, 129, 255],
    [195, 153, 159, 207, 243, 249, 129, 255],
    [195, 153, 159, 199, 159, 153, 195, 255],
    [159, 143, 135, 153, 1, 159, 159, 255],
    [129, 249, 193, 159, 159, 153, 195, 255],
    [195, 153, 249, 193, 153, 153, 195, 255],
    [129, 153, 207, 231, 231, 231, 231, 255],
    [195, 153, 153, 195, 153, 153, 195, 255],
    [195, 153, 153, 131, 159, 153, 195, 255],
    [255, 255, 231, 255, 255, 231, 255, 255],
    [255, 255, 231, 255, 255, 231, 231, 243],
    [143, 231, 243, 249, 243, 231, 143, 255],
    [255, 255, 129, 255, 129, 255, 255, 255],
    [241, 231, 207, 159, 207, 231, 241, 255],
    [195, 153, 159, 207, 231, 255, 231, 255],
    [255, 255, 255, 0, 0, 255, 255, 255],
    [239, 199, 131, 1, 1, 199, 131, 255],
    [231, 231, 231, 231, 231, 231, 231, 231],
    [255, 255, 255, 0, 0, 255, 255, 255],
    [255, 255, 0, 0, 255, 255, 255, 255],
    [255, 0, 0, 255, 255, 255, 255, 255],
    [255, 255, 255, 255, 0, 0, 255, 255],
    [243, 243, 243, 243, 243, 243, 243, 243],
    [207, 207, 207, 207, 207, 207, 207, 207],
    [255, 255, 255, 248, 240, 227, 231, 231],
    [231, 231, 199, 15, 31, 255, 255, 255],
    [231, 231, 227, 240, 248, 255, 255, 255],
    [252, 252, 252, 252, 252, 252, 0, 0],
    [252, 248, 241, 227, 199, 143, 31, 63],
    [63, 31, 143, 199, 227, 241, 248, 252],
    [0, 0, 252, 252, 252, 252, 252, 252],
    [0, 0, 63, 63, 63, 63, 63, 63],
    [255, 195, 129, 129, 129, 129, 195, 255],
    [255, 255, 255, 255, 255, 0, 0, 255],
    [147, 1, 1, 1, 131, 199, 239, 255],
    [249, 249, 249, 249, 249, 249, 249, 249],
    [255, 255, 255, 31, 15, 199, 231, 231],
    [60, 24, 129, 195, 195, 129, 24, 60],
    [255, 195, 129, 153, 153, 129, 195, 255],
    [231, 231, 153, 153, 231, 231, 195, 255],
    [159, 159, 159, 159, 159, 159, 159, 159],
    [239, 199, 131, 1, 131, 199, 239, 255],
    [231, 231, 231, 0, 0, 231, 231, 231],
    [252, 252, 243, 243, 252, 252, 243, 243],
    [231, 231, 231, 231, 231, 231, 231, 231],
    [255, 255, 63, 131, 145, 147, 147, 255],
    [0, 1, 3, 7, 15, 31, 63, 127],
    [255, 255, 255, 255, 255, 255, 255, 255],
    [240, 240, 240, 240, 240, 240, 240, 240],
    [255, 255, 255, 255, 0, 0, 0, 0],
    [0, 255, 255, 255, 255, 255, 255, 255],
    [255, 255, 255, 255, 255, 255, 255, 0],
    [252, 252, 252, 252, 252, 252, 252, 252],
    [204, 204, 51, 51, 204, 204, 51, 51],
    [63, 63, 63, 63, 63, 63, 63, 63],
    [255, 255, 255, 255, 204, 204, 51, 51],
    [0, 128, 192, 224, 240, 248, 252, 254],
    [63, 63, 63, 63, 63, 63, 63, 63],
    [231, 231, 231, 7, 7, 231, 231, 231],
    [255, 255, 255, 255, 15, 15, 15, 15],
    [231, 231, 231, 7, 7, 255, 255, 255],
    [255, 255, 255, 224, 224, 231, 231, 231],
    [255, 255, 255, 255, 255, 255, 0, 0],
    [255, 255, 255, 7, 7, 231, 231, 231],
    [231, 231, 231, 0, 0, 255, 255, 255],
    [255, 255, 255, 0, 0, 231, 231, 231],
    [231, 231, 231, 224, 224, 231, 231, 231],
    [252, 252, 252, 252, 252, 252, 252, 252],
    [248, 248, 248, 248, 248, 248, 248, 248],
    [31, 31, 31, 31, 31, 31, 31, 31],
    [0, 0, 255, 255, 255, 255, 255, 255],
    [0, 0, 0, 255, 255, 255, 255, 255],
    [255, 255, 255, 255, 255, 0, 0, 0],
    [63, 63, 63, 63, 63, 63, 0, 0],
    [255, 255, 255, 255, 240, 240, 240, 240],
    [15, 15, 15, 15, 255, 255, 255, 255],
    [231, 231, 231, 224, 224, 255, 255, 255],
    [240, 240, 240, 240, 255, 255, 255, 255],
    [240, 240, 240, 240, 15, 15, 15, 15],
    [60, 102, 118, 118, 6, 70, 60, 0],
    [0, 0, 60, 96, 124, 102, 124, 0],
    [0, 6, 6, 62, 102, 102, 62, 0],
    [0, 0, 60, 6, 6, 6, 60, 0],
    [0, 96, 96, 124, 102, 102, 124, 0],
    [0, 0, 60, 102, 126, 6, 60, 0],
    [0, 112, 24, 124, 24, 24, 24, 0],
    [0, 0, 124, 102, 102, 124, 96, 62],
    [0, 6, 6, 62, 102, 102, 102, 0],
    [0, 24, 0, 28, 24, 24, 60, 0],
    [0, 96, 0, 96, 96, 96, 96, 60],
    [0, 6, 6, 54, 30, 54, 102, 0],
    [0, 28, 24, 24, 24, 24, 60, 0],
    [0, 0, 102, 254, 254, 214, 198, 0],
    [0, 0, 62, 102, 102, 102, 102, 0],
    [0, 0, 60, 102, 102, 102, 60, 0],
    [0, 0, 62, 102, 102, 62, 6, 6],
    [0, 0, 124, 102, 102, 124, 96, 96],
    [0, 0, 62, 102, 6, 6, 6, 0],
    [0, 0, 124, 6, 60, 96, 62, 0],
    [0, 24, 126, 24, 24, 24, 112, 0],
    [0, 0, 102, 102, 102, 102, 124, 0],
    [0, 0, 102, 102, 102, 60, 24, 0],
    [0, 0, 198, 214, 254, 124, 108, 0],
    [0, 0, 102, 60, 24, 60, 102, 0],
    [0, 0, 102, 102, 102, 124, 48, 30],
    [0, 0, 126, 48, 24, 12, 126, 0],
    [60, 12, 12, 12, 12, 12, 60, 0],
    [48, 72, 12, 62, 12, 70, 63, 0],
    [60, 48, 48, 48, 48, 48, 60, 0],
    [0, 24, 60, 126, 24, 24, 24, 24],
    [0, 8, 12, 254, 254, 12, 8, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [24, 24, 24, 24, 0, 0, 24, 0],
    [102, 102, 102, 0, 0, 0, 0, 0],
    [102, 102, 255, 102, 255, 102, 102, 0],
    [24, 124, 6, 60, 96, 62, 24, 0],
    [70, 102, 48, 24, 12, 102, 98, 0],
    [60, 102, 60, 28, 230, 102, 252, 0],
    [96, 48, 24, 0, 0, 0, 0, 0],
    [48, 24, 12, 12, 12, 24, 48, 0],
    [12, 24, 48, 48, 48, 24, 12, 0],
    [0, 102, 60, 255, 60, 102, 0, 0],
    [0, 24, 24, 126, 24, 24, 0, 0],
    [0, 0, 0, 0, 0, 24, 24, 12],
    [0, 0, 0, 126, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 24, 24, 0],
    [0, 192, 96, 48, 24, 12, 6, 0],
    [60, 102, 118, 110, 102, 102, 60, 0],
    [24, 24, 28, 24, 24, 24, 126, 0],
    [60, 102, 96, 48, 12, 6, 126, 0],
    [60, 102, 96, 56, 96, 102, 60, 0],
    [96, 112, 120, 102, 254, 96, 96, 0],
    [126, 6, 62, 96, 96, 102, 60, 0],
    [60, 102, 6, 62, 102, 102, 60, 0],
    [126, 102, 48, 24, 24, 24, 24, 0],
    [60, 102, 102, 60, 102, 102, 60, 0],
    [60, 102, 102, 124, 96, 102, 60, 0],
    [0, 0, 24, 0, 0, 24, 0, 0],
    [0, 0, 24, 0, 0, 24, 24, 12],
    [112, 24, 12, 6, 12, 24, 112, 0],
    [0, 0, 126, 0, 126, 0, 0, 0],
    [14, 24, 48, 96, 48, 24, 14, 0],
    [60, 102, 96, 48, 24, 0, 24, 0],
    [0, 0, 0, 255, 255, 0, 0, 0],
    [24, 60, 102, 126, 102, 102, 102, 0],
    [62, 102, 102, 62, 102, 102, 62, 0],
    [60, 102, 6, 6, 6, 102, 60, 0],
    [30, 54, 102, 102, 102, 54, 30, 0],
    [126, 6, 6, 30, 6, 6, 126, 0],
    [126, 6, 6, 30, 6, 6, 6, 0],
    [60, 102, 6, 118, 102, 102, 60, 0],
    [102, 102, 102, 126, 102, 102, 102, 0],
    [60, 24, 24, 24, 24, 24, 60, 0],
    [120, 48, 48, 48, 48, 54, 28, 0],
    [102, 54, 30, 14, 30, 54, 102, 0],
    [6, 6, 6, 6, 6, 6, 126, 0],
    [198, 238, 254, 214, 198, 198, 198, 0],
    [102, 110, 126, 126, 118, 102, 102, 0],
    [60, 102, 102, 102, 102, 102, 60, 0],
    [62, 102, 102, 62, 6, 6, 6, 0],
    [60, 102, 102, 102, 102, 60, 112, 0],
    [62, 102, 102, 62, 30, 54, 102, 0],
    [60, 102, 6, 60, 96, 102, 60, 0],
    [126, 24, 24, 24, 24, 24, 24, 0],
    [102, 102, 102, 102, 102, 102, 60, 0],
    [102, 102, 102, 102, 102, 60, 24, 0],
    [198, 198, 198, 214, 254, 238, 198, 0],
    [102, 102, 60, 24, 60, 102, 102, 0],
    [102, 102, 102, 60, 24, 24, 24, 0],
    [126, 96, 48, 24, 12, 6, 126, 0],
    [24, 24, 24, 255, 255, 24, 24, 24],
    [3, 3, 12, 12, 3, 3, 12, 12],
    [24, 24, 24, 24, 24, 24, 24, 24],
    [204, 204, 51, 51, 204, 204, 51, 51],
    [204, 153, 51, 102, 204, 153, 51, 102],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [15, 15, 15, 15, 15, 15, 15, 15],
    [0, 0, 0, 0, 255, 255, 255, 255],
    [255, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 255],
    [3, 3, 3, 3, 3, 3, 3, 3],
    [51, 51, 204, 204, 51, 51, 204, 204],
    [192, 192, 192, 192, 192, 192, 192, 192],
    [0, 0, 0, 0, 51, 51, 204, 204],
    [51, 153, 204, 102, 51, 153, 204, 102],
    [192, 192, 192, 192, 192, 192, 192, 192],
    [24, 24, 24, 248, 248, 24, 24, 24],
    [0, 0, 0, 0, 240, 240, 240, 240],
    [24, 24, 24, 248, 248, 0, 0, 0],
    [0, 0, 0, 31, 31, 24, 24, 24],
    [0, 0, 0, 0, 0, 0, 255, 255],
    [0, 0, 0, 248, 248, 24, 24, 24],
    [24, 24, 24, 255, 255, 0, 0, 0],
    [0, 0, 0, 255, 255, 24, 24, 24],
    [24, 24, 24, 31, 31, 24, 24, 24],
    [3, 3, 3, 3, 3, 3, 3, 3],
    [7, 7, 7, 7, 7, 7, 7, 7],
    [224, 224, 224, 224, 224, 224, 224, 224],
    [255, 255, 0, 0, 0, 0, 0, 0],
    [255, 255, 255, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 255, 255, 255],
    [128, 192, 96, 54, 30, 14, 6, 0],
    [0, 0, 0, 0, 15, 15, 15, 15],
    [240, 240, 240, 240, 0, 0, 0, 0],
    [24, 24, 24, 31, 31, 0, 0, 0],
    [15, 15, 15, 15, 0, 0, 0, 0],
    [15, 15, 15, 15, 240, 240, 240, 240],
    [195, 153, 137, 137, 249, 153, 195, 255],
    [255, 255, 195, 159, 131, 153, 131, 255],
    [255, 249, 249, 193, 153, 153, 193, 255],
    [255, 255, 195, 249, 249, 249, 195, 255],
    [255, 159, 159, 131, 153, 153, 131, 255],
    [255, 255, 195, 153, 129, 249, 195, 255],
    [255, 143, 231, 131, 231, 231, 231, 255],
    [255, 255, 131, 153, 153, 131, 159, 193],
    [255, 249, 249, 193, 153, 153, 153, 255],
    [255, 231, 255, 227, 231, 231, 195, 255],
    [255, 159, 255, 159, 159, 159, 159, 195],
    [255, 249, 249, 201, 225, 201, 153, 255],
    [255, 227, 231, 231, 231, 231, 195, 255],
    [255, 255, 153, 1, 1, 41, 57, 255],
    [255, 255, 193, 153, 153, 153, 153, 255],
    [255, 255, 195, 153, 153, 153, 195, 255],
    [255, 255, 193, 153, 153, 193, 249, 249],
    [255, 255, 131, 153, 153, 131, 159, 159],
    [255, 255, 193, 153, 249, 249, 249, 255],
    [255, 255, 131, 249, 195, 159, 193, 255],
    [255, 231, 129, 231, 231, 231, 143, 255],
    [255, 255, 153, 153, 153, 153, 131, 255],
    [255, 255, 153, 153, 153, 195, 231, 255],
    [255, 255, 57, 41, 1, 131, 147, 255],
    [255, 255, 153, 195, 231, 195, 153, 255],
    [255, 255, 153, 153, 153, 131, 207, 225],
    [255, 255, 129, 207, 231, 243, 129, 255],
    [195, 243, 243, 243, 243, 243, 195, 255],
    [207, 183, 243, 193, 243, 185, 192, 255],
    [195, 207, 207, 207, 207, 207, 195, 255],
    [255, 231, 195, 129, 231, 231, 231, 231],
    [255, 247, 243, 1, 1, 243, 247, 255],
    [255, 255, 255, 255, 255, 255, 255, 255],
    [231, 231, 231, 231, 255, 255, 231, 255],
    [153, 153, 153, 255, 255, 255, 255, 255],
    [153, 153, 0, 153, 0, 153, 153, 255],
    [231, 131, 249, 195, 159, 193, 231, 255],
    [185, 153, 207, 231, 243, 153, 157, 255],
    [195, 153, 195, 227, 25, 153, 3, 255],
    [159, 207, 231, 255, 255, 255, 255, 255],
    [207, 231, 243, 243, 243, 231, 207, 255],
    [243, 231, 207, 207, 207, 231, 243, 255],
    [255, 153, 195, 0, 195, 153, 255, 255],
    [255, 231, 231, 129, 231, 231, 255, 255],
    [255, 255, 255, 255, 255, 231, 231, 243],
    [255, 255, 255, 129, 255, 255, 255, 255],
    [255, 255, 255, 255, 255, 231, 231, 255],
    [255, 63, 159, 207, 231, 243, 249, 255],
    [195, 153, 137, 145, 153, 153, 195, 255],
    [231, 231, 227, 231, 231, 231, 129, 255],
    [195, 153, 159, 207, 243, 249, 129, 255],
    [195, 153, 159, 199, 159, 153, 195, 255],
    [159, 143, 135, 153, 1, 159, 159, 255],
    [129, 249, 193, 159, 159, 153, 195, 255],
    [195, 153, 249, 193, 153, 153, 195, 255],
    [129, 153, 207, 231, 231, 231, 231, 255],
    [195, 153, 153, 195, 153, 153, 195, 255],
    [195, 153, 153, 131, 159, 153, 195, 255],
    [255, 255, 231, 255, 255, 231, 255, 255],
    [255, 255, 231, 255, 255, 231, 231, 243],
    [143, 231, 243, 249, 243, 231, 143, 255],
    [255, 255, 129, 255, 129, 255, 255, 255],
    [241, 231, 207, 159, 207, 231, 241, 255],
    [195, 153, 159, 207, 231, 255, 231, 255],
    [255, 255, 255, 0, 0, 255, 255, 255],
    [231, 195, 153, 129, 153, 153, 153, 255],
    [193, 153, 153, 193, 153, 153, 193, 255],
    [195, 153, 249, 249, 249, 153, 195, 255],
    [225, 201, 153, 153, 153, 201, 225, 255],
    [129, 249, 249, 225, 249, 249, 129, 255],
    [129, 249, 249, 225, 249, 249, 249, 255],
    [195, 153, 249, 137, 153, 153, 195, 255],
    [153, 153, 153, 129, 153, 153, 153, 255],
    [195, 231, 231, 231, 231, 231, 195, 255],
    [135, 207, 207, 207, 207, 201, 227, 255],
    [153, 201, 225, 241, 225, 201, 153, 255],
    [249, 249, 249, 249, 249, 249, 129, 255],
    [57, 17, 1, 41, 57, 57, 57, 255],
    [153, 145, 129, 129, 137, 153, 153, 255],
    [195, 153, 153, 153, 153, 153, 195, 255],
    [193, 153, 153, 193, 249, 249, 249, 255],
    [195, 153, 153, 153, 153, 195, 143, 255],
    [193, 153, 153, 193, 225, 201, 153, 255],
    [195, 153, 249, 195, 159, 153, 195, 255],
    [129, 231, 231, 231, 231, 231, 231, 255],
    [153, 153, 153, 153, 153, 153, 195, 255],
    [153, 153, 153, 153, 153, 195, 231, 255],
    [57, 57, 57, 41, 1, 17, 57, 255],
    [153, 153, 195, 231, 195, 153, 153, 255],
    [153, 153, 153, 195, 231, 231, 231, 255],
    [129, 159, 207, 231, 243, 249, 129, 255],
    [231, 231, 231, 0, 0, 231, 231, 231],
    [252, 252, 243, 243, 252, 252, 243, 243],
    [231, 231, 231, 231, 231, 231, 231, 231],
    [51, 51, 204, 204, 51, 51, 204, 204],
    [51, 102, 204, 153, 51, 102, 204, 153],
    [255, 255, 255, 255, 255, 255, 255, 255],
    [240, 240, 240, 240, 240, 240, 240, 240],
    [255, 255, 255, 255, 0, 0, 0, 0],
    [0, 255, 255, 255, 255, 255, 255, 255],
    [255, 255, 255, 255, 255, 255, 255, 0],
    [252, 252, 252, 252, 252, 252, 252, 252],
    [204, 204, 51, 51, 204, 204, 51, 51],
    [63, 63, 63, 63, 63, 63, 63, 63],
    [255, 255, 255, 255, 204, 204, 51, 51],
    [204, 102, 51, 153, 204, 102, 51, 153],
    [63, 63, 63, 63, 63, 63, 63, 63],
    [231, 231, 231, 7, 7, 231, 231, 231],
    [255, 255, 255, 255, 15, 15, 15, 15],
    [231, 231, 231, 7, 7, 255, 255, 255],
    [255, 255, 255, 224, 224, 231, 231, 231],
    [255, 255, 255, 255, 255, 255, 0, 0],
    [255, 255, 255, 7, 7, 231, 231, 231],
    [231, 231, 231, 0, 0, 255, 255, 255],
    [255, 255, 255, 0, 0, 231, 231, 231],
    [231, 231, 231, 224, 224, 231, 231, 231],
    [252, 252, 252, 252, 252, 252, 252, 252],
    [248, 248, 248, 248, 248, 248, 248, 248],
    [31, 31, 31, 31, 31, 31, 31, 31],
    [0, 0, 255, 255, 255, 255, 255, 255],
    [0, 0, 0, 255, 255, 255, 255, 255],
    [255, 255, 255, 255, 255, 0, 0, 0],
    [127, 63, 159, 201, 225, 241, 249, 255],
    [255, 255, 255, 255, 240, 240, 240, 240],
    [15, 15, 15, 15, 255, 255, 255, 255],
    [231, 231, 231, 224, 224, 255, 255, 255],
    [240, 240, 240, 240, 255, 255, 255, 255],
    [240, 240, 240, 240, 15, 15, 15, 15],
]

class C64Screen:
    # Commodore64 resolution - 320 x 200 pixels, or 40 x 25 characters (8 x 8 pixels each)
    screen_width = 403
    screen_height = 284
    main_width = 320
    main_height = 200
    scale = 3
    # Commodore 64 character bytes
    characters = C64_CHARACTERS
    # Commodore 64 colors - see the very interesting article here:
    #    http://unusedino.de/ec64/technical/misc/vic656x/colors/
    colors = [
        '#000000',  # black
        '#FFFFFF',  # white
        '#68372B',  # red
        '#70A4B2',  # cyan
        '#6F3D86',  # purple
        '#588D43',  # green
        '#352879',  # blue
        '#B8C76F',  # yellow
        '#6F4F25',  # orange
        '#433900',  # brown
        '#9A6759',  # light red
        '#444444',  # dark grey
        '#6C6C6C',  # grey
        '#9AD284',  # light green
        '#6C5EB5',  # light blue
        '#959595',  # light grey
    ]
    color_lookup = {
        'black': colors[0],
        'white': colors[1],
        'red': colors[2],
        'cyan': colors[3],
        'purple': colors[4],
        'green': colors[5],
        'blue': colors[6],
        'yellow': colors[7],
        'orange': colors[8],
        'brown': colors[9],
        'light red': colors[10],
        'dark grey': colors[11],
        'grey': colors[12],
        'light green': colors[13],
        'light blue': colors[14],
        'light grey': colors[15],
        # alternate lookups for those who spell 'grey' as 'gray' :)
        'dark gray': colors[11],
        'gray': colors[12],
        'light gray': colors[15],
    }

    def __init__(self):
        self.main_x0 = int(((self.screen_width - self.main_width) / 2.0) * self.scale)
        self.main_y0 = int(((self.screen_height - self.main_height) / 2.0) * self.scale)

        self.char_width, self.char_height = 8, 8
        self.char_cols = int(self.main_width / self.char_width)
        self.char_rows = int(self.main_height / self.char_height)

        self.screen_char_memory = [32, ] * (self.char_cols * self.char_rows)
        self.last_rendered_screen_char_memory = None
        fg_color = 14  # blue
        bg_color = 6  # light blue
        self.screen_color_memory = []
        for x in range(self.char_cols * self.char_rows):
            self.screen_color_memory.append([fg_color, bg_color])
        self.last_rendered_screen_color_memory = None

        master = Tk()
        self.screen = Canvas(master,
                             width=self.screen_width * self.scale,
                             height=self.screen_height * self.scale)
        self.screen.pack()
        self.set_border_color(14)
        self.set_screen_color(6)
        self.clear_screen()
        self.cursor_position = [0, 0]

    def get_screen_size(self):
        return self.screen_width, self.screen_height

    def get_resolution(self):
        return self.main_width, self.main_height

    def get_char_resolution(self):
        return self.char_cols, self.char_rows

    def get_colors(self):
        return self.colors.copy()

    def get_color(self, color):
        if type(color, int):
            return self.colors[0] if (color < 0 or color >= len(self.colors)) else self.colors[color]
        elif type(color, str):
            return self.color_lookup.get(color, self.colors[0])
        return self.colors[0]

    def constrain_coords(self, col, row):
        return max(0, min(self.char_cols -1, col)), max(0, min(self.char_rows -1, row))

    def get_char(self, col, row):
        col, row = self.constrain_coords(col, row)
        screen_memory_offset = self.get_screen_memory_offset(col, row)
        return self.screen_char_memory[screen_memory_offset]

    def get_char_colors(self, col, row):
        col, row = self.constrain_coords(col, row)
        screen_memory_offset = self.get_screen_memory_offset(col, row)
        return self.screen_color_memory[screen_memory_offset].copy()

    def set_char_colors(self, col, row, fg_color=None, bg_color=None):
        if fg_color is not None or bg_color is not None:
            col, row = self.constrain_coords(col, row)
            screen_memory_offset = self.get_screen_memory_offset(col, row)
            screen_color = self.screen_color_memory[screen_memory_offset]
            if fg_color is not None:
                screen_color[0] = fg_color
            if bg_color is not None:
                screen_color[1] = bg_color

    def set_border_color(self, color):
        color = self.colors[color]
        # top rectangle
        self.screen.create_rectangle(
            0, 0,
            (self.screen_width * self.scale), self.main_y0 - 1,
            fill=color, outline=color
        )
        # bottom rectangle
        self.screen.create_rectangle(
            0, self.main_y0 + (self.main_height * self.scale),
            (self.screen_width * self.scale), (self.screen_height * self.scale),
            fill=color, outline=color
        )
        # left rectangle
        self.screen.create_rectangle(
            0, self.main_y0,
            self.main_x0 - 1, self.main_y0 + (self.screen_height * self.scale),
            fill=color, outline=color
        )
        # right rectangle
        self.screen.create_rectangle(
            self.main_x0 + (self.main_width * self.scale), self.main_y0,
            (self.screen_width * self.scale), self.main_y0 + (self.screen_height * self.scale),
            fill=color, outline=color
        )

    def set_screen_color(self, color):
        color = self.colors[color]
        self.screen.create_rectangle(
            self.main_x0, self.main_y0,
            self.main_x0 + (self.main_width * self.scale) - 1,
            self.main_y0 + (self.main_height * self.scale) - 1,
            fill=color, outline=color
        )
        self.render()

    def clear_screen(self):
        self.screen_char_memory = [32, ] * (self.char_cols * self.char_rows)
        self.render()

    def coord_convert(self, x, y):
            return self.main_x0 + (x * self.scale), self.main_y0 + (y * self.scale)

    def plot(self, x, y, color):
        x1, y1 = self.coord_convert(x, y)
        x2, y2 = self.coord_convert(x+1, y+1)
        self.screen.create_rectangle(
            x1, y1, x2 - 1, y2 - 1,
            fill=self.colors[color], outline=self.colors[color]
        )

    def rect(self, x1, y1, x2, y2, color):
        x1, y1 = self.coord_convert(x1, y1)
        x2, y2 = self.coord_convert(x2, y2)
        self.screen.create_rectangle(
            x1, y1, x2 - 1, y2 - 1,
            fill=self.colors[color], outline=self.colors[color]
        )

    def get_screen_memory_offset(self, col, row):
        return row * self.char_cols + col

    def define_custom_characters(self, start_charcode, character_defs):
        old_character_defs = []
        for charcode, character_def in enumerate(character_defs):
            old_character_defs.append(self.characters[charcode])
            self.characters[charcode] = character_def
        return old_character_defs

    def render(self, force=False):
        screen_mem_offset = 0
        for y in range(0, self.char_rows):
            for x in range(0, self.char_cols):
                current_char = self.screen_char_memory[screen_mem_offset]
                current_fg_color, current_bg_color = self.screen_color_memory[screen_mem_offset]
                if force:
                    has_changed = True
                elif self.last_rendered_screen_char_memory is None or \
                    self.last_rendered_screen_color_memory is None:
                    has_changed = True
                else:
                    last_char = self.last_rendered_screen_char_memory[screen_mem_offset]
                    last_fg_color, last_bg_color = self.last_rendered_screen_color_memory[screen_mem_offset]
                    has_changed = last_char != current_char or \
                                  last_fg_color != current_fg_color or \
                                  last_bg_color != current_bg_color
                if has_changed:
                    self.draw_character(current_char, x, y, current_fg_color, current_bg_color)
                screen_mem_offset += 1

        self.last_rendered_screen_char_memory = self.screen_char_memory.copy()
        self.last_rendered_screen_color_memory = self.screen_color_memory.copy()

    def print(self, text=None, newline=True, inverse=False, render=True):
        if text:
            text = str(text)  # just in case they pass in a numeric rather than a string
            for c in text:
                o = ord(c)

                # need to translate the codes of some characters to map
                # to the internal character schema, unfortunately
                if 32 <= o <= 63:
                    # the following characters are all fine - use as is
                    # [space] ! " # $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < > ?
                    pass
                elif 96 <= o <= 122:
                    # lowercase a-z
                    o = 257 + (o - 97)
                elif 64 <= o <= 94:
                    # uppercase A-Z, as well as...
                    # @ [ ] ^
                    o -= 64

                if inverse:
                    # add 128 to make it inverse colored
                    o += 128
                self.put_character(o, *self.cursor_position)
                self.move_cursor_right()
        if newline:
            self.do_newline()
        if render and (text or newline):
            self.render()

    def print_charcodes(self, charcodes=[], newline=True, render=True):
        if charcodes:
            for c in charcodes:
                self.put_character(c, *self.cursor_position)
                self.move_cursor_right()
        if newline:
            self.do_newline()
        if render and (charcodes or newline):
            self.render()

    def scroll_up(self):
        # scroll up character memory, insert blank line
        self.screen_char_memory = self.screen_char_memory[self.char_cols:]
        self.screen_char_memory.extend([32, ] * self.char_cols)
        # scroll up color memory, copy last row values onto end
        self.screen_color_memory = self.screen_color_memory[self.char_cols:]
        self.screen_color_memory.extend(self.screen_color_memory[-self.char_cols:].copy())

    def move_cursor_up(self):
        self.cursor_position[1] = max(0, self.cursor_position[1] - 1)

    def move_cursor_left(self):
        self.cursor_position[0] -= 1
        if self.cursor_position[0] < 0:
            self.cursor_position[0] = self.char_cols - 1
            self.cursor_position[1] -= 1
            if self.cursor_position[1] < 0:
                self.cursor_position[1] = 0

    def move_cursor_down(self):
        self.cursor_position[1] += 1
        if self.cursor_position[1] >= self.char_rows:
            self.cursor_position[1] = self.char_rows - 1
            self.scroll_up()

    def move_cursor_right(self):
        self.cursor_position[0] += 1
        if self.cursor_position[0] >= self.char_cols:
            self.cursor_position[0] = 0
            self.cursor_position[1] += 1
            if self.cursor_position[1] >= self.char_rows:
                self.cursor_position[1] = self.char_rows - 1
                self.scroll_up()

    def do_newline(self):
        self.cursor_position[0] = 0
        self.move_cursor_down()

    def move_cursor_to(self, col, row):
        col, row = self.constrain_coords(col, row)
        self.cursor_position[0] = col
        self.cursor_position[1] = row

    def put_character(self, char_code, col, row, fg_color=None, bg_color=None):
        screen_mem_offset = self.get_screen_memory_offset(col, row)
        self.screen_char_memory[screen_mem_offset] = char_code
        screen_color = self.screen_color_memory[screen_mem_offset]
        if fg_color is not None:
            screen_color[0] = fg_color
        if bg_color is not None:
            screen_color[1] = bg_color

    def put_characters(self, char_codes, col, row, fg_color=None, bg_color=None):
        screen_mem_offset = self.get_screen_memory_offset(col, row)
        for idx, char_code in enumerate(char_codes):
            current_mem_offset = screen_mem_offset + idx
            self.screen_char_memory[current_mem_offset] = char_code
            screen_color = self.screen_color_memory[current_mem_offset]
            if fg_color is not None:
                screen_color[0] = fg_color
            if bg_color is not None:
                screen_color[1] = bg_color

    def draw_character(self, char_code, col, row, fg_color=None, bg_color=None):
        if fg_color is None or bg_color is None:
            current_fg, current_bg = self.get_char_colors(col, row)
            fg_color = current_fg if fg_color is None else fg_color
            bg_color = current_bg if bg_color is None else bg_color

        top_x = col * self.char_height
        top_y = row * self.char_width
        # clear the character square
        self.rect(top_x, top_y, top_x + self.char_width, top_y + self.char_height, bg_color)
        character_def = self.characters[char_code % len(self.characters)]
        for line_idx, value in enumerate(character_def):
            y1 = top_y + line_idx
            y2 = y1 + 1
            if value == 255:
                self.rect(top_x, y1, top_x + self.char_width, y2, fg_color)
            else:
                for bit_idx, bit_value in enumerate([1, 2, 4, 8, 16, 32, 64, 128]):
                    if value & bit_value:
                        self.plot(top_x + bit_idx, top_y + line_idx, fg_color)
        self.put_character(char_code, col, row, fg_color, bg_color)


custom_characters = [
    [255, 255, 255, 255, 255, 255, 255, 255],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [85, 170, 85, 170, 85, 170, 85, 170],
    [0, 60, 24, 60,126, 126, 126, 60],
    [0, 56, 100, 114, 95, 73, 41, 31],
    [20, 42, 20, 20, 93, 93, 62, 99],
    [60, 126, 255, 255, 255, 253, 255, 255],
    [60, 102, 195, 129, 129, 129, 133, 129],
    [129, 66, 36, 0, 0, 36, 66, 129],
    [0, 60, 66, 66, 66, 66, 60, 0],
    [76, 158, 170, 190, 84, 30, 37, 88],
    [0, 56, 84, 124, 56, 44, 68, 102],
    [0, 8, 28, 42, 127, 85, 65, 34],
]

c64_screen = C64Screen()
c64_screen.clear_screen()
c64_screen.print('abcdefghijklmnopqrstuvwxyz')
c64_screen.print('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
c64_screen.print('0123456789')
c64_screen.print('!"#$%&\'()*+,-./')
c64_screen.print(':;<>?')
c64_screen.print('@^[]')
c64_screen.print('The rain in spain stays mainly on the plain!')
c64_screen.print_charcodes(range(0, 512))
c64_screen.render()
# c64_screen.define_custom_characters(1, custom_characters)
# c64_screen.render(force=True)


mainloop()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import PIL


def square_fractal(n, start=0):
    if n == 2:
        return np.arange(start, start + 4).reshape((2, 2))
    nn = n // 2
    arr1 = square_fractal(nn, start)
    arr2 = square_fractal(nn, start + nn ** 2)
    arr3 = square_fractal(nn, start + 2 * (nn ** 2))
    arr4 = square_fractal(nn, start + 3 * (nn ** 2))
    return np.block([[arr1, arr2], [arr3, arr4]])


square4 = square_fractal(4)
print("-" * 20)
print(square4)

square16 = square_fractal(16)
print("-" * 20)
print(square16)

im = PIL.Image.fromarray(np.uint8(square16), "L")
# im = im.resize((512, 512), PIL.Image.NEAREST)
im.save("fractal_square.bmp")
im.save("fractal_square.png")

rgbarr = np.ones((16, 16, 3), "uint8")
rgbarr = rgbarr * 32
rgbarr[..., 1] = square16
rgbarr[..., 2] = square16
im = PIL.Image.fromarray(rgbarr)
# im = im.resize((256, 256), PIL.Image.NEAREST)
im.save("fractal_square.rgb.png")

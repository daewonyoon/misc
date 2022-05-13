# std
import math

# 3rd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


## problem ##############################
## the series `a_n`` is defined by
##  a_0 = 1
##  a_{n+1} = sin( a_n )
##
## will the sum `s_n`` converge or not?
########################################

def main():
    N = 300000

    inv_x_series = np.array([1 / (i + 1) for i in range(N)])
    sin_rec_x_series = [1]
    for _ in range(N - 1):
        sin_rec_x_series.append(math.sin(sin_rec_x_series[-1]))
    sin_rec_x_series = np.array(sin_rec_x_series)

    df = pd.DataFrame({"1/x": inv_x_series, "fx": sin_rec_x_series})
    df.plot(grid=True)
    plt.show()

    df2 = pd.DataFrame({"diff": sin_rec_x_series - inv_x_series})
    df2.plot(grid=True)
    plt.show()


if __name__ == "__main__":
    main()
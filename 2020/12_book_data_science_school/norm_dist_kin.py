import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import scipy.stats


def show_pdfcdf(rv, m, s):
    mm = m
    ss = 6 * s
    xx = np.linspace(mm - ss, mm + ss, 200)
    pdf = rv.pdf(xx)
    cdf = rv.cdf(xx)

    plt.grid(True)
    plt.plot(xx, pdf)
    plt.plot(xx, cdf)
    plt.title(f" Norm(m={m}, s^2={s*s:.3f}) Pdf & Cdf ")
    plt.savefig("dist.png")
    plt.show()


m, s = 50.2, np.sqrt(48 / 100)
rv = sp.stats.norm(m, s)

show_pdfcdf(rv, m, s)

x1, x2 = 47, 51
print(f"Prob ({x1} < x < {x2}) =", rv.cdf(x2) - rv.cdf(x1))

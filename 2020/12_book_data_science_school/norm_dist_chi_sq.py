# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import pandas as pd
import scipy as sc
import scipy.stats

import seaborn as sns
import matplotlib.pyplot as plt


# %%
dist = scipy.stats.norm()

def plot_chisq(df, ax):
    x = np.linspace(0, 20, 399)
    ax.plot(x, scipy.stats.chi2.pdf(x, df))

def do(n_sample):
    xs = []
    ms = []
    xsqs = []

    for _ in range(200000):
        x = dist.rvs(n_sample)
        xs.append(x)
        ms.append(x.mean())
        xsqs.append((x*x).sum())

    xs = np.array(xs)
    ms = np.array(ms)
    xsqs = np.array(xsqs)

    f, axes = plt.subplots(2, 1, figsize=(12, 12))    

    sns.distplot(ms, ax=axes[1])
    #plt.show()
    plot_chisq(n_sample, axes[0])
    sns.distplot(xsqs, ax=axes[0])
        


# %%
do(1)


# %%
do(2)


# %%
do(3)


# %%
do(4)


# %%
do(5)


# %%



# %%




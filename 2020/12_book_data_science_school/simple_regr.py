import numpy as np
import pandas as pd
import scipy as sc
import statsmodels.api as sm
import matplotlib.pyplot as plt

df = pd.DataFrame(
    {
        "weight": list(map(int, "94 95 107 108 116 117 122 125 128 129 134 141".split())),
        "pressure": list(map(int, "97 100 106 119 111 117 121 124 116 131 125 127".split())),
    }
)

print(df)

#df.plot.scatter(x="weight", y="pressure", grid=True)
#plt.show()

model = sm.OLS.from_formula("pressure ~ weight", data=df)
res = model.fit()
print(res.summary())


df.plot.scatter(x="weight", y="pressure", grid=True)
xs = pd.DataFrame(np.linspace(df["weight"].min(), df["weight"].max(), 100))
ys = res.predict(xs)
plt.plot(xs, ys)
plt.show()
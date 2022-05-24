import matplotlib.pyplot as plt
import pandas as pd
z = pd.read_csv("zillow.csv")
print(z)
zl=z.groupby(["Beds"])
plt.figure(figsize=(50, 20))
fig, ax = plt.subplots(nrows=1,ncols=len(zl.groups.keys()))
for (key,ax) in zip(zl.groups.keys(),ax.flatten()):
    zl.get_group(key).plot(ax=ax)
    ax.set_title(key)
    ax.legend()

plt.show()#
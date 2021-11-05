import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("./data_source/test.csv")

plt.figure(figsize=(6, 6), dpi=80)
plt.figure(1)
ax1 = plt.subplot(211)
plt.plot(df.x)
plt.plot(df.y)
plt.show()
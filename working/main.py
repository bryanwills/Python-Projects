import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('memes.csv')
x = data['Memes']
y = data['Dankness']

np.corrcoef(x, y)

plt.scatter(x, y)
plt.title('A plot to show the correlation between memes and dankness')
plt.xlabel('Memes')
plt.ylabel('Dankness')
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)), color='black')
plt.show()

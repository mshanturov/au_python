import pandas
import matplotlib.pyplot as plt
from scipy import stats

df1 = pandas.read_csv("exp.csv")
ser = df1['values']

print(stats.kstest(ser, 'norm', (ser.mean(), ser.std()), N=len(ser)))

df1.plot(kind='bar', xlabel='Number ', ylabel='U, В', title='Data')
df1.plot.kde(xlabel='Number ', title='Data')
plt.show()

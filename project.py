import csv
import statistics
import plotly.express as px
import pandas as pd
import math
import random
import plotly.figure_factory as ff

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
fig = ff.create_distplot([data],["reading_time"], show_hist=False)
fig.show()

population =statistics.mean(data)
print("Mean is", population)
st=statistics.stdev(data)
print("stdev is", population)

dataset=[]
for i in range(0,1000):
    rand = random.randint(0,len(data))
    value = data[rand]
    dataset.append(value)
mean =statistics.mean(dataset)
stdeev =statistics.stdev(dataset)
print("mean is :",mean)
print("stdev is :",stdeev)
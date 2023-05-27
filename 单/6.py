import pandas as pd
import matplotlib.pyplot as plt

"""
运动员的年龄分布：
绘制一个直方图来显示运动员的年龄分布情况
从中可以观察到参加奥运会的运动员的年龄分布情况
"""
df = pd.read_csv("athlete_events.csv")

age_data = df["Age"].dropna()

age_data = age_data.astype(int)

plt.hist(age_data, bins=range(10, 76), edgecolor="black")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Distribution of Athletes' Age")
plt.xticks(range(10, 76, 5))
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np



def get_length(file_path):

    df = pd.read_excel(file_path)

    first_column = df.iloc[1:, 0]

    return len(first_column)



length1 = get_length('emotion/emotion_positive.xlsx')
length2 = get_length('emotion/emotion_negative.xlsx')



categories = ['positive', 'negative']
values = [length1,length2]

# 设置渐变颜色
colors = plt.cm.Reds(np.linspace(0.2, 1, len(categories)))
#colors = plt.cm.Blues(np.linspace(0.2, 1, len(categories)))
#colors = plt.cm.Greens(np.linspace(0.2, 1, len(categories)))


bar_width = 0.2


fig, ax = plt.subplots(figsize=(11, 7))  # Adjust the width and height as needed


ax.barh(categories, values, color=colors, height=bar_width)


ax.set_xlabel('Quantity', fontsize=17)
ax.set_ylabel('Emotional Categories', fontsize=17)


# 网格
ax.set_axisbelow(True)
ax.grid(True, which='major', linestyle='--', linewidth=0.5)


plt.savefig('bar/Bars.png')

#plt.show()

print("条形图绘制完成")


import pandas as pd
import matplotlib.pyplot as plt


def get_length(file_path):

    df = pd.read_excel(file_path)

    first_column = df.iloc[1:, 0]

    return len(first_column)



length1 = get_length('emotion/emotion_positive.xlsx')
length2 = get_length('emotion/emotion_negative.xlsx')


data = [length1, length2]

total = sum(data)

percentages = [(value / total) * 100 for value in data]

labels = ['positive', 'negative']

# 创建渐变的红色色带
colors = plt.cm.Reds([i / float(len(labels)) for i in range(len(labels))])


plt.pie(percentages, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)


plt.savefig("pie/pie.png")

plt.clf()

print("饼图绘制完成")








### 您好！下面是此项目文件的相关信息：


## 4月3日紧急维护：
由于微博的变动，原爬虫无法正常工作，现已将爬虫程序更新为可用版本。下面是具体的变动和优化内容：

### 1. 新爬虫如何爬取目标微博

新爬虫已无需繁琐地查看帖子id，只需在Crawl_jiagu.py第89行对应位置修改为目标微博的网址即可

![image](https://github.com/Kawabata0223/Programs-Based-on-jiagu_ZUELer/blob/master/pic/%E6%AD%A3%E7%A1%AE%E7%BD%91%E7%AB%99.png)

![image](https://github.com/Kawabata0223/Programs-Based-on-jiagu_ZUELer/blob/master/pic/%E8%BE%93%E5%85%A5%E7%BD%91%E5%9D%80.png)

> 注1：查看目标微博网址的方法

> 点击目标帖子的时间即可进入该帖，进入后复制网址即可
![image](https://github.com/Kawabata0223/Programs-Based-on-jiagu_ZUELer/blob/master/pic/%E8%BF%9B%E5%85%A5%E5%B8%96%E5%AD%90.png)

> 注2：无效网址

> 从首页进入的帖子网址是无法使用的，如下图所示。通过热搜榜或搜索进入的帖子网址则可正常使用
![image](https://github.com/Kawabata0223/Programs-Based-on-jiagu_ZUELer/blob/master/pic/%E9%A6%96%E9%A1%B5.png)


### 2. 修改爬取评论数量的方法
对于成千上万条评论的帖子，爬取将花费相当长的时间，可以通过修改Crawl_jiagu.py第83行的对应数字来控制爬取评论的数量

![image](https://github.com/Kawabata0223/Programs-Based-on-jiagu_ZUELer/blob/master/pic/%E9%A1%B5%E6%95%B0%E9%99%90%E5%88%B6.png)

--------------------------------


## 一、python 推荐版本：3.10


## 二、所需库：
pandas
matplotlib
numpy
json
csv
requests
time
fake_useragent
seaborn
joypy
openpyxl
jiagu
Pillow（PIL）
base64
io
jieba
wordcloud
imageio
os


## 三、项目介绍

### 本项目基于 jiagu 库，可自动爬取目标微博评论区的评论，生成相关<font color="#ff0000">数据图</font>、<font color="#ff0000">数据文件</font>和<font color="#ff0000">情感分析报告</font>以及<font color="#ff0000">标签化评论区</font>。

> Jiagu是一个基于Python的中文文本处理工具包，专门用于自然语言处理（NLP）任务。它提供了一系列功能，包括分词、词性标注、命名实体识别、关键词提取、文本分类、情感分析等，旨在帮助开发者轻松地进行中文文本处理和各种NLP任务。Jiagu 提供了**情感分析功能**，可以自动识别文本中的情感倾向，**将文本划分为积极或消极**。这对于从大量的文本数据中提取有用信息或进行情感监测非常有用。

> 本项目为中南财经政法大学统数学院“基于大语言模型的网络舆情态势感知研究——舆情评论的群体情绪与语义标签化分析”项目**中期研究进展情况**的部分程序文件。



## 四、使用方法

### 1. 查看目标微博的 id

![image](https://github.com/Kawabata0223/Programs-Based-on-jiagu_ZUELer/blob/master/pic/278919608-89dcbb20-5c15-4e84-9e72-520babbaf057.png)

> 在 examples 文件夹中有各示例帖子的 id

![image](https://github.com/Kawabata0223/Programs-Based-on-jiagu_ZUELer/blob/master/pic/Pasted%20image%2020240315130233.png)


### 2. 将 Crawl_jiagu.py 中77行的相应位置改为目标微博的 id


![image](https://github.com/Kawabata0223/Programs-Based-on-jiagu_ZUELer/blob/master/pic/Pasted%20image%2020240315212119.png)

### 3. 运行 Startup_jiagu.py



### 4. 直接打开 jiagu_Summary.html 查看分析报告



### 5. 选择 pycharm 打开 jiagu_Page.html，在 pycharm 中用浏览器打开，生成标签化评论区（直接点开将无法正常载入评论）


![image](https://github.com/Kawabata0223/Programs-Based-on-jiagu_ZUELer/blob/master/pic/Pasted%20image%2020240315213748.png)


![image](https://github.com/Kawabata0223/Programs-Based-on-jiagu_ZUELer/blob/master/pic/Pasted%20image%2020240315213958.png)


![image](https://github.com/Kawabata0223/Programs-Based-on-jiagu_ZUELer/blob/master/pic/Pasted%20image%2020240315214257.png)


## 五、程序说明

![image](https://github.com/Kawabata0223/Programs-Based-on-jiagu_ZUELer/blob/master/pic/Pasted%20image%2020240315223356.png)

Startup_jiagu.py
次序运行其他程序文件，自动生成目标微博的分析结果

Crawl_jiagu.py
爬取目标微博评论区，并保存为csv文件（files/data.csv）

Preprocessing.py
对csv文件进行预处理，包括添加列标题，删去空行，保存为xlsx文件（files/comments.xlsx）

label_jiagu.py
使用 jiagu 对评论逐条进行积极或消极判定，将其分为两组，相关 xlsx 文件均存入 labels 文件夹

NoHeader.py
去除comments_score.xlsx内数据的列名，为生成标签化评论区做准备

pie_jiagu.py
根据分析结果，绘制积极消极占比情况的饼图，图片存入pie文件夹

bar_jiagu.py
根据分析结果，绘制积极消极数量的条形图，图片存入bar文件夹

wordcloud_jiagu.py
根据所有评论的文本，绘制词云图，图片存入wordc1oud文件夹

jiagu_Summary.py
根据以上步骤绘制的图表与数据文件，生成一份综合报告HTML文件

jiagu_Page.html
在 pycharm 中用浏览器打开，生成标签化评论区


## 六、示例文件

在 examples 文件夹中有各事件的数据结果，分析报告


![image](https://github.com/Kawabata0223/Programs-Based-on-jiagu_ZUELer/blob/master/pic/Pasted%20image%2020240315123520.png)

## 七、补充说明

如果您无法正常运行程序，烦请通过以下方式联系我，您的任何批评指正都将使我们做的更好，感谢！

QQ：2859571794
微信：koregajiyuuda


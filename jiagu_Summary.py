import base64
from PIL import Image
import io



with open('bar/bars.png', 'rb') as image_file2:
    encoded_image2 = base64.b64encode(image_file2.read()).decode('utf-8')



output_width = 1000  # 调整后的宽度
output_height = 1000  # 调整后的高度

image_path3 = 'wordc1oud/wordcloud_jiagu.png'

with open(image_path3, 'rb') as image_file:
    original_image = Image.open(image_file)
    resized_image = original_image.resize((output_width, output_height))

    # 将调整大小后的图片编码为Base64格式
    buffered = io.BytesIO()
    resized_image.save(buffered, format="PNG")
    encoded_image3 = base64.b64encode(buffered.getvalue()).decode('utf-8')




output_width = 1000
output_height = 750

image_path5 = 'pie/pie.png'

with open(image_path5, 'rb') as image_file:
    original_image = Image.open(image_file)
    resized_image = original_image.resize((output_width, output_height))

    buffered = io.BytesIO()
    resized_image.save(buffered, format="PNG")
    encoded_image5 = base64.b64encode(buffered.getvalue()).decode('utf-8')


#-------------------------------------------


# 构建HTML代码
html_content = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Summary Based on jiagu</title>
    <style>
        h1 {{
            font-size: 50px;  /* 设置中文标题的字体大小，单位可以根据需要调整 */
            margin-left: 20px; 
        }}
        
    </style>
</head>
<body>
    <h1>饼图</h1>
    <img src="data:image/jpeg;base64,{encoded_image5}" alt="Embedded Image">
    <h1>条形图</h1>
    <img src="data:image/jpeg;base64,{encoded_image2}" alt="Embedded Image">
    <h1>词云图</h1>
    <img src="data:image/jpeg;base64,{encoded_image3}" alt="Embedded Image">
    
    <h1>点击下面的链接下载Excel文件</h1>
    <a href="emotion/comments_emotion.xlsx" style="font-size: 40px; margin-left: 20px;">总文件</a><br>
    <a href="emotion/emotion_positive.xlsx" style="font-size: 40px; margin-left: 20px;">positive</a><br>
    <a href="emotion/emotion_negative.xlsx" style="font-size: 40px; margin-left: 20px;">negative</a><br>
    
    
</body>
</html>
'''

# 将HTML代码写入文件
with open('jiagu_Summary.html', 'w', encoding='utf-8') as html_file:
    html_file.write(html_content)

print("报告创建完成")













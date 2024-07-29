import pdfplumber
#打开PDF文件
with pdfplumber.open('畸变不变光电混合图像识别技术研究_王国田.pdf')as pdf :
    for i in pdf.pages:#遍历页
        print(i.extract_text())#extract_text()方法提取内容
        print(f'--------------第{i.page_number}页结束')
